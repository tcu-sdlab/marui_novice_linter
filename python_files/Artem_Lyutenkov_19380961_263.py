for i in range(5):
    a = input()
    if '1' in a:
        print(abs(2 - i) + int(abs(4 - a.find('1')) / 2))
        break