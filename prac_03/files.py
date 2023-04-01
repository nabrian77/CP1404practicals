# Question 1
name = input("Enter your name: ")
name_file = "name.txt"
name_file_print = open(name_file, 'w')
print(name, file=name_file_print)
name_file_print.close()

# Question 2
open_file = open(name_file, 'r')
written_name = open_file.read().strip()
open_file.close()
print("Your name is", written_name)

# Question 3
number_file = "numbers.txt"
read_number = open(number_file, "r")
first_line = int(read_number.readline())
second_line = int(read_number.readline())
read_number.close()
print(first_line + second_line)

# Question 4
total_number = 0
read_number2 = open("numbers.txt", "r")
for i in read_number2:
    number = int(i)
    total_number += number
read_number2.close()
print(total_number)
