from bcd import bcd

cases = [
    '1\n',
    '123\n',
    '24\n',
    '782\n'
]

outcomes = [
    '0001',
    '0001 0010 0011',
    '0010 0100',
    '0111 1000 0010'
]

for idx, case in enumerate(cases):
    assert outcomes[idx] == bcd(case)