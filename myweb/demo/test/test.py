Person = type("Person", (object, ), {"live": True, "name": 'crisimple'})
print(type(Person))
p1 = Person()
print(type(p1))