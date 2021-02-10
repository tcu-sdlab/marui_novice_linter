def main():
    str = input()
    for i, ch in enumerat(str):
        ch = int(ch)
        if i == 0 and ch == 9:
            print(9, end='')
        else:
            print(min(ch, 9 - ch), end='')

def enumerat(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

main()