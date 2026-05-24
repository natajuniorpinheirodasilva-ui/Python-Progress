import sys

h = float(input())
f = float(input())
n = int(input())
sys.stdout.flush()

while True:
    try:
        if h >= 1 and h <= 1000 and f >= 0 and f <= 1 and n >= 1 and n <= 100:
            total = h
            for i in range(1, n):
                total += 2 * h * (f ** i)
            print(total)
        break
    except ValueError:
        continue