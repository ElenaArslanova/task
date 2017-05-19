try:
    from math import gcd
except ImportError:
    from fractions import gcd

operations_amount = int(input())
data = []

apply_operation = {
    '+': lambda l, x: l.append(x),
    '-': lambda l, x: l.remove(x)
}

for i in range(operations_amount):
    operation, value = input().split()
    apply_operation[operation](data, int(value))
    current_gcd = None
    for value in data:
        if current_gcd is None:
            current_gcd = value
        else:
            current_gcd = gcd(current_gcd, value)
    print(current_gcd)