def gcd(a, b):
    if b == 0:
        return a
    if a < b:
        temp = a
        a = b
        b = temp
    q, r = divmod(a, b)
    return gcd(b, r)

def find_xy(a, b, x0, y0, r0, x1, y1, r1, d):
    if r1 == d:
        list = [ x1, y1 ]
        return list
    q, r = divmod(r0, r1)
    x2 = x0 - x1 * q
    y2 = y0 - y1 * q
    return find_xy(a, b, x1, y1, r1, x2, y2, r, d)

def print_gcd(a, b):
    print("gcd(" + str(a) + ", " + str(b) + ") =", gcd(a, b))

def q1():
    print("Question 1:")
    a, b = 8765, 23485
    print_gcd(a, b)
    print("")

def q2():
    print("Question 2:")
    a, b = 65537, 3511
    print_gcd(a, b)
    d = 1
    if gcd(a, b) != d:
        print("Error")
        return

    list = find_xy(a, b, 1, 0, a, 0, 1, b, d)
    print("part a: value for [x, y]:", list)
    mult = 17
    list2 = []
    for value in list:
        value *= mult
        list2.append(value)
    print("part b: value for [x, y]:", list2)
    print("")

def q3():
    print("Question 3:")
    p = 1234567
    n = 100000
    print("Print the last five digit is the same as taking mod", n)
    si = int(n * (1 - 1/2) * (1 - 1/5))
    print("Number of 100000's coprimes:", si)
    print("Last five digit:", (3 ** (p % si)) % n)
    print("")

def q4():
    print("Question 4:")
    a = 314
    b = 11111
    r = 271
    d = gcd(a, b)
    print_gcd(a, b)
    list = find_xy(a, b, 1, 0, a, 0, 1, b, d)
    a_inverse = list[0]
    print("Value of x (mod" + str(b) + "):", (271 * a_inverse) % b)
    print("")

def q6_subfunc(a, b, r1, r2):
    list = find_xy(a, b, 1, 0, a, 0, 1, b, 1)
    x, y = list[0], list[1]
    print("x, y value for", a ,"and", b, ":", x, ",", y, "such that ax + by = 1")
    val = a * x * r2 + b * y * r1
    new_mod = a * b
    r = val % new_mod
    ret = [ val, new_mod, r ]
    return ret


def q6():
    print("Question 6:")
    a, b, c, r1, r2, r3 = 101, 201, 301, 17, 18, 19
    if gcd(a, b) != 1 and gcd(a, c) != 1 and gcd(b, c) != 1:
        print("Error")
        return
    ret = q6_subfunc(b, a, r2, r1)
    val, new_mod, r = ret[0], ret[1], ret[2]
    ret = q6_subfunc(new_mod, c, r, r3)
    val, new_mod, r = ret[0], ret[1], ret[2]
    print("value that satisfies the three conditions:", val)
    print("new modulus value:", new_mod)
    print("new remainder:", r)

def main():
    q1()
    q2()
    q3()
    q4()
    q6()

if __name__ == "__main__":
    main()