dw = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
print('YES' if (-dw.index(input()) + dw.index(input()) + 7) % 7 in (0, 2, 3) else 'NO')