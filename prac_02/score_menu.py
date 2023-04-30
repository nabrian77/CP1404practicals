def main():
    score = int(input("Enter your score: "))
    while 0 > score or 100 < score:
        print("Invalid score")
        score = int(input("Enter your score: "))
    print("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
    user_choice = str(input("Enter your choice from the menu: ")).upper()
    while user_choice != "Q":
        if user_choice == "G":
            score = int(input("Enter your score: "))
        elif user_choice == "P":
            final_result = score_result(score)
            print(final_result)
        elif user_choice == "S":
            for i in range(score):
                print("*", end=' ')
        print("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
        user_choice = str(input("Enter your choice from the menu: ")).upper()
    print("Farewell")


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
