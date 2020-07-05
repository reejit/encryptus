a_z = ''.join(map(chr, range(ord('a'), ord('z') + 1)))
conv_table = dict(zip(a_z, sorted(a_z, reverse=True)))
conv_table_upper = dict(zip(a_z.upper(), sorted(a_z.upper(), reverse=True)))
conv_table[' '] = ' '

def atbash(message) -> str:
    for char in message.replace(' ', ''):
        if not char.isalpha():
            message = message.replace(char, '')
    return ''.join([conv_table[char] if not char.isupper() else conv_table_upper[char] for char in message])
