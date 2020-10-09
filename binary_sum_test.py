from binary_sum import binary_sum

cases = [
    '1,0\n',
    '10,001\n',
    '110,10001\n',
    '1101,01011\n'
]

outcomes = [
    '1',
    '11',
    '10111',
    '11000'
]

for idx, case in enumerate(cases):
    assert outcomes[idx] == binary_sum(case)