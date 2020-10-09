def capitalize(line):
    spl = line.split()
    return ' '.join(list(map(lambda x: x[0].upper()+x[1:], spl)))