import sys

version = tuple(sys.argv[1].split("."))

if version >= (3, 12):
    print("--enable-optimizations --with-lto --enable-bolt")
else:
    print("--enable-optimizations --with-lto")
