"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months_input = int(input("How many months? "))
    # This variable stores the input that is user's number of months.

    for month in range(1, months_input + 1):
        income = float(input(f"Enter income for month {month}:"))
        incomes.append(income)

    report_output(incomes, months_input)


def report_output(incomes, months_input):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months_input + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
# This function will print the report based on user's months and income per month.


main()
