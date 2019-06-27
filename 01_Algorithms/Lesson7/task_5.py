class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'name={self.name}; age={self.age}'


p_1 = Person('Sergey', 37)
p_2 = Person('Agrafena', 23)
p_3 = Person('Violetta', 18)
p_4 = Person('Nicolay', 18)

people = [p_1, p_2, p_3, p_4]
print(people)


def by_name(obj):
    return obj.name


a = sorted(people, key=by_name)

print(a)

# best practic
from operator import attrgetter

b = sorted(people, key=attrgetter('name'))
print(b)
c = sorted(b, key=attrgetter('age'))
print(c)
