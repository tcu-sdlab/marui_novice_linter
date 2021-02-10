bus = """+------------------------+
|#.#.#.#.#.#.#.#.#.#.#.|D|)
|#.#.#.#.#.#.#.#.#.#.#.|.|
|#.......................|
|#.#.#.#.#.#.#.#.#.#.#.|.|)
+------------------------+"""

bus = [list(line) for line in bus.split()]

n = int(input())
for i in range(4):
    if n <= 0:
        break
    bus[i + 1][1] = 'O'
    n -= 1

row = 1
col = 3
while n > 0:
    bus[row][col] = 'O'
    n -= 1
    row = 2 * row
    if row > 4:
        row = 1
        col += 2

print('\n'.join([''.join(line) for line in bus]))