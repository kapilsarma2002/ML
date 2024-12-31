def add(a, b):
  return a + b;

def subtract(a, b):
  return a - b;

def multiply(a, b):
  return a * b;

def divide(a, b):
  return a / b;

def main():
  print(add(1, 2))
  print(subtract(1, 2))
  print(multiply(1, 2))
  print(divide(1, 2))

if __name__ == "__main__":
  # main()
  a = [1, 2, 3, 4, 5]
  a[1:3] = [-1,-1]
  print(a)