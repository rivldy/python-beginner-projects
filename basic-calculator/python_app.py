def add(a, b):
  answer = a + b
  print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
  answer = a - b
  print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a, b):
  answer = a * b
  print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
  answer = a / b
  print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")


while True:
  print("A. Addition")
  print("B. Subtraction")
  print("C. Multiplication")
  print("D. Division")
  print("E. Exit")

  choice = input("Input your choice: ").lower()

  if choice == "a":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    add(a, b)
  elif choice == "b":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    sub(a, b)
  elif choice == "c":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    mul(a, b)
  elif choice == "d":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    div(a, b)
  elif choice == "e":
    print("Program ended.")
    quit()