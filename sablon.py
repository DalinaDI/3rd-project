class Student:
    def __init__(self, name, adress, phone, course, index_number):
        self._name = name
        self._adress = adress
        self._phone = phone
        self._course = course
        self._index_number = index_number

    def _getInfo(self):
        return f" Student: Name: {self._name}, Adress: {self._adress}, Phone: {self._phone}, Course:{self._course}, Index: {self._index_number}"
    
   
    
student_1 = Student("Dobrescu Dalina", "Brasov, str. Vlahuta", 740505954, "English", 1)
print(student_1._getInfo())

student_2 = Student("Urdea Elena", "Campulung, str. Bratianu", 740505958, "Math", 2)
print(student_2._getInfo())

student_3 = Student("Todoru Andreea", "Bucuresti, str. Narciselor", 74050587, "Physics", 3)
print(student_3._getInfo())
