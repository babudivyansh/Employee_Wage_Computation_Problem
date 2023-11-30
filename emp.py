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
    PART_TIME = 0
    FULL_TIME = 1
    WAGE_PER_HR = 20
    workingHours = 0

    def empType1():
        """Description: implementation to get Employee Type.

           Parameter: None

           Return:Employee Type """
        emp = random.randint(0, 1)
        return emp
def main():
    empType = empType1()
    

    if empType == FULL_TIME:
        print("Employee is present")
        pt_ft_wage = empType1()
        if pt_ft_wage == FULL_TIME:
            print("Employee is present Full time")
            workingHours = 8
        elif pt_ft_wage == PART_TIME:
            print("Employee is working Part time")
            workingHours = 4
    else:
        print("Employee is not present")
    wage = workingHours * WAGE_PER_HR
    print("Employee Daily Wage is: ", wage)


if __name__ == '__main__':
    main()
