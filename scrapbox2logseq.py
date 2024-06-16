import json
import re
import sys
from datetime import datetime

with open(sys.argv[1], 'r', encoding="utf-8") as f:
    data = json.load(f)

pages = {}
for p in data["pages"]:
    d = datetime.fromtimestamp(p["updated"])

    formatted_date = d.strftime("%Y_%m_%d")

    if formatted_date in pages:
        pages[formatted_date] += "\n".join(p["lines"])
    else:
        pages[formatted_date] = "\n".join(p["lines"])


for i,v in pages.items():
    with open( f"{i}.md", "w", encoding="utf-8") as f:
        print( v, file = f)
