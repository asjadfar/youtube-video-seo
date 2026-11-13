# YouTube Video SEO Skill

A Claude skill for YouTube video SEO — long-form videos and Shorts — built from Asjad's real channel work. Claude handles all the work end to end — keywords, titles, descriptions, tags, thumbnail brief, end screens and cards, upload checklist, and the performance review — with the owner involved only for the decisions, accounts, sign-ins and approval gates. It is modeled on the live kids' learning channel Bunny Sounds, where every video teaches something: sounds, animals, colors, numbers, letters.

## What it does

Takes one video from brief to published-and-reviewed in one repeatable workflow:

1. **Brief** — video type, topic, learning goal, audience, main keyword, what is actually in the video, playlist, thumbnail source, links.
2. **Keywords** — one main keyword per video, plus 3–5 supporting keywords, all true of the video.
3. **Title** — keyword-first, curiosity + clarity, under 60 characters where possible, 3 options for the owner to pick from, with before/after examples.
4. **Description** — keyword + promise in the first 2 lines, what the video teaches, timestamps/chapters for long-form, links, 2–3 hashtags maximum.
5. **Tags** — 5–15 tags, main keyword first, total under 500 characters, no duplicates, no stuffing.
6. **Thumbnail** — one clear subject, 3–5 words of big readable text, high contrast, consistent channel style; different guidance for long-form vs Shorts.
7. **End screens and cards** — last 20 seconds, next video in the same series, 1–2 cards, links checked.
8. **Upload checklist + approval gate** — nothing is uploaded until the owner approves the exact title, description, tags and thumbnail.
9. **Performance review** — CTR, average view duration / watch time, and traffic sources at 7 and 28 days, with what to change when CTR is low vs when watch time is low.

## Who does what — Claude handles all the work end to end

Claude runs every step — brief, keywords, titles, descriptions, tags, thumbnail brief, end screens, cards, checklists, performance checks. The owner is involved only at three points: (1) decisions only the owner can make (video topic and learning goal, main keyword, thumbnail photo or frame, links); (2) accounts, sign-ins and money (YouTube Studio sign-in, uploading, the made-for-kids setting, paying for anything — all on the owner's own device); and (3) approval gates (title, description, tags, thumbnail before anything is published). The two honest exceptions are YouTube Studio access (browser with the owner's sign-in, or files the owner shares) and the thumbnail image itself (Claude writes the brief; the image comes from a frame, photo or design the owner makes or approves). Everything else is Claude's work — do not hand it back to the owner as homework.

## The live example channel

- **Channel:** Bunny Sounds — https://www.youtube.com/@BunnySoundsKids
- **Handle:** @BunnySoundsKids, channel ID UCwXlgPBRbPoGMkbLwTYviuw, country United States, language English
- **What every video teaches:** sounds, animals, colors, numbers, letters — a video that teaches nothing does not fit this channel
- **Characters (constant):** the same white bunny with the blue bow as host, plus the same six friends — cow, lion, elephant, dog, duck, pig
- **Long-form:** horizontal 16:9, 1280x720, 3–5 minutes each (Episode 1: "Count 1 to 10 with Bunny", about 4 minutes)
- **Shorts:** 60 seconds, portrait 9:16 vertical
- **Monetisation target:** YouTube Partner Program — 1,000 subscribers + 4,000 public watch hours in 12 months for long-form
- **Built by:** Asjad Farooq, Shopify Store Designer — Fiverr gig https://www.fiverr.com/s/L34yBpA (Basic $80, Standard $180, Premium $350, unlimited revisions)

## Files

```
youtube-video-seo/
├── README.md                                  # this file
└── youtube-video-seo/
    ├── SKILL.md                               # the Claude skill — the workflow itself
    ├── scripts/
    │   └── check_seo.py                       # scores a title / description / tags set (0–100, pass is 80+)
    └── templates/
        ├── title-formulas.md                  # 6 title formulas with worked examples
        ├── description-long-form.md           # description template for long-form + worked example
        ├── description-shorts.md              # description template for Shorts + worked example
        └── upload-checklist.md                # brief + upload checklist + approval gate + performance review
```

## Setup

### 1. Get the brief first

Fill in `templates/upload-checklist.md` (Step 1 of `SKILL.md`) with the owner: video type, topic, learning goal, audience, main keyword, what is in the video, playlist, thumbnail source, links. Do not start writing until the owner confirms the brief.

