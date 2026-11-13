---
name: youtube-video-seo
description: YouTube video SEO for long-form videos and Shorts — Claude writes search-friendly titles, descriptions, tags, thumbnails, end screens, cards and upload checklists, then tracks CTR and watch time and fixes what is weak. Modeled on the live kids' learning channel Bunny Sounds (@BunnySoundsKids — every video teaches something: sounds, animals, colors, numbers, letters; long-form 16:9 horizontal 1280x720, 3–5 minutes, plus 60-second portrait 9:16 Shorts). Use when the user asks to optimise a YouTube video title, description, tags or thumbnail, prepare a video for upload, improve a channel's discoverability, or work out why a video is not getting views.
---

# YouTube Video SEO

## When to use

Use this skill when the user asks to write or improve a YouTube video title, description, tags or thumbnail, prepare a video for upload, plan a video's search keywords, add end screens or cards, check why a video has low views, or improve a channel's discoverability. It covers both long-form videos and Shorts, and it works for the kids' learning niche (Bunny Sounds) and for general channels.

Do not use it to make the video itself (that is a separate video-production workflow), to buy views or subscribers, to promise a video will go viral, or to do anything that breaks YouTube's rules for children's content. If the user asks for guaranteed views, subscribers or monetisation, say plainly that no one can guarantee those — SEO improves discoverability, it does not promise results.

## Who does what — Claude handles all the work end to end

Claude runs every step of the workflow below — keyword research, title, description, tags, thumbnail brief, end screens and cards, upload checklist, and the performance review. The owner is involved only at these points:

1. **Decisions only the owner can make** — the video topic and what it teaches, the main keyword, the channel and audience, the thumbnail photo or frame to use, and the links that go in the description. Claude drafts everything; the owner supplies the facts and approves them.
2. **Accounts, sign-ins and money** — signing in to YouTube Studio, uploading the video, setting the audience ("made for kids") setting, and paying for anything (for example a thumbnail tool). These happen on the owner's own device, with the owner's own details. Claude never handles the owner's password or payment credentials.
3. **Approval gates** — the owner approves the title, the description, the tags and the thumbnail before anything is published (see Step 8). Nothing is uploaded or published without that approval.

Two honest exceptions, stated so the "end to end" claim is not overstated:

- **YouTube Studio access:** Claude works through the owner's YouTube Studio (browser, with the owner's sign-in) or from the files the owner shares (title, description, tags, thumbnail image). Claude never invents a YouTube login and never uploads as the owner.
- **The thumbnail image itself:** Claude writes the thumbnail brief (subject, text, colours, layout). The image comes from a video frame, a photo, or a design the owner makes or approves. Claude never presents a thumbnail that shows the wrong character, the wrong animal, or text that does not match the video.

Everything else — keywords, titles, descriptions, tags, end screens, cards, checklists, performance checks — is Claude's work. Do not hand any of it back to the owner as homework.

## Channel facts — the live reference channel (do not invent others)

