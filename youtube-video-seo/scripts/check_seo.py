#!/usr/bin/env python3
"""check_seo.py — score a YouTube title / description / tags set against
the rules in the youtube-video-seo skill.

Part of the youtube-video-seo Claude skill.
See youtube-video-seo/SKILL.md, "The rules in short", for the full rules.

What it checks (and how it scores, out of 100):
  Title (40 points):
    - 15 pts: under 60 characters (10 pts if 60-100, 0 if over 100)
    - 15 pts: main keyword appears in the title
    - 10 pts: main keyword is in the first half of the title
  Description (30 points):
    - 10 pts: main keyword appears in the first 2 lines
    - 10 pts: at least 100 characters long (5 pts if 50-99)
    - 10 pts: 2-3 hashtags, and no more than 3 (0 if 4 or more)
  Tags (30 points):
    - 10 pts: between 5 and 15 tags
    - 10 pts: total tag text under 500 characters (YouTube's limit)
    - 10 pts: no duplicate tags (case-insensitive) and no tag repeated
      as a near-duplicate of the main keyword

  A score of 80 or above passes. Fix everything below 80 before the
  approval gate — do not send a failing set to the owner as finished.

Input: a JSON file with these fields:
  {
    "title": "Count 1 to 10 with Bunny | Numbers for Kids",
    "keyword": "count 1 to 10 for kids",
    "description": "Count 1 to 10 with Bunny! ...",
    "tags": ["count 1 to 10 for kids", "numbers for toddlers", "..."]
  }
  "keyword" is required. "description" and "tags" may be empty, but
  they will score 0 for the checks that need them.

Prints PASS (score >= 80) or FAIL with one line per problem, and exits
0 on PASS, 1 on FAIL. Exits 2 on a usage or input error.

Usage:
  python3 check_seo.py <seo.json>

  Example:
    python3 check_seo.py ../templates/seo-example.json

Requirements: Python 3, standard library only. No credentials, no network.
"""

import json
import re
import sys

PASS_SCORE = 80
TITLE_TARGET = 60
TITLE_LIMIT = 100
DESCRIPTION_MIN = 100
TAGS_MIN = 5
TAGS_MAX = 15
TAGS_CHAR_LIMIT = 500
HASHTAG_MAX = 3


def first_two_lines(text):
    """Return the first two non-empty lines of a description."""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines[:2])


def count_hashtags(text):
    """Return the hashtags found in the text (e.g. #BunnySounds)."""
    return re.findall(r"#\w+", text)


def normalise(text):
    """Lowercase, collapse whitespace, strip punctuation at the ends."""
    return re.sub(r"\s+", " ", text.strip().lower())


