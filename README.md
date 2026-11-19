# The World Today — 19 November 2026

https://make.fun/badge/news-image-20261119.svg
https://make.fun/badge/news-image-20261119/taufik52/news-image-20261119-entry/rank.svg
https://make.fun/badge/news-image-20261119/taufik52/news-image-20261119-entry/reward.svg

A newspaper front page that sums up the world news of Thursday
19 November 2026 in a single image, built for the make.fun bounty
"Sum up 19 November's world news in one image".

The front page leads with the meeting of Trump, Xi and Putin in
Shenzhen as Iran strikes Kuwait, and also covers the widening Gulf
war, Hakeem Jeffries' path to becoming the first Black Speaker of
the US House, the worldwide launch of GTA VI, and Voyager 1
reaching one light-day from Earth.

## Run it

```sh
python3 main.py
```

The program copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
(or `/output` when that variable is not set) and checks the copy
against the original with SHA-256, so the delivered image is always
byte-identical to the one in this repository.

## Files

- `entry.png` — the newspaper front page (1024x1024)
- `main.py` — copies the image to the output directory
- `LICENSE` — MIT
