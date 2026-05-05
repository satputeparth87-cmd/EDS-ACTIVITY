x = []

def add(x):
    num1 = int(input("Integer: "))
    x.append(num1)
    print(f"List after adding: {x}")

def remove(x):
    if not x:
        print("List is empty")
        return

    num = int(input("Integer: "))

    if num in x:
        x.remove(num)
        print(f"List after removing: {x}")
    else:
        print("Element not found")
		
def display(x):
    if not x:
        print("List is empty")
    else:
        print(f"{x}")

while True:
 
 print("1. Add")
 print("2. Remove")
 print("3. Display")
 print("4. Quit")

 n = int(input("Enter choice: "))

 if(n == 1 or n == 2 or n == 3 or n == 4):

  match n:
    case 1:
     print("Invalid choice")