# Python Automation — Update Allow List

This script removes IPs listed in **remove_list.txt** from **allow_list.txt**, then writes back the updated list.

## Files
- `update_allow_list.py` — runnable script
- `allow_list.txt` — sample input (one IP per line)
- `remove_list.txt` — sample input

## Usage

```bash
python update_allow_list.py
# updated allow_list.txt is written in-place
```

## Notes
- Uses safe file I/O context managers.
- Splits on newline; de-duplicates while preserving order.
