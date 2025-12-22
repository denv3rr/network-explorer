# run.py
# Simple launcher: installs minimal deps and runs main app (network_explorer.py)

import importlib.util
import subprocess
import sys
import os

REQUIRED_PACKAGES = ['requests', 'ifaddr', 'texttable', 'bleak', 'colorama']


def is_installed(pkg: str) -> bool:
    return importlib.util.find_spec(pkg) is not None


def check_and_install_requirements():
    missing = [p for p in REQUIRED_PACKAGES if not is_installed(p)]
    if missing:
        print(f"[🔧] Installing missing packages: {', '.join(missing)}")
        if os.getenv("NEX_AUTO_INSTALL") != "1" and sys.stdin.isatty():
            resp = input("Install missing packages now? (y/N): ").strip().lower()
            if resp not in ("y", "yes"):
                print("Aborting. Set NEX_AUTO_INSTALL=1 to auto-install.")
                sys.exit(1)

        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])


def main():
    check_and_install_requirements()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)

    import network_explorer  # type: ignore

    network_explorer.main()


if __name__ == "__main__":
    main()
