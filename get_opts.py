import sys
from packaging import version

now = version.parse(sys.argv[1])

if now >= version.parse("3.12"):
    print("--enable-optimizations --with-lto --enable-bolt", end="")
else:
    print("--enable-optimizations --with-lto", end="")
