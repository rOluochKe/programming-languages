"""
Title: Staff Tracking System

We can create a system for checking the different roles within a company

1. Start by defining the base class Employee with the __init__() method. This method should initialize the name and employee_id attributes.

2. Implement the __str__() method in the Employee class. It should return a formatted string that represents the employee's name and ID.

3. Define the __eq__() method in the Employee class. This method compares the employee's employee_id with another object of the same class. If they match, return True; otherwise, return False.

4. create a derived class Manager that inherits from the Employee class. Add an additional attribute, department, in the __init__() method of the Manager class. Use super() to call the base class's __init__() method and pass the required arguments.

5. Implement the __str__() method in the Manager class to return a formatted string that includes the manager's name, ID, and department.

6. Define the __eq__() method in the Manager class. Similar to the Employee class, compare the manager's employee_id with another object of the same class.

7. Create another derived class Staff that also inherits from the Employee class. In the __init__() method of the Staff class, add an additional attribute, role.

8. Implement the __str__() method in the Staff class to return a formatted string representing the staff member's name, ID, and role.

9. Define the __eq__() method in the Staff class to compare the staff member's employee_id with another object of the same class.

10. Finally, in the Employee, Manager, and Staff classes, implement the __add__() method. For the Employee class, simply return an error message as adding two employees is not meaningful. In the Manager class, check if the other object is also a Manager and if their departments match. If the conditions are met, create a new Manager object with the combined names, a unique ID of -1, and the shared department. Otherwise, return an error message stating that addition cannot be performed between managers from different departments. For the Staff class, return an error message as adding staff members is not allowed.

11. create instances of Employee, Manager, and Staff objects with different attributes.

Test the code by printing the objects using print(), comparing their equality using the == operator, and performing addition operations using the + operator.
"""


class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def __str__(self):
        return f"Employee: {self.name}, (ID: {self.employee_id})"

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.employee_id == other.employee_id
        return False

    def __add__(self, other):
        raise ValueError("Can not add employees!")


class Manager(Employee):
    def __init__(self, name, employee_id, department):
        Employee.__init__(self, name, employee_id)
        self.department = department

    def __str__(self):
        return f"Name: {self.name}, (ID: {self.employee_id}, Dept: {self.department})"

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.employee_id == other.employee_id
        return False

    def __add__(self, other):
        raise ValueError("Can not add Manager!")


class Staff(Employee):
    def __init__(self, name, employee_id, role):
        Employee.__init__(self, name, employee_id)
        self.role = role

    def __str__(self):
        return f"Name: {self.name}, (ID: {self.employee_id}, Position: {self.role})"

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.employee_id == other.employee_id
        return False

    def __add__(self, other):
        raise ValueError("Can not add Staff Members!")


employee1 = Employee("John Doe", 1)
employee2 = Employee("Jane Doe", 2)

manager1 = Manager("Bruce Bruce", 9, "marketing")
manager2 = Manager("Sarah Jane", 8, "sales")

staff1 = Staff("Mark Jones", 12, "Marketing Ops Dev")
staff2 = Staff("Emily Davis", 14, "Software Engineer")


print(employee1)
print(manager1)
print(staff1)

print(employee1 == employee2)
print(staff1 == staff2)

print(manager1 + manager2)
