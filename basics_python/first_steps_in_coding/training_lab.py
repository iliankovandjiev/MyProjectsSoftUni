h_room = float(input())
w_room = float(input())
w_room_without_co = w_room - 1
w_desk = w_room_without_co // 0.7
h_desk = h_room // 1.2
total_desk = w_desk * h_desk - 3
print(total_desk)


