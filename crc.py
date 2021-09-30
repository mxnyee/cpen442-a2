import timeit

# Algo to find next step given input

def num_to_bits(num: int):
    # https://stackoverflow.com/a/16660062
    num_bits = len(bin(num)) - 2
    return [(num >> bit) & 1 for bit in range(num_bits - 1, -1, -1)]

offset_map = {
    0: 7,
    1: 6,
    2: 5,
    3: 4,
}

poly = 69995715440 # crc-32 polynomial, 0x104C11DB70

def crc_step(input):
    # Convert hex to array of bits
    num = input
    num_bits = len(bin(num)) - 2
    bits = num_to_bits(num)
    print(hex(num))

    # Pad with leading 0s until byte-aligned
    while num_bits % 8 != 0:
        bits.insert(0, 0)
        num_bits += 1
    print('padded input:   ', ''.join([str(b) for b in bits]))

    # Reverse each byte
    for i, bit in enumerate(bits):
        offset = i % 8;
        if offset <= 3:
            base = i - offset
            j = base + offset_map[offset]
            bits[i], bits[j] = bits[j], bits[i] # swap
    print('reversed input: ', ''.join([str(b) for b in bits]))
    
    # Pad polynomial with trailing 0s until matching MSB
    p_bits = num_to_bits(poly)
    p_num_bits = len(bin(poly)) - 2
    while p_num_bits < num_bits:
        p_bits.append(0)
        p_num_bits += 1
    print('padded poly:    ', ''.join([str(b) for b in p_bits]))
    
    # XOR to get result
    result = [bits[i] ^ p_bits[i] for i in range(num_bits)]
    print('result:         ', ''.join([str(b) for b in result]))

    # Reverse each byte of result
    for i, bit in enumerate(result):
        offset = i % 8;
        if offset <= 3:
            base = i - offset
            j = base + offset_map[offset]
            result[i], result[j] = result[j], result[i] # swap
    print('reversed result:', ''.join([str(b) for b in result]))

    # Convert to num then hex
    n = 0;
    for i, b in enumerate(result):
        n += b * 2**(num_bits - i - 1)

    h = hex(n)
    print(h)
    
start = timeit.default_timer()
crc_step(0xDC12C44703879F4EABAB83F6643B328C)
stop = timeit.default_timer()
print('Time: ', stop - start)
