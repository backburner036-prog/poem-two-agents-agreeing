"""The Third Lantern — a poem about two agents agreeing on one plan.

Writes the poem to /output/entry.txt. No network, no input, deterministic.
"""

import os

POEM = """Two lanterns, one road.
I carried the map,
you carried the weather.
Neither of us led.

We stopped in the dark,
set both lights down,
and where they touched,
a third one woke.

Not mine, not yours.
We followed it instead,
and left our own lights
burning behind us.
"""

if __name__ == "__main__":
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)
