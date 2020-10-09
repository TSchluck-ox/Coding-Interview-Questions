def binary_sum(line):
    num1, num2 = line.strip().split(',')
    return '{:b}'.format(int(num1, 2) + int(num2, 2))