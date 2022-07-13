from collections import deque

def create_queue(list):
    linked_list_q = deque()

    for num in list:
        linked_list_q.append(num)

    return linked_list_q

def main():
    my_list = [7, 10, 15, 2, 28, 91, 5, 83]
    
    my_queue = create_queue(my_list)
    print(my_queue)

    while len(my_queue) != 0:
        print(my_queue.popleft())

main()