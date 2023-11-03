class Address:
    _address: str = ""
    def addAddress(self, address):
        self._address = address
    def getAddress(self):

        return self._address

class Employee(Address):
    _firstName: str = ""
    _lastName: str = ""
    _sunName: str = ""
    def setName(self, fName: str, lName: str, sName: str = ""):
        self._firstName = fName
        self._sunName = sName
        self._lastName = lName

    def _nameFormat(self):
        return f'{self._sunName} {self._firstName} {self._lastName}'

    def getFullName(self):
        return self._nameFormat()

class perminentEmployee(Employee):
    _sal : int = 30000
    def salcal(self) -> float:
         return 12 * self._sal
emp =perminentEmployee()
emp.setName(fName="Thulasi", sName="D", lName="hari")
emp.addAddress("Tirupati")
print(emp.getFullName())
print(emp.getAddress())

