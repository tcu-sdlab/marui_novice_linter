def main():
    num = input()
    signal = list(input())
    len_signal = len(signal)
    if signal[0] == '<':
        try:
            left_num = signal.index('>')
        except ValueError:
            return len_signal
    else:
        left_num = 0
    signal.reverse()
    if signal[0] == '>':
        try:
            right_num = signal.index('<')
        except ValueError:
            return len_signal
    else:
        right_num = 0
    return left_num + right_num


if __name__ == "__main__":
    print(main())