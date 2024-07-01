from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

def main():
    print("Simple Calculator Program")
    
    a = 10
    b = 5
    c=4
    
    print(f"Addition of {a} and {b}: {add(a, b,c)}")
    print(f"Subtraction of {a} and {b}: {subtract(a, b,c)}")
    print(f"Multiplication of {a} and {b}: {multiply(a, b,c)}")
    print(f"Division of {a} and {b}: {divide(a, b,c)}")

if __name__ == "__main__":
    main()
