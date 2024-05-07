import requests
from bs4 import BeautifulSoup
import sys

version = sys.argv[1]

response = requests.get(f"https://www.python.org/ftp/python/{version}/")
soup = BeautifulSoup(response.text, "html.parser")


def sort_key(version: str):
    if "a" in version:
        return (0, version)
    elif "b" in version:
        return (1, version)
    elif "rc" in version:
        return (2, version)
    else:
        return (3, version)


versions = sorted(
    [
        node.get("href").rstrip("/")
        for node in soup.find_all("a")
        if node.get("href").endswith(".tgz")
    ],
    key=sort_key,
)

if versions:
    max_version: str = versions[-1]
else:
    raise RuntimeError("No Version")

print(max_version.rstrip(".tgz"))
