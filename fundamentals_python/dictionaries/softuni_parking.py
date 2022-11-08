number_of_commands = int(input())
registered_users = {}
for num in range(number_of_commands):
    commands = input().split()
    if commands[0] == 'register':
        username = commands[1]
        license_plate_number = commands[2]
        if username in registered_users.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            registered_users[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif commands[0] == 'unregister':
        username = commands[1]
        if username not in registered_users.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del registered_users[username]

for users in registered_users.keys():
    print(f"{users} => {registered_users[users]}")
