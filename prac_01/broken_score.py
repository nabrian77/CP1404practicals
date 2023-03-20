"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
'''
get score 
if score < 0:
print invalid score
else
if score > 100:
print invalid score
elif score > 90:
print excellent
elif score > 50:
print passable
else:
bad
'''

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    else:
        print("Bad")