string_of_stops = input()
command = input()
while command != 'Travel':
    command = command.split(':')
    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0 <= index <= len(string_of_stops):
            string_of_stops = string_of_stops[:index] + string + string_of_stops[index:]
        print(string_of_stops)
    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= len(string_of_stops) and start_index < end_index <= len(string_of_stops):
            string_of_stops = string_of_stops[:start_index] + string_of_stops[(end_index + 1):]
        print(string_of_stops)
    elif command[0] == 'Switch':
        old_string = command[1]
        new_sting = command[2]
        if old_string in string_of_stops:
            string_of_stops = string_of_stops.replace(old_string, new_sting)
        print(string_of_stops)
    command = input()
print(f"Ready for world tour! Planned stops: {string_of_stops}")
