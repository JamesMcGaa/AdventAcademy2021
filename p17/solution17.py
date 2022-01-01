INPUT_X = (265, 287)
INPUT_Y = (-103, -58)

EXAMPLE_X = (20, 30)
EXAMPLE_Y = (-10, -5)

# returns timestamps [], is_final_timestamp_perpetual boolean 
def hits_x_timestamps(x_velocity, x_ranges):
    timestamps = []

    timestamp = 0
    x_pos = 0 
    while x_pos < x_ranges[1] and x_velocity != 0: #while still further valids to go and still going
        timestamp += 1
        new_x_pos = x_pos + x_velocity
        new_x_velocity = max(0, x_velocity - 1)

        if new_x_pos >= x_ranges[0] and new_x_pos <= x_ranges[1]:
            timestamps.append(timestamp)

        if new_x_velocity == 0:
            return timestamps, True
        else:
            x_pos = new_x_pos
            x_velocity = new_x_velocity


    return timestamps, False

# returns timestamps []
def hits_y_timestamps(y_velocity, y_ranges):
    timestamps = []

    timestamp = 0
    y_pos = 0 
    while y_pos >= y_ranges[0] or y_velocity > 0: #if we are both falling and below, return
        timestamp += 1
        new_y_pos = y_pos + y_velocity
        new_y_velocity = y_velocity - 1

        if new_y_pos >= y_ranges[0] and new_y_pos <= y_ranges[1]:
            timestamps.append(timestamp)

        y_pos = new_y_pos
        y_velocity = new_y_velocity


    return timestamps

# print(hits_x_timestamps(7, EXAMPLE_X))
# print(hits_y_timestamps(2, EXAMPLE_Y))

# x_results = {}
y_results = {}
valid_timestamps = set()
lowest_perpetual = 1000000000000000000
for x_vel in range(1, EXAMPLE_X[1] + 1):
    timestamps, perpetual = hits_x_timestamps(x_vel, EXAMPLE_X)
    for timestamp in timestamps:
        valid_timestamps.add(timestamp)
    if perpetual and len(timestamps) > 0:
        lowest_perpetual = min(lowest_perpetual, timestamps[-1])

    # x_results[x_vel] = hits_x_timestamps(x_vel, EXAMPLE_X)
import sys
for y_vel in reversed(range(1, abs(EXAMPLE_Y[0]) + 1)):
    # y_results[y_vel] = hits_y_timestamps(y_vel, EXAMPLE_Y)
    possibles = hits_y_timestamps(y_vel, EXAMPLE_Y)
    if len(possibles) == 0:
        continue
    for timestamp in possibles:
        if timestamp in valid_timestamps or timestamp >= lowest_perpetual:
            print(y_vel * (y_vel + 1) / 2)
            sys.exit()

# def exists_x_for_timestamps(y_timestamps):
#     for timestamp in timestamps: 