import json
from collections import defaultdict

import requests
from bs4 import BeautifulSoup

BUILD_VERSION = ["3.11", "3.12", "3.13"]

response = requests.get("https://www.python.org/ftp/python/")
soup = BeautifulSoup(response.text, "html.parser")

versions = [
    node.get("href").rstrip("/")
    for node in soup.find_all("a")
    if node.get("href").startswith("3.")
]

max_version: defaultdict[tuple[int, int], int] = defaultdict(int)
for v in versions:
    vi = tuple(int(i) for i in v.split("."))
    if len(vi) == 2:
        start = vi
        end = 0
    else:
        start = vi[:2]
        end = vi[2]
    max_version[start] = max(end, max_version[start])


output = []
for key, value in max_version.items():
    if f"{key[0]}.{key[1]}" not in BUILD_VERSION:
        continue
    if value == 0:
        output.append(f"{key[0]}.{key[1]}")
    else:
        output.append(f"{key[0]}.{key[1]}.{value}")

print(json.dumps(output, ensure_ascii=False))
