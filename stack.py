stack = []

user_input = input('Type something to see it reversed: ')

for letter in user_input:
    stack.append(letter)

while len(stack) != 0:
    print(stack.pop(), end="")