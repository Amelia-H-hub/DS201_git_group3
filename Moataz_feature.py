for i in range(1, n + 1):       # loop rows
    for j in range(i):          # prnt i stars
        print("*", end="")
    print()

print()                         # blank line

# shape 2 – middle triangel (point up)
for row in range(n):
    for _ in range(n - row - 1):    # spaces on left
        print(" ", end="")
    for _ in range(2 * row + 1):    # stars line
        print("*", end="")
    print()

print()
