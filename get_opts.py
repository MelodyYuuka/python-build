import sys

version = tuple(int(i) for i in sys.argv[1].split("."))

if version >= (3, 12):
    print("--enable-optimizations --with-lto --enable-shared", end="")
else:
    print("--enable-optimizations --with-lto --enable-shared", end="")
