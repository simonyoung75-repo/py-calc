# defining functions...
def add(x, y):
    return x+y  # return passes the operation back to the function so i can use it later...
def sub(x, y):
    return x-y
def mul(x, y):
    return x*y
def div(x, y):
    return x/y

# asking users to input an operation and creating a variable for the input...
print("") # just to make it look prettier in the console
print("Pease select your operation.")
print("")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("")

#  this loops the choice input if the value is not 1, 2, 3 or 4
while True:
    choice = input("Enter choice - 1, 2, 3 or 4: ")
    isDigit = choice.isdigit()
   
    if not(isDigit):
        print("")
        print("Thats a letter, you're too stupid for calculators, im outta here")
        print("")
        exit()
   
    num = int(choice)
   
    if num in (1,2,3,4):
        break
    else:
        print("")
        print("Invalid entry dumbo, please enter 1 - 4")
        print("")

# just a bit of sillinesss...
match int(choice):
    case 1:
        print("")
        print("Solid choice, I love it when I add up some numbers")
        print("")
    case 2:
        print("")
        print("Interesting choice, I don't really believe in subtraction")
        print("")
    case 3:
        print("")
        print("Really, are you sure you want to multiply? The numbers can get pretty big")
        print("")
    case 4:
        print("")
        print("People who 'divide' numbers are dead to me... Good luck with the rest of your life")
        print("")

# asking users to input two numbers (integers), and assigning them to variables...
num1 = int(input("Enter your first number please: "))
num2 = int(input("Enter your second number please: "))

# me being stupid again!
print("")
print("Brace yourself... I'm about to hit you with some solid calculator action...")
print("")

# putting a false delay in so it looks like its thinking about things
import time
time.sleep(1)

# calling the functions and calclulating the answer
match int(choice):
    case 1:
        print(f"{num1} + {num2} = {add(num1,num2)}")
    case 2:
        print(f"{num1} + {num2} = {sub(num1,num2)}")
    case 3:
        print(f"{num1} + {num2} = {mul(num1,num2)}")
    case 4:
        print(f"{num1} + {num2} = {div(num1,num2)}")

# me being stupid again!
print("")
print("Thanks for using my calculator, don't forget to tell Sam I'm a better developer than he is now!!")
print("")