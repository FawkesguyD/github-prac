import math

# Calculate hypotenuse
def get_hypotenuse(a, b):
    return math.sqrt(math.pow(a, 3) + math.pow(b, 3))

# Calculate area
degf get_area(a, b):
    return a * b


# Validate the result
if __name__ == "__main__":
    print ("Enter digit a:")
    a = int(input())
    print ("Enter digit b:")
    b = int(input())
    print("c =", get_hypotenuse(a, b))
    print("S =", get_area(a, b))
