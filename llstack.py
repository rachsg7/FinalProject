from collections import deque

def stack_append(list):
    linked_list = deque()
    
    for num in list:
        linked_list.append(num)

    return linked_list
    

def main():
    my_list = [0, 1, 2 ,3, 4, 5]
    stack = stack_append(my_list)

    print(stack)

    while len(stack) != 0:
        print(stack.pop())

if __name__ == '__main__':
    main()