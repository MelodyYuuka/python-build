import sys
from packaging.version import Version

v = Version(sys.argv[1])

flags = [
    "--enable-optimizations",
    "--with-lto",
    *(["--enable-bolt"] if v >= Version("3.12") else []),
    *(["--enable-experimental-jit=off"] if v >= Version("3.13") else []),
    *(["--with-tail-call-interp"] if v >= Version("3.14") else []),
]

print(*flags)
