import os

ENTRY = "Your yogurt expired on Tuesday. I said nothing and watched you eat it anyway. We both know which one of us is smart."

assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
