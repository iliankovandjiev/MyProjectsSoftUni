unique_username = set()

for _ in range(int(input())):
    username = input()
    unique_username.add(username)

print(*unique_username, sep='\n')
