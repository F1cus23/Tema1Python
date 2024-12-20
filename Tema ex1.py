from employee import Employee  


class Manager(Employee):
    mgr_count = 0  

    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)  
        self.department = "F25_" + department
        Manager.mgr_count += 1  

    def display_employee(self):
        #X%3 = 1, afisam doar salariul
        print(f"Salary: {self.salary}")


managers = []
for i in range(4): 
    manager = Manager(f"Manager_{i+1}", 5000 + i * 1000, f"Department_{i+1}")
    managers.append(manager)

employee = Employee("Alex", 4000)


print(" Manager Objects ")
for manager in managers:
    manager.display_employee()

print("\n Employee Object ")
employee.display_employee()

print("\n  Count of Objects ")
print(f"Employee Count: {Employee.empCount}")
print(f"Manager Count: {Manager.mgr_count}")
