"""The World Today -- 19 November 2026.

A single-image newspaper front page summing up the world news of
Thursday 19 November 2026, produced for the make.fun competition
"Sum up 19 November's world news in one image".

Headline story: TRUMP, XI AND PUTIN MEET IN SHENZHEN AS IRAN STRIKES
KUWAIT -- the three leaders gather in Shenzhen while the Gulf war
widens: Iran hits Kuwait and Bahrain after the United States struck
Qeshm island.

Also on the page:
- Hakeem Jeffries is set to become the first Black Speaker of the
  United States House, riding the Democrats' largest Senate gains in
  roughly seventy years.
- Grand Theft Auto VI launches worldwide.
- Voyager 1 reaches one light-day from Earth, the farthest any
  human-made object has ever travelled.

Ticker: Cyclone Akvan; Nvidia halts H-series chip shipments to China;
the European Union approves a 45 billion euro loan for Ukraine; the
Federal Reserve; Russia accuses France; Australia imposes sanctions.

The picture itself lives in entry.png next to this file. Running this
program copies that picture to the output directory so the competition
harness can collect it.
"""

import os
import shutil
import sys
from pathlib import Path


def entry_image_path() -> Path:
    """Return the path of the front page shipped with this entry."""
    return Path(__file__).resolve().parent / "entry.png"


def output_directory() -> Path:
    """Return where the entry image should be written.

    Honours MAKEFUN_OUTPUT_DIR and falls back to /output, the
    directory the make.fun harness mounts for collected entries.
    """
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(chosen)


def deliver() -> Path:
    """Copy entry.png into the output directory and return its path."""
    source = entry_image_path()
    if not source.is_file():
        print(f"entry image missing: {source}", file=sys.stderr)
        raise SystemExit(1)

    target_dir = output_directory()
    target_dir.mkdir(parents=True, exist_ok=True)

    target = target_dir / "entry.png"
    shutil.copyfile(source, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return target


if __name__ == "__main__":
    deliver()
