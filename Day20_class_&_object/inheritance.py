class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
        self.skill = []

    def person_info(self):
        return (f"Name : {self.name}\nAge : {self.age}\nCity : {self.city}")

    def add_skill(self,skill):
        self.skill.append(skill)

class student(Person):
    pass

s1 = student('akash',20,"india")
s1.add_skill('C++')
s1.add_skill("python")
print(s1.person_info())
print(f"Skills : {s1.skill}")

# output <--
# Name : akash
# Age : 20
# City : india
# Skills : ['C++', 'python']