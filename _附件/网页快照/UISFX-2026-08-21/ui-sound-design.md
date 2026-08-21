# UI sound design and interface sound effects

> UI SFX is an open-source library of 936 interface sound effects: 78 semantic UI cues in 12 interchangeable sonic styles.

UI sound design is the practice of using brief, intentional audio cues to reinforce interaction, status, navigation, progress, and outcomes. Good interface sound effects clarify what happened without replacing visual, textual, haptic, or accessible feedback.

## What UI SFX provides

- 78 semantic cues across 13 interaction categories
- 12 complete sound packs for different product personalities
- 72 brief one-shots and 6 seamless loops
- MP3 and Ogg assets for native apps and games
- A zero-dependency Web Audio runtime for browser products
- MIT-licensed code and CC0 audio

## Install

```bash
npm install uisfx
```

```ts
import { createUISFX } from 'uisfx'

const ui = createUISFX({ pack: 'minimal', volume: 0.7 })
ui.play('success')
```

Use one shared client-side player. Start audio after user interaction, add a persistent sound preference, and stop loop cues with the visible state they represent.

## Sound packs

| Pack | Character | Good fit |
| --- | --- | --- |
| `minimal` | Dry, precise, almost invisible. | Productivity, SaaS, system UI |
| `soft` | Rounded felt, warm and reassuring. | Mobile, wellness, friendly SaaS |
| `glass` | Bright, crystalline, and premium. | Media, finance, luxury products |
| `arcade` | Chunky pixels and cheerful voltage. | Games, streaks, gamified learning |
| `mechanical` | Switches, relays, and firm detents. | Devtools, hardware, industrial UI |
| `organic` | Wood, water, breath, and small stones. | Education, kids, calm games |
| `dreamy` | Airy blooms, soft light, and slow sparkle. | Creative tools, wellness, ambient apps |
| `scifi` | Clean holographic pings with a restrained digital shimmer. | AI tools, spatial UI, futuristic games |
| `rubber` | Tactile elastic taps with a quick, friendly rebound. | Kids, playful mobile, casual games |
| `cinematic` | Deep impacts, polished tails, and quiet scale. | Premium media, games, dramatic moments |
| `studio` | Tactile editing precision with warm cinematic restraint. | Film, audio, and AI creative tools |
| `zen` | Pure tones, dry wood, and brief washi detail. | Mindfulness, reading, writing, calm productivity |

## Documentation

- Interactive showcase: https://uisfx.com/
- UI sound design guide: https://uisfx.com/ui-sound-design
- Coding-agent guide: https://uisfx.com/docs/agent-guide.md
- Semantic catalog: https://uisfx.com/uisfx-catalog.json
- npm package: https://www.npmjs.com/package/uisfx
- Source: https://github.com/romainsimon/uisfx
