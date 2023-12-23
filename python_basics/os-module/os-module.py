import os
if (not os.path.exists("data")):
    os.mkdir("data")

# OS Module is super helpful for doing bulk actions in case of creation, renaming of different modules.
# Method for creating multiple folders.

# for i in range(0, 100):
#     os.mkdir(f"data/day{i+1}")
#     os.mkdir

# Method for renaming multiple folders.
for i in range(0, 100):
    os.rename(f"data/Tutorial{i+1}", f"data/Tutorial_{i+1}")

