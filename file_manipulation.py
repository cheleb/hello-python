"""Sample: basic file manipulation (write, read, append, copy, rename, delete)."""
from pathlib import Path
import shutil
import tempfile


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)

        # Write
        src = base / "hello.txt"
        src.write_text("Hello, file!\n", encoding="utf-8")

        # Append
        with src.open("a", encoding="utf-8") as f:
            f.write("Second line\n")

        # Read
        print("Content:")
        for n, line in enumerate(src.read_text(encoding="utf-8").splitlines(), 1):
            print(f"  {n}: {line}")

        # Copy and rename
        copy = base / "copy.txt"
        shutil.copy(src, copy)
        renamed = copy.rename(base / "renamed.txt")

        # List
        print("Files:", sorted(p.name for p in base.iterdir()))

        # Delete
        renamed.unlink()
        print("After delete:", sorted(p.name for p in base.iterdir()))


if __name__ == "__main__":
    main()