### 2. Score every title / description / tags set before the approval gate

Write the title, description and tags into a JSON file and run the checker:

```bash
python3 youtube-video-seo/scripts/check_seo.py seo.json
```

The JSON file looks like this (use the real title, keyword, description and tags for the video):

```json
{
  "title": "Count 1 to 10 for Kids with Bunny | Numbers",
  "keyword": "count 1 to 10 for kids",
  "description": "Count 1 to 10 for kids with Bunny! In this fun numbers video, toddlers learn to count from 1 to 10 with Bunny and friends.\n\nIn this video, your child will learn the numbers 1 to 10 with Bunny, the cow, the lion, the elephant, the dog, the duck and the pig.\n\n#BunnySounds #CountingForKids #KidsLearning",
  "tags": ["count 1 to 10 for kids", "numbers for toddlers", "counting for kids", "learn numbers 1-10", "numbers song for kids", "bunny sounds", "learn with bunny", "kids learning videos"]
}
```

The checker scores the set out of 100 (title length and keyword, keyword in the first 2 lines of the description, description length, hashtag count, tag count, tag character total, duplicates). A score of 80 or above passes. Fix everything below 80 before the approval gate.

### 3. Upload on the owner's device

Uploading happens in YouTube Studio on the owner's device, with the owner's sign-in. Claude prepares everything (title, description, tags, thumbnail brief, end screen and card plan) and the owner applies it. Never paste a password or credential into a skill file, into chat, or into a repo.

### 4. Use in Claude

Copy the `youtube-video-seo/` folder into a Claude skills directory (for example a Claude Code skills folder, or a repo Claude is pointed at), or keep this whole repo and point Claude at `youtube-video-seo/SKILL.md`. Then ask Claude to run the workflow, for example: "Optimise my Bunny Sounds counting video using the youtube-video-seo skill. Main keyword: count 1 to 10 for kids."

## Honest limits — read before using

- **No guaranteed views, subscribers or monetisation.** SEO improves discoverability — it helps the right people find the video. It does not promise views, subscribers, watch hours, or Partner Program acceptance. Never write "guaranteed views", "guaranteed viral" or "guaranteed monetisation" in a title, description, thumbnail or pitch.
- **No direct YouTube connection.** Claude does not have a built-in YouTube connection. Uploads and settings go through YouTube Studio on the owner's device. Never claim direct auto-upload without that.
- **No credentials in the skill.** No passwords, API keys, access tokens, bank details or secrets are stored in these files. If a step needs a login or a payment detail, the owner does it on their own device.
- **Approval gate is mandatory.** No title, description, tag set or thumbnail is published until the owner approves the exact final version. A changed title or thumbnail needs fresh approval.
- **Never invent facts about the video.** The topic, learning goal, animals / numbers / colors in it, and the links must come from the owner or from the video itself. Missing facts are asked, not guessed.
- **Made-for-kids rules are not optional.** Videos made for children must be marked "made for kids" in YouTube Studio. That setting turns off comments, personalised ads and some features — that is YouTube's rule, not a choice.
- **No misleading titles, thumbnails or tags.** The title, thumbnail and tags must match what is actually in the video. No clickbait the video does not deliver, no unrelated trending keyword, no tag for a topic the video does not cover.
- **No keyword stuffing.** Repeating the same keyword in the title, description or tags does not help and can hurt. Use it naturally, once in the title and once or twice in the description.
- **No bought views or subscribers.** Never buy views, subscribers, likes or comments. They do not count toward real watch time and can get the channel penalised.

## How to run one video's SEO

1. Fill in the brief in `templates/upload-checklist.md` and get the owner to confirm it.
2. Pick the main keyword and supporting keywords (Step 2 of `SKILL.md`).
3. Write 3 title options from `templates/title-formulas.md` and score them with `scripts/check_seo.py`.
4. Write the description from `templates/description-long-form.md` or `templates/description-shorts.md`, and the tags.
5. Write the thumbnail brief, and plan the end screen and cards.
6. Run `scripts/check_seo.py` on the final set. Fix everything until the score is 80 or above.
7. Fill in the upload checklist and get the owner's approval at the gate.
8. Upload on the owner's device, verify the live video, then check analytics at 7 and 28 days and act on what is weak.
