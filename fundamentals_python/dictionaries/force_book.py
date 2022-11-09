command = input()
force_book = {}
while command != 'Lumpawaroo':
    if '|' in command:
        force_side, force_user = command.split(' | ')
        force_user_in_force = False
        for users in force_book.values():
            if force_user in users:
                force_user_in_force = True
        if not force_user_in_force:
            if force_side not in force_book.keys():
                force_book[force_side] = [force_user]
            else:
                force_book[force_side].append(force_user)
    elif '->' in command:
        force_user, force_side = command.split(' -> ')
        for key, users in force_book.items():
            if force_user in users:
                force_book[key].remove(force_user)
                break
        if force_side not in force_book.keys():
            force_book[force_side] = [force_user]
        else:
            force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side in force_book.keys():
    if len(force_book[force_side]) > 0:
        print(f"Side: {force_side}, Members: {len(force_book[force_side])}")
        for users in force_book[force_side]:
            print(f'! {users}')