def check(data):
    """Score the SEO set in data. Returns (score, problems) where problems
    is a list of strings, one per failed check."""
    problems = []
    score = 0

    title = (data.get("title") or "").strip()
    keyword = (data.get("keyword") or "").strip()
    description = (data.get("description") or "").strip()
    tags = data.get("tags") or []
    tags = [str(tag).strip() for tag in tags if str(tag).strip()]

    if not keyword:
        return 0, ["No main keyword given: the 'keyword' field is empty."]

    keyword_norm = normalise(keyword)

    # --- Title: length (15 points) ---
    if not title:
        problems.append("Title is empty.")
    elif len(title) <= TITLE_TARGET:
        score += 15
    elif len(title) <= TITLE_LIMIT:
        score += 10
        problems.append(
            "Title is %d characters — over the %d-character target "
            "(YouTube limit is %d). Shorten it."
            % (len(title), TITLE_TARGET, TITLE_LIMIT)
        )
    else:
        problems.append(
            "Title is %d characters — over YouTube's %d-character limit. "
            "Shorten it." % (len(title), TITLE_LIMIT)
        )

    # --- Title: keyword present (15) and near the start (10) ---
    if title:
        title_norm = normalise(title)
        if keyword_norm in title_norm:
            score += 15
            # "Near the start" means the keyword begins in the first half
            # of the title. (Checking that the whole keyword fits inside
            # the first half would be impossible for a short title with
            # a long keyword, e.g. a 24-character keyword in a 43-character
            # title, so the start position is the right test.)
            if title_norm.find(keyword_norm) < len(title_norm) // 2:
                score += 10
            else:
                problems.append(
                    "Main keyword %r is in the title but does not start "
                    "near the front — move it toward the front." % keyword
                )
        else:
            problems.append(
                "Main keyword %r does not appear in the title." % keyword
            )

    # --- Description: keyword in first 2 lines (10) ---
    if not description:
        problems.append("Description is empty.")
    else:
        opening = normalise(first_two_lines(description))
        if keyword_norm in opening:
            score += 10
        else:
            problems.append(
                "Main keyword %r does not appear in the first 2 lines of "
                "the description." % keyword
            )

    # --- Description: length (10) ---
    if description:
        if len(description) >= DESCRIPTION_MIN:
            score += 10
        elif len(description) >= 50:
            score += 5
            problems.append(
                "Description is %d characters — under the %d-character "
                "minimum. Add what the video teaches."
                % (len(description), DESCRIPTION_MIN)
            )
        else:
            problems.append(
                "Description is %d characters — under the %d-character "
                "minimum. Add what the video teaches."
                % (len(description), DESCRIPTION_MIN)
            )

    # --- Description: hashtags (10) ---
    if description:
        hashtags = count_hashtags(description)
        if 1 <= len(hashtags) <= HASHTAG_MAX:
            score += 10
        elif not hashtags:
            problems.append(
                "No hashtags in the description — add 2-3 (for example "
                "the channel hashtag plus one topic hashtag)."
            )
        else:
            problems.append(
                "%d hashtags in the description — maximum is %d. Remove "
                "the extras." % (len(hashtags), HASHTAG_MAX)
            )

    # --- Tags: count (10) ---
    if TAGS_MIN <= len(tags) <= TAGS_MAX:
        score += 10
    elif not tags:
        problems.append("No tags given — add %d-%d tags." % (TAGS_MIN, TAGS_MAX))
    else:
        problems.append(
            "%d tags given — use between %d and %d tags."
            % (len(tags), TAGS_MIN, TAGS_MAX)
        )

    # --- Tags: total characters (10) ---
    total_chars = sum(len(tag) for tag in tags)
    if tags and total_chars <= TAGS_CHAR_LIMIT:
        score += 10
    elif tags:
        problems.append(
            "Tags total %d characters — YouTube's limit is %d. Remove or "
            "shorten tags." % (total_chars, TAGS_CHAR_LIMIT)
        )

    # --- Tags: duplicates and keyword repeats (10) ---
    if tags:
        seen = {}
        duplicates = []
        for tag in tags:
            key = normalise(tag)
            if key in seen:
                duplicates.append(tag)
            else:
                seen[key] = True
        keyword_variants = [
            tag
            for tag in tags
            if normalise(tag) != keyword_norm
            and keyword_norm in normalise(tag)
        ]
        if duplicates:
            problems.append(
                "Duplicate tags: %s." % ", ".join(sorted(set(duplicates)))
            )
        elif keyword_variants:
            problems.append(
                "Tags repeat the main keyword as near-duplicates: %s. "
                "Use varied supporting keywords instead."
                % ", ".join(keyword_variants)
            )
        else:
            score += 10

    return score, problems


def main(argv):
    if len(argv) != 2:
        print("Usage: %s <seo.json>" % argv[0], file=sys.stderr)
        return 2

    path = argv[1]
    try:
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError:
        print("File not found: %s" % path, file=sys.stderr)
        return 2
    except (OSError, json.JSONDecodeError) as exc:
        print("Could not read %s: %s" % (path, exc), file=sys.stderr)
        return 2

    if not isinstance(data, dict):
        print("Input must be a JSON object with title, keyword, "
              "description and tags.", file=sys.stderr)
        return 2

    score, problems = check(data)

    title = (data.get("title") or "").strip()
    description = (data.get("description") or "").strip()
    tags = [t for t in (data.get("tags") or []) if str(t).strip()]
    print("Title: %d characters" % len(title))
    print("Description: %d characters, %d hashtag(s)"
          % (len(description), len(count_hashtags(description))))
    print("Tags: %d tag(s), %d characters total"
          % (len(tags), sum(len(str(t)) for t in tags)))
    print("Score: %d/100" % score)

    if score >= PASS_SCORE and not problems:
        print("PASS: this title / description / tags set is ready for "
              "the approval gate.")
        return 0

    print("FAIL: %d problem(s) in %s" % (len(problems), path))
    for problem in problems:
        print("  - %s" % problem)
    if score >= PASS_SCORE:
        print("Score is %d, but every problem above must still be fixed."
              % score)
    else:
        print("Fix every problem above, then run the checker again.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
