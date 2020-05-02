# Parent Class i.e Employee class
class Employee:
    def __init__(self, employeeName, employeeNumber):
        self.employeeName = employeeName
        self.employeeNumber = employeeNumber

    def getEmployeeName(self):
        return self.employeeName
    
    def setEmployeeName(self, employeeName):
        self.employeeName = employeeName
    
    def getEmployeeNumber(self):
        return self.employeeNumber

    def setEmployeeNumber(self, employeeNumber):
        self.employeeNumber = employeeNumber

    
#Subclass i.e ProductionWorker class
class ProductionWorker(Employee):
    def __init__(self, employeeName, employeeNumber, shiftNumbered, hourlyPayRate):
        self.shiftNumbered = shiftNumbered
        self.hourlyPayRate = hourlyPayRate
        Employee.__init__(self, employeeName, employeeName)

    def getShiftNumbered(self):
        return self.shiftNumbered
    
    def setShiftNmubered(self, shiftNumbered):
        self.shiftNumbered = shiftNumbered

    def getHourlyPayRate(self):
        return self.hourlyPayRate

    def setHourlyPayRate(self, hourlyPayRate):
        self.hourlyPayRate = hourlyPayRate
    
