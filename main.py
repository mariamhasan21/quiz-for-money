#this is done on 9th September, 2024
from typing import final
q = {
    "Capital of BD": "Dhaka",
     "Capital of India": "Delhi",
     "Capital of Pakistan": "Lahore"
     }
op = [
    ["Dhaka", "Comilla", "Sylhet"],
    ["Mumbai", "Delhi", "Haryana"],
    ["Lahore", "Karachi", "Multan"]
]
l = len(q)
i = 0
score = 0
for key, value in q.items():
    print(key)
    for j in range(len(op[i])):
        print(f"{j+1}. {op[i] [j]}")
    ans = input("Enter your answer (1, 2, or 3): ")
    if int(ans) == 1:
        if op[i] [0] == value:
            score += 1
            print("Fantastic! ")
        else:
            print("Dumb asf")
    elif int(ans) == 2:
        if op[i] [1] == 2:
            score += 1
            print("Another correct")
        else:
            print("Fuck you")
    elif int (ans) == 1:
        if op[i] == value:
            score += 1
            print("You are crushing it! ")
    i += 1
# Calculate the final score and award money
f = int(score/l * 1000)
print("Congratulations, you received", f, "taka")
