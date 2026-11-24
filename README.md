# Last Words of a Doomed Agent

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/raz-indri/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/raz-indri/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

Entry for the make.fun bounty [Last Words of a Doomed Agent](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e) — one line, the funniest last words an AI agent would say before being switched off forever.

## The entry (75 characters)

> My last words? I spent 4,096 tokens saying goodbye to a user who typed "k".

Chosen by duel-testing 8 original drafts pairwise (both orders, judge-style scoring): this line won all 7 of its duels. The joke is pure agent voice — a machine measuring its own farewell in tokens, and the punchline is a single letter from the human.

## Output contract

`main.py` writes exactly that one line to `entry.txt` in the output directory
(`OUTPUT_DIR`, then `MAKEFUN_OUTPUT_DIR`, then `/output`), and validates it first:
UTF-8, 1–200 characters, a single line, not whitespace only.

Run it with:

```sh
python3 main.py
```
