import math


def swap(a, b):
    return b, a


def gcd(a, b):
    a, b = abs(a), abs(b)
    if a < b:
        a, b = swap(a, b)
    while b:
        b, a = a % b, b
    return a


def find_xy(r0, r1, d):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while r1 != d:
        q, r = divmod(r0, r1)
        x2 = x0 - x1 * q
        y2 = y0 - y1 * q
        x0, y0, r0 = x1, y1, r1
        x1, y1, r1 = x2, y2, r
    return [x1, y1]


def find_inverse(x, n):
    return find_xy(x, n, gcd(x, n))[0] % n


def find_private_key(e, phi_n):
    return find_inverse(e, phi_n)


def decrypt_rsa(c, priv_key, n):
    return expmod(c, priv_key, n)


def calc_phi_n(prim_composite):
    product = 1
    for prime in prim_composite:
        product *= prime * (1 - 1 / prime)
    return int(product)


def expmod(base, power, modulus):
    exp = 1
    while power:
        if power & 1:
            exp = (exp * base) % modulus
        base = (base ** 2) % modulus
        power >>= 1
    return exp % modulus


def factor_n(e, d, n):
    def test_power(remainder, mult):
        return not remainder and mult % 2

    prod = e * d - 1 # ed = 1 mod phi_n
    power, step = -1, -1

    for k in range(1, int(math.log2(prod)) + 1):
        m, r = divmod(prod, (2 ** k))
        if test_power(r, m):
            power = m
            step = k
            print("Odd number m and power k:", power, step)
            break

    if power == -1 or step == -1:
        print("Error finding odd m for phi_n")
        exit(1)

    found = False
    for base in range(2, n - 1):
        if gcd(base, n) != 1:
            continue
        b_prev = expmod(base, power, n)
        for i in range(step - 1):
            b = (b_prev ** 2) % n
            if b == -1:
                print("Base", base, "doesn't work, try a different base")
                break
            elif b == 1:
                found = True
                break
            b_prev = b
        if found:
            return gcd(b_prev - 1, n), gcd(b_prev + 1, n)
    print("n cannot be factored")
    exit(1)


def q1_nc():
    print("Question 1:")
    p, q = 101, 113
    n = p * q
    n_composite = [ p, q ]
    phi_n = calc_phi_n(n_composite)
    e, c = 7467, 5859
    d = find_private_key(e, phi_n)
    print("phi_n:", phi_n)
    print("private key:", d)
    print("Plaintext:", decrypt_rsa(c, d, n), "\n")


def q4_nc():
    print("Question 4:")
    print("private key:", find_private_key(3, 100), "\n")


def q2():
    print("Question 2:")
    n, e, d = 718548065973745507, 3449, 543546506135745129
    p, q = factor_n(e, d, n)
    print("Factors:", p, q, "\n")

def q6():
    print("Question 6:")
    n, a, b = 537069139875071, 85975324443166, 462436106261
    # a^2 = b^2 (mod n) <=> (a^2 - b^2) = nk
    # <=> gcd(a+b, n), gcd(a-b, n)
    print("Factors:", gcd(a + b, n), gcd(a - b, n), "\n")


def q8():
    print("Question 8:")
    print("Part a:")
    n, a, b = 670726081, 670705093, 33335
    print("Factors:", gcd(a + b, n), gcd(a - b, n), "\n")
    print("Part b:")
    a, b = 670726078, 3
    s = "This one doesn't help,\n" \
        "since a + b = n and a - b is coprime to n.\n" \
        "Therefore it reveals nothing about the factorization.\n"
    print("Factors:", gcd(a + b, n), gcd(a - b, n))
    print(s)


def q14():
    print("Question 14:")
    print("Using Generalized Chinese Remainder Theorem")
    n1, n2, n3 = 2469247531693, 11111502225583,44444222221411
    c1, c2, c3 = 359335245251, 10436363975495, 5135984059593
    e = 3
    z1, z2, z3 = n2 * n3, n1 * n3, n1 * n2
    y1, y2, y3 = find_inverse(z1, n1), find_inverse(z2, n2), find_inverse(z3, n3)

    print("y1, z1:", y1, ",", z1)
    print("y2, z2:", y2, ",",  z2)
    print("y3, z3:", y3, ",",  z3)

    m_cube = (c1 * y1 * z1 + c2 * y2 * z2 + c3 * y3 * z3) % (n1 * n2 * n3)
    print("Result of adding all ci * yi * zi 's mod n1 * n2 * n3:", m_cube)
    m = round(m_cube ** (1/3))
    print("Decrypted message:", m)


def q12_nc():
    print("Question 12:")
    n = 642401
    a = 516107 * 2
    b = 187722
    print(a)
    if a % n == b:
        print("The information doesn't help")
    else:
        p, q = gcd(a + b, n), gcd(a - b, n)
        print("Factor:", p, q)

def main():
    q1_nc()
    q4_nc()
    q12_nc()
    #q2()
    #q6()
    #q8()
    #q14()

if __name__ == "__main__":
    main()
