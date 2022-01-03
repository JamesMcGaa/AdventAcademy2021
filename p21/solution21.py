dice_location = 1
# p1_location = 4
# p2_location = 8

p1_location = 7
p2_location = 4

dice_counter = 0
p1_counter = 0
p2_counter = 0

while True:
    move_counter = 0
    for i in range(3):
        move_counter += 1
        p1_location = (p1_location + dice_location - 1) % 10 + 1
        dice_location = (dice_location % 100) + 1
    
    dice_counter += 3
    p1_counter += p1_location
    if p1_counter >= 1000:
        print(dice_counter * p2_counter)
        break

    move_counter = 0
    for i in range(3):
        move_counter += 1
        p2_location = (p2_location + dice_location - 1) % 10 + 1
        dice_location = (dice_location % 100) + 1
    
    dice_counter += 3
    p2_counter += p2_location
    if p2_counter >= 1000:
        print(dice_counter * p1_counter)
        break