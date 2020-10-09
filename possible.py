def partitions(s):
    if len(s) > 0:
        for i in range(1, len(s)+1):
            first, rest = s[:i], s[i:]
            for p in partitions(rest):
                yield [first] + p
    else:
        yield []

def isValid(s):
    return all(map(lambda x: int(x) > 0 and int(x) <= 26, s))

def possible(line):
    return len(list(filter(isValid, partitions(line.strip()))))