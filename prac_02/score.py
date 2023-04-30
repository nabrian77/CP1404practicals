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

def main():
    score = float(input("Enter score: "))
    final_result = score_result(score)
    print(final_result)
    import random
    random_result = score_result(random.randint(1, 101))
    print(random_result)


def score_result(user_score):
    if user_score < 0:
        score_grade = "Invalid score"
        return score_grade
    else:
        if user_score > 100:
            score_grade = "Invalid score"
            return score_grade
        elif user_score > 90:
            score_grade = "Excellent"
            return score_grade
        elif user_score > 50:
            score_grade = "Passable"
            return score_grade
        else:
            score_grade = "Bad"
            return score_grade


main()


