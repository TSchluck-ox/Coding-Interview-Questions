from capitalize import capitalize

cases = [
    'hello, world!',
    'other,thing here',
    'here:as wellas there',
    'ignore&punctuation',
]

outcomes = [
    'Hello, World!',
    'Other,thing Here',
    'Here:as Wellas There',
    'Ignore&punctuation'
]

for idx, case in enumerate(cases):
    assert capitalize(case) == outcomes[idx]