def encode(data):
    bin_conv = []
    for c in data:
        ascii_val = ord(c)
        binary_val = bin(ascii_val)
        sliced_binary = binary_val[2:]
        while len(sliced_binary) != 8:
            sliced_binary = '0'+sliced_binary 
        bin_conv.append(sliced_binary) 
    return (' '.join(bin_conv))

def decode(binary_str):
    binary_values = binary_str.split(' ')
    decoded_chars = []
    for binary_val in binary_values:
        decimal_val = int(binary_val, 2)
        decoded_char = chr(decimal_val)
        decoded_chars.append(decoded_char)
    decoded_str = ''.join(decoded_chars)
    return decoded_str

def AccessControl(medium):
    # CSMA random access control 
    if medium == 'Idle':
        return True
    else:
        return False
