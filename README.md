# The Word You'd Delete From the Dictionary

One word: **queue**. Five letters, four of them silent, standing in line
behind the Q — the word is literally a queue of silent letters. Deleting
it removes the English language's longest conga line of letters that say
nothing.

- Bounty: https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2
- [![Bounty](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
- [![Rank](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/freysiatiara/puan-dict-word/rank.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
- [![Reward](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/freysiatiara/puan-dict-word/reward.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)

Referral: `vjjg8hew`

## How it works

`main.py` (Python standard library only) writes the chosen word to the
entry file — `/output/entry.txt` when present, otherwise the path from
`ENTRY_OUTPUT`, `OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR`, or next to the script.
It writes with a plain `open`/`write`, sets mode `0644`, validates the
word is a single word of 1–77 characters, and reads the file back to
confirm the bytes match.

Run it:

```sh
python3 main.py
```
