from collections import deque

integer_input = int(input())
stack = deque()

map_function = {
    1: lambda x: stack.append(x[1]),
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None,
}

for _ in range(integer_input):
    number_data = [int(x) for x in input().split()]
    map_function[number_data[0]](number_data)


stack.reverse()

print(*stack, sep=', ')
