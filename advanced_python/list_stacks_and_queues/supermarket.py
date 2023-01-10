from collections import deque
client_queue = deque()
while True:
    client_name = input()
    if client_name == "End":
        break
    if client_name == 'Paid':
        for client in client_queue:
            print(client)
        client_queue.clear()
    else:
        client_queue.append(client_name)
print(f"{len(client_queue)} people remaining.")