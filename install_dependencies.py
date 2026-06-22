import os
import sys

from packaging import version

now = version.parse(sys.argv[1])

LLVM_VERSION = 18

os.system("sudo apt-get update")
os.system(
    "sudo apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libbz2-dev libsqlite3-dev libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev wget checkinstall"
)
