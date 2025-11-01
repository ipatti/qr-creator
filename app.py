import sys, qrcode
from pathlib import Path

if len(sys.argv) < 3:
    print("Usage: python app.py <text> <filename.png>")
    sys.exit(1)

text, name = sys.argv[1], Path(sys.argv[2])
img = qrcode.make(text)
img.save(name)
print(f"Saved -> {name.resolve()}")

