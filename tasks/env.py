from os.path import dirname, abspath, join
from multiprocessing import cpu_count
import yaml

PROJ_ROOT = dirname(dirname(abspath(__file__)))

VERSIONS_FILE = join(PROJ_ROOT, "versions.yml")

TOOLCHAIN_IMAGE_NAME = "faasm/toolchain"
TOOLCHAIN_DOCKERFILE = join(PROJ_ROOT, "docker", "toolchain.dockerfile")
SYSROOT_IMAGE_NAME = "faasm/sysroot"
SYSROOT_DOCKERFILE = join(PROJ_ROOT, "docker", "sysroot.dockerfile")

USABLE_CPUS = int(cpu_count()) - 1

TOOLCHAIN_BIN = "/usr/local/faasm/toolchain/bin"
SYSROOT = "/usr/local/faasm/llvm-sysroot"

WASM_CC = join(TOOLCHAIN_BIN, "clang")
WASM_AR = join(TOOLCHAIN_BIN, "llvm-ar")
WASM_NM = join(TOOLCHAIN_BIN, "llvm-nm")


def _get_version_yaml_value(key):
    with open(VERSIONS_FILE) as fh:
        versions = yaml.load(fh)

    return versions[key]


def get_version():
    return _get_version_yaml_value("toolchain")


def get_llvm_version():
    return _get_version_yaml_value("llvm")