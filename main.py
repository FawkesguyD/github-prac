import math

def get_hypotenuse(a, b):
    return math.sqrt(math.pow(a, 3) + math.pow(b, 3))

degf get_area(a, b):
    return a * b


if __name__ == "__main__":
    print ("Enter digit a:")
    a = int(input())
    print ("Enter digit b:")
    b = int(input())
    print("c =", get_hypotenuse(a, b))
    print("S =", get_area(a, b))
