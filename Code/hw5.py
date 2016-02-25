#from sympy import *
#x, y, z = symbols('x,y,z')
#init_printing(use_unicode=False, wrap_line=False, no_global=True)


def expmod(base, power, modulus):
    exp = 1
    while power:
        if power & 1:
            exp = (exp * base) % modulus
        base = (base ** 2) % modulus
        power >>= 1
    return exp % modulus


def q1_nc():
    a = 8.0 * x**4 - 12 * x**3 + 8 * x - 3
    b = 4 * x**3 - 4 * x**2 - 3 * x + 2
    print(gcd(a, b))

def q2_nc():
    number = 2048
    n = 65537
    phi_n = 65536
    list = []
    for i in range(1, 32):
        if i % 2:
            list.append(number * i)

    for i in list:
        if expmod(3, i, n) == 2:
            print(i, i / number)




def main():
    #q1_nc()
    q2_nc()


if __name__ == "__main__":
    main()