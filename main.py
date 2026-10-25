"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost) / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    cost_for_cs1430 = cost_per_credit(annual_cost, credits) * CS1430_CREDITS
    return cost_for_cs1430 / CS1430_MEETINGS_PER_SEMESTER


def cost_of_skipped_classes(annual_cost, credits, classes_skipped):
    """Give back the cost of the CS 1430 classes skipped."""
    return cost_per_class(annual_cost, credits) * classes_skipped


# ---- PROGRAM ----

def main():
    annual_cost = float(input("Enter the total college cost for one year: "))
    credits = int(input("Enter the credits taken this semester: "))

    while True:
        print()
        print("Cost of College Menu")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per class day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("6. Total cost of skipped classes")
        print("7. Compare cost per credit")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice.upper() == "Q":
            break

        if choice == "1":
            amount = cost_per_semester(annual_cost)
            print(f"Cost per semester: ${amount:,.2f}")
        elif choice == "2":
            amount = cost_per_month(annual_cost)
            print(f"Cost per month: ${amount:,.2f}")
        elif choice == "3":
            amount = cost_per_day(annual_cost)
            print(f"Cost per class day: ${amount:,.2f}")
        elif choice == "4":
            amount = cost_per_credit(annual_cost, credits)
            print(f"Cost per credit: ${amount:,.2f}")
        elif choice == "5":
            amount = cost_per_class(annual_cost, credits)
            print(f"Cost per class: ${amount:,.2f}")
        elif choice == "6":
            classes_skipped = int(input("How many classes did you skip or plan to skip? "))
            amount = cost_of_skipped_classes(annual_cost, credits, classes_skipped)
            print(f"Total cost of skipped classes: ${amount:,.2f}")
        elif choice == "7":
            current_cost = cost_per_credit(annual_cost, credits)
            cost_at_12_credits = cost_per_credit(annual_cost, 12)
            cost_at_18_credits = cost_per_credit(annual_cost, 18)

            if credits < 12:
                print(f"Cost per credit at {credits} credits (current): ${current_cost:,.2f}")
                print(f"Cost per credit if you took 12 credits: ${cost_at_12_credits:,.2f}")
                print(f"Cost per credit if you took 18 credits: ${cost_at_18_credits:,.2f}")
            elif credits == 12:
                print(f"Cost per credit if you took 12 credits: ${current_cost:,.2f}")
                print(f"Cost per credit if you took 18 credits: ${cost_at_18_credits:,.2f}")
            elif credits < 18:
                print(f"Cost per credit if you took 12 credits: ${cost_at_12_credits:,.2f}")
                print(f"Cost per credit at {credits} credits (current): ${current_cost:,.2f}")
                print(f"Cost per credit if you took 18 credits: ${cost_at_18_credits:,.2f}")
            elif credits == 18:
                print(f"Cost per credit if you took 12 credits: ${cost_at_12_credits:,.2f}")
                print(f"Cost per credit at 18 credits (current): ${current_cost:,.2f}")
            else:
                print(f"Cost per credit if you took 12 credits: ${cost_at_12_credits:,.2f}")
                print(f"Cost per credit if you took 18 credits: ${cost_at_18_credits:,.2f}")
                print(f"Cost per credit at {credits} credits (current): ${current_cost:,.2f}")
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7, or Q.")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
