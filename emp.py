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
    WAGE_PER_HR = 20
    MAX_WORKING_DAYS = 20
    MAX_WORKING_HRS = 100
    emp_working_hrs = 0
    emp_working_days = 0
    total_wage = 0
    while emp_working_hrs < MAX_WORKING_HRS and emp_working_days < MAX_WORKING_DAYS:
        empType = random.randint(0, 2)
        working_hours = 0
        match empType:
            case 0:
                working_hours = 0
                # print("Employee is not present")
            case 1:
                # print("Employee is present and working Part time")
                working_hours = 4
            case 2:
                # print("Employee is present and working Full time")
                working_hours = 8
        emp_working_hrs += working_hours
        total_wage += working_hours * WAGE_PER_HR
        emp_working_days += 1
    print(emp_working_days)
    print(f"Total working hours of an employee is: {emp_working_hrs}")
    print(f"Total working days of an employee is: {total_wage}")


if __name__ == '__main__':
    employee_wage_implementation()
