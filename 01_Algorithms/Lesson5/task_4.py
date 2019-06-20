from collections import namedtuple

hero_1 = ('Vasya', 'Man', 100, 250, 50)
print(hero_1[4])

Person = namedtuple('Person', 'name race health mana armor')
Person = namedtuple('Person', 'name, race, health, mana, armor')
hero_2 = Person('Vasya', 'Man', 100, 250, 50)
hero_3 = Person('Ivan', 'Man', 2500, 250, 50)
hero_4 = Person(tuple([1, 2, 3, 5]), 'Man', 2500, 250, 50)
# hero_4.name.append(555)
print(hero_4)


print(hero_2.name)
print(hero_3.mana)
print(hero_2)

cord = ['x', 'y', 'z']
Point = namedtuple('Point', cord)
p1 = Point(2, 3, 4)
print(p1)
# p1.x = 22
p1 = p1._replace(x=22)
print(p1)
p2 = p1._replace(z=0)
print(p1, p2, sep='\n')

print(p2._fields)
print(p1.x + p2.x)