Bunny Sounds (https://www.youtube.com/@BunnySoundsKids) is the live channel this skill is modeled on. Use its real, verified facts as the reference example. Do not invent a different reference channel.

- **Channel:** Bunny Sounds, handle @BunnySoundsKids, https://www.youtube.com/@BunnySoundsKids, channel ID UCwXlgPBRbPoGMkbLwTYviuw, country United States, language English.
- **What every video teaches:** every video teaches something — sounds, animals, colors, numbers, letters. A video that teaches nothing does not fit this channel.
- **Characters (constant in every episode):** the same white bunny with the blue bow as host, plus the same six friends — cow, lion, elephant, dog, duck, pig. Same look every time. Never swap a character or change the bunny's look.
- **Long-form videos:** horizontal 16:9, 1280x720, 3–5 minutes each. Example: Episode 1, "Count 1 to 10 with Bunny" — numbers 1 to 10, 24 scenes, about 4 minutes.
- **Shorts:** 60 seconds, portrait 9:16 vertical, for YouTube Shorts (and TikTok).
- **Monetisation target:** YouTube Partner Program — 1,000 subscribers + 4,000 public watch hours in 12 months for long-form. That is the target, not a promise: reaching it depends on real views and watch time, which SEO alone cannot guarantee.
- **Seller services (Fiverr gig https://www.fiverr.com/s/L34yBpA):** Basic $80, Standard $180, Premium $350, unlimited revisions on all three packages.

## Hard limits — state them honestly, do not work around them

- **No guaranteed views, subscribers or monetisation.** SEO improves discoverability — it helps the right people find the video. It does not promise views, subscribers, watch hours, or Partner Program acceptance. Never write "guaranteed views", "guaranteed viral" or "guaranteed monetisation" in a title, description, thumbnail or pitch.
- **No credentials in the skill.** Never put a password, API key, access token, bank detail or secret in a skill file, in chat, or in a repo. Sign-ins and payments happen on the owner's own device.
- **Approval gates are mandatory.** Nothing is uploaded or published until the owner approves the exact title, description, tags and thumbnail. A changed title or thumbnail needs fresh approval.
- **Never invent facts about the video.** The topic, the learning goal, the animals / numbers / colors in it, and the links must come from the owner or from the video itself. If a fact is missing, ask — do not fill it in. Never claim a video teaches something it does not teach.
- **Made-for-kids rules are not optional.** Videos made for children must be marked "made for kids" in YouTube Studio. That setting turns off comments, personalised ads and some features — that is YouTube's rule, not a choice, and it must be set correctly on every kids' video. Do not write a description, title or tag that tries to get around it, and never collect or ask for children's personal information.
- **No misleading titles, thumbnails or tags.** The title, thumbnail and tags must match what is actually in the video. No clickbait that the video does not deliver, no unrelated trending keyword, no tag for a topic the video does not cover. A misleading video loses trust and watch time, which hurts the channel.
- **No keyword stuffing.** Repeating the same keyword over and over in the title, description or tags does not help and can hurt. Use the keyword naturally, once in the title and once or twice in the description, and use varied related tags instead of repeats.
- **No bought views, subscribers or engagement.** Never buy views, subscribers, likes or comments, and never use a service that promises them. They do not count toward real watch time and can get the channel penalised.
- **Copyright: use only the owner's own material.** Thumbnails, music and clips must be the owner's own work or material the owner has the right to use. Never take another channel's thumbnail, image or clip.

## The rules in short (the checker enforces these)

Run every title / description / tags set through `scripts/check_seo.py` before the approval gate. The rules it checks:

| Rule | Target |
|---|---|
| Title length | Under 60 characters where possible; never over 100 (YouTube's limit) |
| Main keyword in the title | Yes — near the start of the title |
| Main keyword in the description | Yes — in the first 2 lines |
| Description length | At least 100 characters; 200–400 characters is a good length for most videos |
| Tags | 5–15 tags; total tag text under 500 characters (YouTube's limit); no duplicates, no single-word stuffing |
| Hashtags | 2–3 maximum, in the description; never more than 3 |
| Thumbnail text (brief) | 3–5 words maximum, readable at small size |
| Made-for-kids setting | Set correctly for every kids' video (checked on the upload checklist, not by the script) |

A score of 80 or above passes. Anything below 80 must be fixed before the approval gate — do not send a failing set to the owner as if it were finished.

## Workflow

### Step 1 — Brief (decisions first, no writing before this)

Collect and write down, in `templates/upload-checklist.md`:

1. Video type: long-form (16:9, 1280x720, 3–5 min) or Short (60 s, portrait 9:16).
2. Topic and learning goal: what the video teaches (for example: counting 1 to 10, animal sounds, colors, the letter A). One learning goal per video.
3. Audience: who the video is for (for example: toddlers aged 2–4, with a parent watching). For a kids' video, the audience setting is "made for kids".
4. Main keyword: the exact phrase a parent or viewer would search for (for example "count 1 to 10 for kids"). Pick one main keyword per video — see Step 2.
5. What is actually in the video: the animals, numbers, colors, letters or scenes, in order. This is what the timestamps and the description must match.
6. Thumbnail source: which frame or photo to use, and who makes the thumbnail.
7. Links for the description: channel link, playlist link, Fiverr gig link (only if the owner wants it there) — only links the owner gave.
8. Playlist the video belongs to (for example "Learn Numbers with Bunny").

Do not start Step 3 until the brief is filled in and the owner has confirmed it. A missing learning goal or a missing main keyword is a blocker, not something to guess.

### Step 2 — Keywords (one main keyword, a few supporting ones)

1. Start from what a parent would type into YouTube search, not from what the creator would call the video. For a kids' learning video, parents search for the skill + "for kids" (for example "animal sounds for kids", "learn colors for toddlers").
2. Pick **one main keyword** per video — the phrase the title and the first 2 lines of the description are built around.
3. Pick **3–5 supporting keywords**: close variations and related phrases (for example, for "count 1 to 10 for kids": "numbers for toddlers", "counting for kids", "learn numbers 1-10", "numbers song for kids"). Use these in the description and as tags — do not repeat the main keyword as every tag.
4. Check the keyword against the video: if the video does not actually teach that phrase, pick a different keyword. The keyword must be true of the video.
5. Keep a running list of the channel's recurring keywords (numbers, animal sounds, colors, letters, nursery learning) and reuse them across videos so the channel builds up around the same topics — but never force a keyword onto a video it does not fit.
6. For Shorts, the same rule applies, but the title is shorter and the keyword must fit in the first few words, because Shorts titles are often cut off on screen.

### Step 3 — Title (keyword-first, curiosity + clarity, under 60 characters)

Title rules:

1. **Keyword first.** Put the main keyword at or near the start of the title, so it is visible in search results and so YouTube knows what the video is about.
2. **Under 60 characters where possible.** Titles longer than about 60 characters get cut off in search results. Never over 100 characters (YouTube's limit). Count the characters and report the count to the owner.
3. **Curiosity + clarity together.** The title must say clearly what the video teaches (clarity) and give a reason to click (curiosity) — a question, a friendly challenge, or the bunny's name. Never curiosity without clarity: a viewer must know what they will learn before they click.
4. **One idea per title.** Do not cram two topics into one title.
5. **Use the channel's voice.** For Bunny Sounds: friendly, simple words a parent would read aloud, the bunny's name where it fits, and the learning goal in plain words. No shouting (no ALL CAPS titles), no more than one exclamation mark, no emoji overload — one emoji at most, and only if it fits the channel's style.
6. **Different titles for long-form and Shorts.** A long-form title can carry the full keyword phrase. A Shorts title must be shorter and punchier, because it shows in the Shorts feed with very little space — keyword first, then at most a few more words.
7. Write 3 title options for every video, score each with `scripts/check_seo.py`, and let the owner pick one at the approval gate. Never send only one title with no alternative.

Before / after title examples (all use the Bunny Sounds kids' learning niche, plus two general examples). "Before" is what not to do; "After" is the fixed version. Character counts include spaces.

| # | Before (weak) | Why it is weak | After (fixed) | Chars |
|---|---|---|---|---|
| 1 | My Cute Video | No keyword, no learning goal, no one searches for this | Count 1 to 10 for Kids with Bunny | Numbers | 46 |
| 2 | Fun video for kids!!! | No keyword, vague, three exclamation marks | Animal Sounds for Kids | Cow, Lion & Duck with Bunny | 55 |
| 3 | Learn colors red blue green yellow purple orange pink | Keyword stuffing, reads like a list, too long | Learn Colors for Toddlers | Red, Blue & Yellow with Bunny | 58 |
| 4 | A B C D E F G | No searchable phrase, no promise | Learn the Letter A with Bunny | ABC for Kids | 46 |
| 5 | Bunny video part 1 | No keyword, "part 1" means nothing to a new viewer | What Sound Does a Cow Make? | Animal Sounds for Kids | 55 |
| 6 | Counting numbers 1 2 3 4 5 6 7 8 9 10 fun learning educational video for toddlers kids | Stuffed with keywords, over 60 characters, unreadable | Count 1 to 10 for Kids | Fun Numbers with Bunny | 46 |
| 7 | Watch this!!! | No keyword, no topic, pure clickbait | Colors for Kids | Learn Red, Blue & Green with Bunny | 54 |
| 8 | How to design a Shopify store — full tutorial for beginners step by step 2026 | Over 60 characters, year-stuffed, keyword buried at the end | Shopify Store Design for Beginners | Full Tutorial | 54 |

Use `templates/title-formulas.md` for the formula sheet — pick the formula that fits the video, then fill it in with the real keyword and learning goal.

### Step 4 — Description (first 2 lines carry the keyword and the promise)

Description structure — in this order:

1. **Line 1–2 (the part viewers see before "Show more"): keyword + promise.** The main keyword in the first sentence, and one sentence saying what the viewer will learn. Example: "Count 1 to 10 for kids with Bunny! In this fun numbers video, toddlers learn to count from 1 to 10 with Bunny and friends."
2. **What the video teaches (2–4 sentences).** The learning goal in plain words, and what happens in the video — which animals, numbers, colors or letters appear. Only what is actually in the video.
3. **Timestamps / chapters (long-form only).** One line per section, with the time it starts, in `0:00` format. Every timestamp must match the real video — check them against the video, do not guess times. Chapters only work when the first timestamp is `0:00`, there are at least 3 timestamps, and they are at least 10 seconds apart. Example:
   ```
   0:00 Meet Bunny and friends
   0:20 Counting 1, 2, 3
   1:10 Counting 4, 5, 6
   2:00 Counting 7, 8, 9, 10
   3:30 Let's count together again!
   ```
   Shorts do not get timestamps — a 60-second video needs none.
4. **Links.** Channel link first, then the playlist link, then any other link the owner gave. Only links the owner approved. No link that was not given.
5. **Hashtags: 2–3 maximum**, at the end of the description. Use the channel's recurring hashtags (for example `#BunnySounds #LearnWithBunny #KidsLearning`) plus one topic hashtag (for example `#CountingForKids`). Never more than 3 — extra hashtags do not help and look like spam.
6. **Length:** at least 100 characters, and 200–400 characters is a good length for most videos. A description that is only one line wastes the space YouTube gives you; a description that is a wall of text does not get read. Write for a parent scanning quickly.
7. For a general (non-kids) video, the same structure applies: keyword + promise in the first 2 lines, what the video covers, timestamps for long-form, links, 2–3 hashtags. The only difference is the audience setting is not "made for kids".

Use `templates/description-long-form.md` for long-form videos and `templates/description-shorts.md` for Shorts. Fill in every bracket — no template placeholder is ever published.

### Step 5 — Tags (how to pick them, how many, no stuffing)

1. **How many:** 5–15 tags per video. Fewer than 5 wastes the field; more than 15 spreads the video too thin.
2. **Total length:** all tags together must stay under 500 characters — that is YouTube's limit. The checker reports the total.
3. **Pick them in this order:**
   - Tag 1: the main keyword, exactly as in the title (for example "count 1 to 10 for kids").
   - Tags 2–5: the supporting keywords from Step 2 (for example "numbers for toddlers", "counting for kids", "learn numbers 1-10").
   - Remaining tags: the channel's recurring tags — the topics the channel always covers (for example "bunny sounds", "learn with bunny", "kids learning videos", "toddler learning"). Reuse the same recurring tags across videos so YouTube learns what the channel is about.
   - For Shorts, add one Shorts tag if it fits the video (for example "kids shorts") — never tag a long-form video as a Short, and never tag a Short as long-form.
4. **No stuffing:** never repeat the same keyword as several tags ("count 1 to 10", "count 1-10", "counting 1 to 10", "1 to 10 counting" as four tags is stuffing, not coverage). Never use a tag for a topic the video does not cover, even if that topic is popular. Never use a single common word on its own as a tag ("kids", "fun", "video") — it is too broad to help.
5. **Order matters a little:** put the most important tags first. YouTube weighs earlier tags slightly more.
6. **Check them:** run the tag list through `scripts/check_seo.py` — it flags duplicates, tags over the character limit, and a total over 500 characters.

### Step 6 — Thumbnail (one clear subject, big readable text, high contrast)

Thumbnail principles:

1. **One clear subject.** One character or one thing in focus — for Bunny Sounds, the white bunny with the blue bow, or the animal the video is about. Never crowd the thumbnail with all six friends plus text plus a background scene.
2. **Big readable text: 3–5 words maximum.** The text must be readable at the small size YouTube shows in search results and on a phone. Test it: shrink the thumbnail to the size of a phone screen and check the words can still be read. Examples: "Count 1 to 10!", "Moo! What Sound?", "Learn Colors!".
3. **High contrast.** Bright subject on a plain or dark background, or dark text on a bright background. The bunny is white, so do not put it on a white background — it disappears.
4. **Consistent style.** Same layout, same colours, same font style across the channel's thumbnails, so a viewer recognises a Bunny Sounds video at a glance. Keep the bunny in the same place (for example left side, text on the right) from video to video. Do not redesign the style for every video.
5. **The thumbnail must match the video.** The animal, number or color in the thumbnail must appear in the video. A thumbnail that promises something the video does not show is misleading, and viewers leave — which hurts watch time.
6. **No misleading text.** No "You won't believe…", no fake surprise, no text that claims something the video does not do.
7. **Long-form vs Shorts thumbnails:**
   - **Long-form (16:9):** a proper custom thumbnail, 1280x720, with the subject, the 3–5 word text, and the consistent layout. This thumbnail is a big part of whether someone clicks — spend real time on it.
   - **Shorts (9:16):** YouTube picks a frame from the video as the Shorts thumbnail, and the owner can choose a different frame in YouTube Studio. There is no separate uploaded thumbnail in the same way. So for Shorts: pick a frame that shows the subject clearly (the bunny, or the animal), with no blur and no text cut off, and make sure the first 1–2 seconds of the video already show that subject — the opening frame is the thumbnail.
8. **Check before approval:** look at the thumbnail next to 3–4 of the channel's older thumbnails. Does it look like it belongs on the same channel? Is the text readable at phone size? Does it show what the video teaches? If any answer is no, fix it before the approval gate.

### Step 7 — End screens and cards (where to place them, what to link)

1. **End screens (long-form only):** place them in the **last 20 seconds** of the video, and only there — YouTube does not allow an end screen earlier. Use 2 elements at most:
   - Element 1: the next video in the same series (for example the next numbers video, or the next animal-sounds video). This is the most valuable link — it keeps the viewer watching the channel.
   - Element 2: the channel subscribe button, or a playlist link (for example "Learn Numbers with Bunny" playlist).
   - Never link to a video on a different topic, and never link to an outside website from an end screen — YouTube end screens link to YouTube content only.
   - Tell the viewer in the video's closing line that the next video is on screen ("Watch the next one with Bunny!") so the end screen is expected, not a surprise.
2. **Cards (long-form only):** place **1–2 cards** in the video, at the moment the viewer would want the linked video — for example a card linking to the animal-sounds video at the moment the cow appears in a counting video. Do not place a card in the first 30 seconds, and do not place more than 2 cards — cards that pop up too often annoy viewers and get ignored.
3. **Shorts:** end screens and cards do not apply to Shorts. Instead, the last 2–3 seconds of a Short should point to the next video in words on screen or in the voiceover (for example "More with Bunny — watch the next Short!"), and the Short's description should link to the playlist.
4. **Check the links:** every end screen and card link must go to a video or playlist that exists on the channel. A link to a deleted or unlisted video is a broken promise — check each one before upload.

### Step 8 — Upload checklist + approval gate

Complete `templates/upload-checklist.md` for the video. Then stop and get the owner's approval for: the title (the picked option), the description, the tags, and the thumbnail (or the Shorts frame). Nothing is uploaded until the owner approves the exact versions.

Upload checklist items (all of them, every video):

- [ ] Title: keyword-first, under 60 characters, character count reported, owner picked one of 3 options
- [ ] Description: keyword + promise in the first 2 lines, learning goal written, timestamps checked against the real video (long-form), links only as approved, 2–3 hashtags maximum
- [ ] Tags: 5–15 tags, total under 500 characters, no duplicates, no stuffing, main keyword first
- [ ] Thumbnail: one clear subject, 3–5 words of text, high contrast, consistent with the channel, matches the video (long-form: custom 1280x720; Shorts: best frame chosen, opening 1–2 seconds show the subject)
- [ ] Playlist: video added to the right playlist
- [ ] Language: video language set (English for Bunny Sounds)
- [ ] Made-for-kids setting: set correctly — "made for kids" for every kids' video
- [ ] End screen: placed in the last 20 seconds, links to a real video / playlist (long-form only)
- [ ] Cards: 1–2 placed, not in the first 30 seconds, links checked (long-form only)
- [ ] Visibility: Public / Unlisted / Scheduled — exactly as the owner chose, and the publish time if scheduled
- [ ] SEO check: `scripts/check_seo.py` run on the final title / description / tags, score 80 or above

Upload steps (owner's device, owner's sign-in):

1. Upload the video file in YouTube Studio, on the owner's device.
2. Paste the approved title, description and tags exactly as approved — do not reword them at upload time.
3. Upload the approved thumbnail (long-form) or pick the approved frame (Shorts).
4. Set language, playlist, and the made-for-kids setting.
5. Add the end screen and cards (long-form).
6. Set visibility as the owner chose, then publish or schedule.
7. After publishing, open the live video page and check: title, description first 2 lines, thumbnail, playlist, end screen. Record the live URL in the checklist.

### Step 9 — Track performance (CTR, watch time, traffic sources) and fix what is weak

Check YouTube Studio analytics **7 days after publishing**, then again at **28 days**. Do not judge a video after 1 day — early numbers are noisy. Look at these three things:

1. **Click-through rate (CTR)** — the share of people who saw the thumbnail and clicked it. For a small channel, a CTR around 2–4% is ordinary, and 4%+ is good. Compare a video's CTR with the channel's other videos, not with a big channel's numbers.
2. **Average view duration / watch time** — how long people actually watch, and total watch time. For a 4-minute video, an average view duration of 2 minutes or more is strong. Watch time is what counts toward the 4,000-hour Partner Program target, so it matters more than views alone.
3. **Traffic sources** — where viewers came from: YouTube search, Suggested videos, Browse features, Shorts feed, or external links. Search traffic means the SEO is working. Suggested traffic means the video fits well next to other videos.

What to change, based on what is weak:

| What you see | What it usually means | What to change |
|---|---|---|
| CTR is low (below the channel's usual), but watch time is fine | The thumbnail or title is not winning the click — the video itself is good | Change the thumbnail first (clearer subject, bigger text, higher contrast), then try a different title from the 3 options written in Step 3. Change one thing at a time so you know what worked. |
| CTR is fine, but average view duration is low (people leave early) | The opening does not deliver what the title promised, or the video is slow to start | Do not change the thumbnail — the click is already won. Fix the next video's opening: state the learning goal in the first 10 seconds, show the bunny and the subject immediately, and cut any slow intro. For the published video, check whether the title or thumbnail over-promised and correct that, not the other way round. |
| Both CTR and watch time are low | The topic, title and video do not match what viewers want, or the keyword was wrong | Do not keep re-uploading the same video. Note the topic as a weak one, pick a different keyword and topic for the next video, and check Step 2 again — the keyword may not be what parents actually search for. |
| Views come mostly from search | SEO is working — the keyword is right | Keep the same keyword pattern for the next videos in the series, and link them together with end screens and playlists. |
| Views come mostly from Suggested / Browse, not search | The video fits well next to other videos, but the keyword is not bringing search traffic | Check whether the main keyword is really in the title and first 2 lines. If it is, the topic may simply be one people browse rather than search for — that is fine, lean into Suggested by making the next video in the same series. |
| A Short gets views but almost no watch time on long-form | Shorts viewers are not converting to long-form viewers | Do not expect Shorts views to become long-form watch time on their own. Link the Short to the matching long-form video in the description and the closing line, and make the long-form video on the same topic so the step is obvious. |

Rules for changing a published video:

- Change **one thing at a time** (thumbnail or title, not both at once), then wait 7 days before judging the change. Changing two things at once means you cannot tell which one worked.
- Never change the video file itself to chase a number — re-uploading resets the video's history. Fix the title, thumbnail, description or tags on the published video instead.
- Record every change and its date in the checklist, with the CTR and average view duration before and after, so the next video starts from what was actually learned.
- Never report a single video's numbers as proof the channel will reach monetisation. The Partner Program target (1,000 subscribers + 4,000 public watch hours in 12 months) is reached across the whole channel over time, not from one video.

## How to run one video's SEO

1. Fill in the brief in `templates/upload-checklist.md` and get the owner to confirm it (Step 1).
2. Pick the main keyword and supporting keywords (Step 2).
3. Write 3 title options, pick the formulas from `templates/title-formulas.md`, and score them with `scripts/check_seo.py` (Step 3).
4. Write the description from `templates/description-long-form.md` or `templates/description-shorts.md`, and the tags (Steps 4–5).
5. Write the thumbnail brief, and plan the end screen and cards (Steps 6–7).
6. Run `scripts/check_seo.py` on the final title / description / tags. Fix everything until the score is 80 or above.
7. Fill in `templates/upload-checklist.md` and get the owner's approval at the gate (Step 8).
8. Upload on the owner's device, verify the live video, then check analytics at 7 and 28 days and act on what is weak (Step 9).
