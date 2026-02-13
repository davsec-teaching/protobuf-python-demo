# Generated with Cursor assistance

# Method to create a Person class using MetaClass
# Person class will have attributes: user_name, favourite_number, interests
# The class will also have a method to display the person's information
def make_person_class():
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

    attrs = {
        "__slots__": ("name", "age"),
        "__init__": __init__,
        "__repr__": __repr__,
    }
    return type("Person", (), attrs)

Person = make_person_class()

p = Person("Tapti", 10)
print(p)           # Person(name='Tapti', age=10)
print(type(p))     # <class '__main__.Person'>
