n = int(input(), 16)
print (n)

def twos_complement(n, bits):
    mask = 2**bits - 1
    if n < 0:
        n = ((abs(n)^mask) + 1)
    return bin(n & mask)[2:]

print(twos_complement(n, 8))