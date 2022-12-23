import math

# Initialize the position of the robot
x = 0
y = 0

# Store the movements of the robot in a list
moves = ["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]

# Loop through the list of movements
for move in moves:
    # Split the move string into the direction and the distance
    direction, distance = move.split(" ")

    # Update the position of the robot based on the direction and distance
    if direction == "UP":
        y += int(distance)
    elif direction == "DOWN":
        y -= int(distance)
    elif direction == "LEFT":
        x -= int(distance)
    elif direction == "RIGHT":
        x += int(distance)

print(f"Ending position:  (x)={x}, (y)={y}")

# Use the Pythagorean theorem to compute the distance the robot has traveled
distance = math.sqrt(x**2 + y**2)
print("Distance traveled: ", distance)
