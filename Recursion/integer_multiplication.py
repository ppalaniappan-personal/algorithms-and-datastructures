# Integer multiplication


def multiply(x, y, n):
    if n == 1:
        return x * y
    a = int(x / pow(10, n/2))
    b = int(x - (a * pow(10, n/2)))
    c = int(y / pow(10, n/2))
    d = int(y - (c * pow(10, n/2)))
    ac = multiply(a, c, n/2)
    bd = multiply(b, d, n/2)
    bc_plus_ad = multiply(b, c, n/2) + multiply(a, d, n/2)
    mul_result = (pow(10, n) * ac) + (pow(10, n/2) * bc_plus_ad) + bd
    return mul_result


x = 1234
y = 4567
n = len(str(x))

result = int(multiply(x, y, n))

print(result)
