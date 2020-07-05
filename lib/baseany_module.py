import base64

def encode_base(msg, base):
    try: return eval(f'base64.b{base}encode(f"{msg}".encode())')
    except: return False

def decode_base(msg, base):
    try: return eval(f'base64.b{base}decode(f"{msg}".encode())')
    except: return False
