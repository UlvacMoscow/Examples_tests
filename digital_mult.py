from functools import reduce
""" х никогда не будет итерироваться по последнему элементу,
    у никогда не будет первым элементом """
def checkio(number: float) -> float:


    return reduce(lambda x, y: int(x) * int(y) if x != "0" and x != '.' else int(x), str(number))

print(checkio(10888888))
# print(01)
