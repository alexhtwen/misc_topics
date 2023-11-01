def stuff(raw: str, start: int, len_del: int, insert: str) -> str:
    return f'{raw[0:start]}{insert}{raw[start + len_del:]}'

raw = '0123456789' * 3
print(raw)
print(f'{stuff(raw, 3, 2, 'abc' ) = }')
print(f'{stuff(raw, 11, 5, '' ) = }')
print(f'{stuff(raw, 8, 0, 'Python' ) = }')