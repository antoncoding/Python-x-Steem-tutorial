class Person:
    def __init__(self, _name, _height, _weight, _gender):
        self.name = _name
        self.height = _height
        self.weight = _weight
        self.gender = _gender
        self.count_update = 0

    def get_bmi(self):
        bmi = self.weight/(self.height * self.height)
        return bmi

    def rename(self, new_name,):
        self.name = new_name
        self.count_update += 1




me = Person('Anton',1.75, 65, 'Male')
print(me.name)
me.rename('Antoooon')
me.rename('Antonazzo')
print('========= After Update ===========')
print(me.name)
print(me.count_update)
