import os
import sys

from packaging import version

now = version.parse(sys.argv[1])

LLVM_VERSION = 18

os.system("sudo apt-get update")
os.system(
    "sudo apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libbz2-dev libsqlite3-dev libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev wget checkinstall"
)


if now >= version.parse("3.12"):
    os.system(
        f'echo "deb http://apt.llvm.org/jammy/ llvm-toolchain-jammy-{LLVM_VERSION} main" | sudo tee -a /etc/apt/sources.list > /dev/null'
    )
    os.system(
        f'echo "deb-src http://apt.llvm.org/jammy/ llvm-toolchain-jammy-{LLVM_VERSION} main" | sudo tee -a /etc/apt/sources.list > /dev/null'
    )
    os.system(
        "wget -qO - https://apt.llvm.org/llvm-snapshot.gpg.key | sudo apt-key add -"
    )
    os.system("sudo apt-get update")
    os.system(
        f"sudo apt-get install -y libllvm-{LLVM_VERSION}-ocaml-dev libllvm{LLVM_VERSION} llvm-{LLVM_VERSION} llvm-{LLVM_VERSION}-dev llvm-{LLVM_VERSION}-doc llvm-{LLVM_VERSION}-examples llvm-{LLVM_VERSION}-runtime"
    )
    os.system(
        f"sudo apt-get install -y clang-{LLVM_VERSION} clang-tools-{LLVM_VERSION} clang-{LLVM_VERSION}-doc libclang-common-{LLVM_VERSION}-dev libclang-{LLVM_VERSION}-dev libclang1-{LLVM_VERSION} clang-format-{LLVM_VERSION} python3-clang-{LLVM_VERSION} clangd-{LLVM_VERSION} clang-tidy-{LLVM_VERSION}"
    )
    os.system(f"sudo apt-get install -y libclang-rt-{LLVM_VERSION}-dev")
    os.system(f"sudo apt-get install -y libbolt-{LLVM_VERSION}-dev bolt-{LLVM_VERSION}")
    os.system(f"sudo ln -s /usr/bin/llvm-bolt-{LLVM_VERSION} /usr/bin/llvm-bolt")
    os.system(f"sudo ln -s /usr/bin/merge-fdata-{LLVM_VERSION} /usr/bin/merge-fdata")
    os.system(f"sudo cp -r /usr/lib/llvm-{LLVM_VERSION}/lib /usr/lib")
