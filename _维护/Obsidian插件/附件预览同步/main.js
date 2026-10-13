const { Plugin, requestUrl } = require('obsidian');

const DIRECTORY_API = 'https://api.github.com/repos/youfei0719/glint-vault/contents/_%E9%99%84%E4%BB%B6%2F%E6%94%B6%E8%97%8F%E9%A2%84%E8%A7%88';
const PREVIEW_DIRECTORY = '_附件/收藏预览';
const INTERVAL_MS = 5 * 60 * 1000;
const EXTENSIONS = new Set(['png', 'jpg', 'jpeg', 'gif', 'webp', 'avif', 'svg', 'mp4']);

function isAllowedFile(entry) {
  if (!entry) return false;
  const extension = String(entry.name || '').split('.').pop().toLowerCase();
  return entry.type === 'file' && typeof entry.download_url === 'string'
    && Number.isSafeInteger(entry.size) && entry.size > 0
    && /^[^/\\]+$/.test(entry.name) && !entry.name.includes('..')
    && EXTENSIONS.has(extension);
}

function hasExpectedHeader(name, body) {
  const bytes = new Uint8Array(body);
  const extension = name.split('.').pop().toLowerCase();
  const starts = (...values) => values.every((value, index) => bytes[index] === value);
  if (extension === 'png') return starts(0x89, 0x50, 0x4e, 0x47);
  if (extension === 'jpg' || extension === 'jpeg') return starts(0xff, 0xd8);
  if (extension === 'gif') return starts(0x47, 0x49, 0x46);
  if (extension === 'webp') return starts(0x52, 0x49, 0x46, 0x46) && String.fromCharCode(...bytes.slice(8, 12)) === 'WEBP';
  if (extension === 'mp4') return String.fromCharCode(...bytes.slice(4, 8)) === 'ftyp';
  if (extension === 'svg') return new TextDecoder().decode(bytes.slice(0, 512)).includes('<svg');
  return bytes.length > 16;
}

module.exports = class GlintVaultPreviewSync extends Plugin {
  async onload() {
    this.running = false;
    this.settings = { collectionRoot: '', ...(await this.loadData() || {}) };
    this.status = this.addStatusBarItem();
    this.status.setText('预览同步：准备中');
    this.registerInterval(window.setInterval(() => void this.sync(), INTERVAL_MS));
    await this.sync();
  }

  async sync() {
    if (this.running) return;
    this.running = true;
    try {
      const listing = await requestUrl({ url: DIRECTORY_API, method: 'GET' });
      if (!Array.isArray(listing.json)) throw new Error('远端附件目录返回格式异常');
      let restored = 0;
      let pending = 0;
      for (const entry of listing.json.filter(isAllowedFile)) {
        const target = [this.settings.collectionRoot, PREVIEW_DIRECTORY, entry.name]
          .filter(Boolean).join('/');
        if (await this.app.vault.adapter.exists(target)) continue;
        pending += 1;
        const download = await requestUrl({ url: entry.download_url, method: 'GET' });
        if (!download.arrayBuffer || download.arrayBuffer.byteLength !== entry.size) {
          throw new Error(`${entry.name} 下载大小不符`);
        }
        if (!hasExpectedHeader(entry.name, download.arrayBuffer)) {
          throw new Error(`${entry.name} 不是有效的预览媒体`);
        }
        const temporary = `${target}.syncing`;
        await this.app.vault.adapter.writeBinary(temporary, download.arrayBuffer);
        if (await this.app.vault.adapter.exists(target)) {
          await this.app.vault.adapter.remove(temporary);
          continue;
        }
        await this.app.vault.adapter.rename(temporary, target);
        restored += 1;
      }
      const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
      this.status.setText(restored ? `预览同步：已补 ${restored} 张` : `预览同步：正常 ${time}`);
      await this.saveData({ ...this.settings, lastSuccess: new Date().toISOString(), restored, pending });
    } catch (error) {
      console.error('Glint 收藏预览同步失败', error);
      this.status.setText('预览同步：远端检查失败');
    } finally {
      this.running = false;
    }
  }
};
