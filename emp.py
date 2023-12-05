"""
@Author: Divyansh Babu

@Date: 2021-12-05 14:30

@Last Modified by: Divyansh Babu

@Last Modified time: 2021-12-05 14:30

@Title : Employee Wage Computation Problem.
"""
import random


class EmployeeWageProblem:
    def __init__(self):
        self.wage_per_hrs = int(input("Enter wage per Hours: "))
        self.max_working_days = int(input("Enter Max working Days: "))
        self.max_working_hrs = int(input("Enter Max working Hours: "))

    def employee_wage_implementation(self):
        """
        Description: implementation of Employee Wage Computation Problem.

        Parameter: None

        Return:None
        """
        print("Welcome to Employee Wage Computation Program on Master Branch")
        emp_working_hrs = 0
        emp_working_days = 0
        total_wage = 0
        while emp_working_hrs < self.max_working_hrs and emp_working_days < self.max_working_days:
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
            total_wage += working_hours * self.wage_per_hrs
            emp_working_days += 1
        print(f"Max working Days: {emp_working_days}")
        print(f"Total working hours of an employee is: {emp_working_hrs}")
        print(f"Total working days of an employee is: {total_wage}")


if __name__ == '__main__':
    employee_wage_problem = EmployeeWageProblem()
    employee_wage_problem.employee_wage_implementation()
