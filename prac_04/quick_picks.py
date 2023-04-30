import random

min_num = 1
max_num = 45
nums_per_line = 6

picks_number = int(input("How many quick picks? "))

for i in range(picks_number):
    quick_picks = []
    for j in range(nums_per_line):
        number = random.randint(min_num, max_num)
        quick_picks.append(number)
    quick_picks.sort()
    print(" ".join("{:2}".format(number) for number in quick_picks))



