"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
def main():
    sales = float(input("Enter sales amount: "))
    subpar_bonus = 0.1
    metpar_bonus = 0.15
    bonuspar = 1000

    while sales >= 0:
        if sales < bonuspar:
            user_bonus = sales * subpar_bonus
        elif sales >= bonuspar:
            user_bonus = sales * metpar_bonus
        print(user_bonus)
        main()

main()

