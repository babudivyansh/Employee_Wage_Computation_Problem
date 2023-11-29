"""
@Author: Divyansh Babu

@Date: 2021-11-29 13:26

@Last Modified by: Divyansh Babu

@Last Modified time: 2021-11-29 16:47

@Title : Employee Wage Computation Problem.
"""
import random


def calculate_wage():
    """
    Description: implementation of Employee Wage Computation Problem.

    Parameter: None

    Return:None
    """
    print("Welcome to Employee Wage Computation Program on Master Branch")

    FULL_TIME = 1
    WAGE_PER_HR = 20
    empType = random.randint(0, 1)
    workingHours = 0
    if empType == FULL_TIME:
        print("Employee is present")
        workingHours = 8
    else:
        print("Employee is not present")
    wage = workingHours * WAGE_PER_HR
    print("Employee Daily Wage is: ", wage)


if __name__ == '__main__':
    calculate_wage()
