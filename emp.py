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
    # PART_TIME = 1
    # FULL_TIME = 2
    WAGE_PER_HR = 20
    WORKING_DAYS = 20
    totalWage = 0
    for day in range(1, WORKING_DAYS + 1):

        empType = random.randint(0, 2)
        workingHours = 0
        match empType:
            case 0:
                print("Employee is present Full time")
                workingHours = 8
            case 1:
                print("Employee is working Part time")
                workingHours = 4
            case 2:
                print("Employee is not present")
        wage = workingHours * WAGE_PER_HR
        print("Day", day, "wage is", wage)
        totalWage += wage
    print("Total wages of a month is: ", totalWage)


if __name__ == '__main__':
    employee_wage_implementation()
