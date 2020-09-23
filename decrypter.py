# Made for school task
# Inverse of d must be calculated by hand
def decrypt(c_blocks, e, p, q, d):
    n = p * q
    a_list = list(str(bin(d)))
    a_list = [int(a) for a in a_list[2:]]

    m_blocks = []
    print(f'Decrypting {" ".join([str(c) for c in c_blocks])} using key ({p}*{q}, {e}), where {d} is the inverse of {e} mod {p-1}*{q-1}')
    for c in c_blocks:
        print(f'Block being decrypted: {c}')

        x = 1
        power = c % n
        for i, a in enumerate(a_list[::-1]):
            if a:
                x = (x * power) % n
            power = (power * power) % n
            print(f'a_{i} = {str(a)} => x = {x} and power = {power}')
        print(f'Decrypted block is {format(x, "04d")}\n')
        m_blocks.append(format(x, '04d'))
    print(f'Decrypted numbers is {" ".join(m_blocks)}')


if __name__ == '__main__':
    decrypt([3185, 2038, 2460, 2550], 17, 53, 61, 2753)