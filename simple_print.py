import time
import sys

for i in range(21):
    bar = "█" * i + "-" * (20 - i)
    sys.stdout.write(f"\rLoading [{bar}] {i*5}%")
    sys.stdout.flush()
    time.sleep(0.2)

print("\nGame Loaded ✅")
