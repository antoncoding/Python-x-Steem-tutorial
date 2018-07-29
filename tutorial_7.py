class Person:
    def __init__(self, _name, _height, _weight, _gender):
        self.name = _name
        self.height = _height
        self.weight = _weight
        self.gender = _gender

    def get_bmi(self):
        bmi = self.weight/(self.height * self.height)
        return bmi

me = Person('Anton',1.75, 65, 'Male')
print(me.name)
print(me.height)

print(me.get_bmi())
