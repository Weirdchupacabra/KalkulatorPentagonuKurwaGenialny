#this is calculator. My first project in Python

def add(x, y):     #dodawanie
    return x + y
def subtract(x, y):    #odejmowanie
    return x - y
def multiply(x, y):   #mnozenie
    return x * y
def divide(x , y):   #dzielenie
    return x / y

print("Select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2)
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2)
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2)
        else:
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
