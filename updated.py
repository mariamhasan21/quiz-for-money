q = { 
    'Question 1: What is the name of the famous cat that accompanied Lewis Carroll on his travels?': 'Dinah',
    'Question 2: In which country is the Colosseum located?':'Italy',
    'Question 3: What is the smallest continent in the world?':'Australia',
    'Question 4: Which fruit is often associated with the color green?': 'Apple',
    'Question 5: What is the name of the largest freshwater lake in the world?':'Lake Baikal'
}

op = [
    ["Cheshire Cat", "Alice", "Dinah", "Tweedledum"],
    ['Italy', 'Greece', 'Spain', 'France'],
    ['Africa', 'Australia', 'Europe', 'Antarctica'],
    ['Apple', 'Banana', 'Grapefruit', 'Watermelon'],
    ['Lake Superior', 'Lake Victoria', 'Lake Baikal', 'Lake Caspian']
]

l = len(q)
i = 0
score = 0

# Loop through each question and its corresponding options
for keys, values in q.items():
    print(keys)  # Print the question
    
    # Display all options
    for j in range(len(op[i])):
        print(f"{j+1}. {op[i][j]}")  # Display options 1 to 4

    # Take the answer input after showing all the options
    ans = input("Enter your answer (1, 2, 3, or 4): ")

    # Check the answer and update the score
    if int(ans) == 1:
        if op[i][0] == values:
            score += 1
            print("Wonderful, Correct answer!")
        else:
            print("Oopsie, wrong answer!")
    elif int(ans) == 2:
        if op[i][1] == values:
            score += 1
            print("Excellent!")
        else:
            print("Oopsie, wrong answer!")
    elif int(ans) == 3:
        if op[i][2] == values:
            score += 1
            print("Marvelous!")
        else:
            print("Oopsie, wrong answer!")
    elif int(ans) == 4:
        if op[i][3] == values:
            score += 1
            print("Great choice!")
        else:
            print("Oopsie, wrong answer!")

    # Move to the next question
    i += 1

# Calculate the final score
f = int(score / l * 100)  # Adjust the score to a percentage
print(f"Congratulations, you received {f} points")
