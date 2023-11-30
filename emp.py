"""
@Author: Divyansh Babu

@Date: 2021-11-29 16:06

@Last Modified by: Divyansh Babu

@Last Modified time: 2021-11-29 16:06

@Title : Employee Wage Computation Problem.
"""
import random


def employee_wage_implementation():
    """
    Description: implementation of Employee Wage Computation Problem.

    Parameter: None

    Return:None
    """
    print("Welcome to Employee Wage Computation Program on Master Branch")
    # NOT_PRESENT = 0
    # PART_TIME = 1
    # FULL_TIME = 2
    WAGE_PER_HR = 20
    WORKING_DAYS = 20
    MAX_WORKING_DAYS = 20
    MAX_WORKING_HRS = 100

    totalWage = 0
    if MAX_WORKING_DAYS <= 20 and MAX_WORKING_HRS <= 100:
        for day in range(0, (MAX_WORKING_DAYS or MAX_WORKING_HRS)):
            empType = random.randint(0, 2)
            workingHours = 0
            match empType:
                case 0:
                    print("Employee is not present")
                case 1:
                    print("Employee is present and working Part time")
                    workingHours = 4
                case 2:
                    print("Employee is present and working Full time")
                    workingHours = 8

            wage = workingHours * WAGE_PER_HR
            print("Day", day + 1, "wage is", wage)
            totalWage += wage
        print("Total wages of a month is: ", totalWage)
    else:
        print("Max working days or Max working hours is more the 20,100 respectively")


if __name__ == '__main__':
    employee_wage_implementation()
