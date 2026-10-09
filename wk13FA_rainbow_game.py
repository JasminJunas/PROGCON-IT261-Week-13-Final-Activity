rainbowColors = [""] * (7)
correctColors = [""] * (7)

correctColors[0] = "Red"
correctColors[1] = "Orange"
correctColors[2] = "Yellow"
correctColors[3] = "Green"
correctColors[4] = "Blue"
correctColors[5] = "Indigo"
correctColors[6] = "Violet"
print("Hello and welcome!")
print("Instruction: Type each color with the first letter in CAPITAL and do not put spaces before or after the word:")
for i in range(0, 6 + 1, 1):
    print("Please enter color " + str(i + 1) + " of the rainbow:")
    rainbowColors[i] = input()
    if rainbowColors[i] == correctColors[i]:
        print("Correct!")
    else:
        i = -1
        print("Wrong color input!")
print("Great! Now you know the colors of the rainbow!")
