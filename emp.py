"""
@Author: Divyansh Babu

@Date: 2021-11-28 13:06

@Last Modified by: Divyansh Babu

@Last Modified time: 2021-11-28 13:06

@Title : Employee Wage Computation Problem.
"""
import random


def check_attendence():
    """
    Description: implementation of Employee Wage Computation Problem.

    Parameter: None

    Return:None
    """
    print("Welcome to Employee Wage Computation Program on Master Branch")

    FULL_TIME = 1
    WAGE_PER_HR = 20
    empType = random.randint(0, 100) % 2
    workingHours = 0
    if empType == FULL_TIME:
        print("Employee is present")
        workingHours = 8
    else:
        print("Employee is not present")
    wage = workingHours * WAGE_PER_HR
    print("Employee Daily Wage is: ", wage)


if __name__ == '__main__':
    check_attendence()
