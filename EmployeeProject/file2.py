import file1

print("Enter the following details of the employee")
name = input("Enter Employee Name: ")
number = int(input("Enter Employee Number: "))
payRate = int(input("Enter Pay Rate: "))
shiftNumber = int(input("Enter Shift Number: "))

productionWorker = file1.ProductionWorker(name, number, payRate, shiftNumber)

print("Details of Employee: ")
print("Name: ", productionWorker.getEmployeeName())
print("Employee Number: ", productionWorker.getEmployeeNumber())
print("Shift: ", productionWorker.getShiftNumbered())
print("Pay Rate: ", productionWorker.getHourlyPayRate())