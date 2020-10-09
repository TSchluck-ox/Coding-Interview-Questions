from possible import possible

cases = [
    '123',
    '1234',
    '21251',
    '12',
]

outcomes = [
    3,
    3,
    5,
    2
]

for idx, case in enumerate(cases):
    assert possible(case) == outcomes[idx]