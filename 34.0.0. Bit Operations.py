# counting bits
# bit shifting
# bit operator coding have many tricks, not very often in coding interviews.

n = 20
n = n >> 1
# The binary representation of 20 is 10100.
# Shifting it right by 1 bit gives 01010, which is the binary representation of 10.
print(n)
n = n << 1
# The binary representation of 10 is 01010.
# Shifting it left by 1 bit gives 10100, which is the binary representation of 20.
print(n)


def countBits(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1  # same as n = n // 2
    return count


print(countBits(23))


# AND
n = 1 & 1

# OR
n = 1 | 1

# XOR
n = 1 ^ 1

# NOT
n = ~1

# Bit shifting
n = 1
n = 1 << 1
n = 1 >> 1