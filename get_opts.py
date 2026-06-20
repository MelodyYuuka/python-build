import sys
from packaging import version

now = version.parse(sys.argv[1])

if now >= version.parse("3.14"):
    print("--enable-optimizations --with-lto --enable-bolt --enable-experimental-jit=yes-off --with-tail-call-interp", end="")
elif now >= version.parse("3.13"):
    print("--enable-optimizations --with-lto --enable-bolt --enable-experimental-jit=yes-off", end="")
elif now >= version.parse("3.12"):
    print("--enable-optimizations --with-lto --enable-bolt", end="")
else:
    print("--enable-optimizations --with-lto", end="")
