# Istiqamah Digital daily post kit

Everything a fresh session needs to make one day's Instagram post for @istiqamah.digital.

## Founder's standing rules (always)

- Never post, publish or send anything anywhere. Only make the files and save them here; the founder posts herself.
- Nothing may sound AI-written. Every line must sound like her.
- Load and follow ALL of these skills for ANY piece of content, every time:
  `my-writing-style`, `carousel-writer`, `hifdh-storytelling`, `hifdh-sales-structure`, `hifdh-conversion-strategist`.
  If a skill isn't available in the session, say so in `notes.txt` instead of guessing.

## What to make each day

1. Open `CALENDAR.md`. Day 1 is the first date in its header; count days from there to today (wrap after day 28).
2. Make that day's post: Carousel (5 to 6 slides), Single (1 slide) or Infographic (1 to 3 slides).
3. Use only that row's topic, pain and cost. Do not invent new topics, pains, claims, quotes or numbers.
4. Save the finished files to `posts/YYYY-MM-DD/` (slide-01.png ..., or .mp4 for video slides) plus `caption.txt`, then commit and push.

## Look (copy `examples/nt.py` and `examples/v4.py`)

- 1080x1350. Background #2b1a10, text #f7f5f2, highlight #f2e600 with dark brown text, rounded 8px.
- Headline Playfair Display 800 (66 to 92px). Body Jost 500 (min 40px).
- Rounded inset border at 24px, logo `assets/logo.png` top left (112px wide), slide count top right ("2/6").
- Bottom-left teaser line with hand-drawn arrow on every slide but the last.
- One graphic per slide: cards, stats, bars, week grid, or a real photo.
- Real photos only: `assets/desk.jpg` (open Mushaf), `assets/desk2.jpg` (closed Mushaf on desk). Any new photo the founder adds to `assets/` can be used too.
- Video: `assets/quran.mp4` (page turning) for a hook slide; `assets/montage.mp4` (real planner footage) for every planner slide. Never draw a fake planner screen.
- Render with Playwright (`examples/render-nt.js`); a video slide is a transparent hole in the PNG with the clip overlaid by ffmpeg (see how `nt.py` slide 3 was built). H.264, silent.
- Check every slide before saving: nothing cut off, nothing past 90px side margins, nothing touching the logo, count or teaser.

## Voice (the founder's own)

- Plain, conversational sentences joined with "and" and commas. Direct statement, then a "but" turn.
- Hot-take energy: hooks should ruffle feathers a little ("Unpopular opinion: ...").
- "Consistent" is the anchor word. "Inshallah" where natural. Few words per slide; people don't read.
- Never: em dashes, "not X, but Y", "quietly", "here's the truth", corporate words, hearts or flower emojis.
- It's a "planner", never a "system". No promises like "never forget" or "your Hifdh gets stronger".
- Never shame, never use fear about losing the Qur'an, never present anything as a religious ruling.
- Any hadith or reward must come from the founder's HIFDH-KNOWLEDGE file with its reference; if it's not available, skip that claim and say so.

## Sales days

- End on the planner: real `montage.mp4` footage, "That's why I made the Hifdh Planner", one thing it does, "Comment PLANNER and I'll send you the link", "$16.99 one-time".
- Nurture days may end with a soft planner line or none.

## Caption

Skimmable: short lines, the hook idea in a new angle (don't repeat the slides), one "send this to someone who..." line, Comment PLANNER, $16.99 one-time on sales days, 4 hashtags.
