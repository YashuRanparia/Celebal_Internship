def lower_triangle(rows):
  for i in range(rows):
    for j in range(i + 1):
      print("*", end=" ")
    print()

def upper_triangle(rows):
  for i in range(rows):
    for j in range(rows):
      if j > i:
        print("*", end=" ")
      else:
        print(" ", end=" ")
    print()

def pyramid(rows):
  for i in range(rows):
    spaces = rows - i - 1
    print(" " * spaces, end="")
    print("*" * (2 * i + 1))

if __name__ == "__main__":
    rows = 5
    print("Lower triangle:")
    lower_triangle(rows)
    print("\nUpper triangle:")
    upper_triangle(rows)
    print("\nPyramid:")
    pyramid(rows)
