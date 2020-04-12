import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")
previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
    if equation == "quit":
        print("Goodbye humaaannn")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:_""" "]', "",equation)

        if previous == 0:
            previous = eval(equation)
            print("You typed: ", previous)
        else:
            previous = eval(str(previous)+equation)
            print("Result is: ", previous)

while run:
      performMath()
