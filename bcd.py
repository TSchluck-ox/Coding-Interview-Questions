def bcd(line):
    to_bcd = lambda x: '{:04b}'.format(int(x))
    digits = list(line.strip())
    return ' '.join(list(map(to_bcd, digits)))