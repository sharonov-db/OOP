class Student:

    def __init__(self, name = 'Ivan', age = 18, group_number = '10A'):
        self.name = name
        self.age = age
        self.group_number = group_number

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_group_number(self):
        return self.group_number

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_group_number(self, group_number):
        self.group_number = group_number


