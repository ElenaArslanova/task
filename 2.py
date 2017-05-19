from functools import reduce
try:
    from math import gcd
except ImportError:
    from fractions import gcd


class GCD:
    @staticmethod
    def calculate(x, y):
        return gcd(x, y)


class Aggregator:
    def __init__(self, collection, aggregator_function):
        self.collection = collection
        self.function = aggregator_function

    def aggregate(self):
        return reduce(self.function, self.collection)


class GCDAggregator(Aggregator):
    def __init__(self, collection):
        super().__init__(collection, lambda x, y: GCD.calculate(x, y))


apply_operation = {
    '+': lambda l, value: l.append(value),
    '-': lambda l, value: l.remove(value)
}

operations_amount = int(input())
data = []
for i in range(operations_amount):
    operation, value = input().split()
    apply_operation[operation](data, int(value))
    print(GCDAggregator(data).aggregate())
