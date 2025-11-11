#!/usr/bin/env python3
from pathlib import Path

ALLOW = Path("allow_list.txt")
REMOVE = Path("remove_list.txt")

def read_lines(p: Path) -> list[str]:
    if not p.exists():
        return []
    return [line.strip() for line in p.read_text().splitlines() if line.strip()]

def main():
    ip_addresses = read_lines(ALLOW)
    remove_list = set(read_lines(REMOVE))

    # preserve order while filtering
    updated = [ip for ip in ip_addresses if ip not in remove_list]

    # write back
    ALLOW.write_text("\n".join(updated) + ("\n" if updated else ""))

    print(f"Removed {len(ip_addresses) - len(updated)} entries.")
    print(f"Remaining {len(updated)} entries written to {ALLOW}")

if __name__ == "__main__":
    main()
