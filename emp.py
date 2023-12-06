"""
@Author: Divyansh Babu

@Date: 2021-12-06 17:06

@Last Modified by: Divyansh Babu

@Last Modified time: 2021-12-06 16:06

@Title : Employee Wage Computation Problem.
"""
import random


class Employee:
    def __init__(self, emp_name, wage_per_hours, max_working_day, max_working_hours):
        self.wage_per_hrs = wage_per_hours
        self.max_working_days = max_working_day
        self.max_working_hrs = max_working_hours
        self.employee_name = emp_name
        self.total_wage = 0

    def employee_wage_implementation(self):
        """
        Description: implementation of Employee Wage Computation Problem.

        Parameter: None

        Return:None
        """
        # print("Welcome to Employee Wage Computation Program on Master Branch")
        emp_working_hrs = 0
        emp_working_days = 0
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
            self.total_wage += working_hours * self.wage_per_hrs
            emp_working_days += 1
        # print(f"Max working Days: {emp_working_days}")
        # print(f"Total working hours of an employee is: {emp_working_hrs}")
        # print(f"Total working days of an employee is: {self.total_wage}")


class Company:
    def __init__(self, company_name):
        self.comp_name = company_name
        self.employee_dict = {}

    def add_employee(self, employee_obj: Employee):
        self.employee_dict.update({employee_obj.employee_name: employee_obj})

    def employee_details(self):
        for key, value in self.employee_dict.items():
            print(f"Name: {key} Total Wage: {value.total_wage} Company Name: {self.comp_name} ")

    def get_employee(self, employee_name):
        emp: Employee = self.employee_dict.get(employee_name)
        print("Employee is fetched!!")

    def update_employee(self, employee_name):
        employee_obj: Employee = self.employee_dict.get(employee_name)
        if employee_obj:
            employee_obj.employee_wage_implementation()
            self.employee_dict.update({employee_name: employee_obj})
        else:
            print("Employee is not Found!!")

    def delete_employee(self, employee_name):
        employee_boj: Employee = self.employee_dict.get(employee_name)
        if employee_boj:
            self.employee_dict.pop(employee_name)
            print("deleted!!")
        else:
            print("Employee is not Found!!")


def main():
    # print(f"{employee_obj.total_wage}")
    company_obj = Company('A')

    while True:
        print(
            "choice 1 for add\nchoice 2 for all details of employee\nchoice 3 to get an item from dictionary\nchoice 4"
            " for update an item of dictionary\nchoice 5 for delete an item of dictionary\nchoice 6 for exit")
        user_choice = int(input("Enter your choice: "))
        match user_choice:
            case 1:
                employee_name = input("Enter the emp name: ")
                wage_per_hrs = int(input("Enter wage per Hours: "))
                max_working_days = int(input("Enter Max working Days: "))
                max_working_hrs = int(input("Enter Max working Hours: "))
                employee_obj = Employee(employee_name, wage_per_hrs, max_working_days, max_working_hrs)
                employee_obj.employee_wage_implementation()
                company_obj.add_employee(employee_obj)  # to add an item to dictionary
            case 2:
                company_obj.employee_details()  # for all details of employee
            case 3:
                employee_name = input("Enter the emp name: ")
                wage_per_hrs = int(input("Enter wage per Hours: "))
                max_working_days = int(input("Enter Max working Days: "))
                max_working_hrs = int(input("Enter Max working Hours: "))
                employee_obj = Employee(employee_name, wage_per_hrs, max_working_days, max_working_hrs)
                company_obj.get_employee(employee_obj)  # to get an item from dictionary
            case 4:
                employee_name = input("Enter the emp name: ")
                company_obj.update_employee(employee_name)  # for update an item of dictionary
            case 5:
                employee_name = input("Enter the emp name: ")
                company_obj.delete_employee(employee_name)  # for delete an item of dictionary
            case 6:
                break


if __name__ == '__main__':
    main()
