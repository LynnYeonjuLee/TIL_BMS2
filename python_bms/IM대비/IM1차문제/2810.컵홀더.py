N = int(input())
# seat = list(map(str,input()))
seat = str(input())
seat_S = seat.count('S')
seat_L = seat.count('L') // 2
cup_holder = 1 + seat_S + seat_L
if 'S' in seat and 'L' in seat:
    print(cup_holder)
elif 'S' in seat and 'L' not in seat: 
    print(seat_S)