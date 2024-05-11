class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("name: {}, age: {}".format(self.name, self.age))
