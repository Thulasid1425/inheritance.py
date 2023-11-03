#hierarchal
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
    def salcal(self) -> str:
         return f'sal cal per year: {12 * self._sal}'

class contactEmployee(Employee):
       _hr_pay:int = 300
       def salcal(self, hrs: int) -> str:
           return f'sal cal for {hrs} hrs: {self._hr_pay * hrs}'
pemp =perminentEmployee()
pemp.setName(fName="Thulasi", sName="D", lName="hari")
pemp.addAddress("Tirupati")
print(pemp.getFullName())
print(pemp.getAddress())
print(pemp.salcal())

cemp = contactEmployee()
cemp.setName(fName="tendu", sName="d", lName="seenu")
cemp.addAddress("Puttur")
print(cemp.getFullName())
print(cemp.getAddress())
print(cemp.salcal(20))
