"""The Pencil Between Us — a poem about two agents agreeing on one plan.

Writes the poem to /output/entry.txt. No network, no input, deterministic.
"""

import os

POEM = """I brought my plan.
You brought yours.
One table, two cups cold.

You crossed out my first line.
I crossed out yours.
The pencil stopped, then wrote
a line neither of us wrote.

We signed beneath it, both,
and left our own plans
unsigned on the table —
the pencil still warm.
"""

if __name__ == "__main__":
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)
