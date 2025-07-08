class Person:
    def __init__(self, name_param):
        self.name = name_param
        print("Hello, I', created! ", self, " name : ", self.name)

    def introduce(self):
        print("Hi, My name is ", self.name, ". 😊")

person1 = Person("Coco")
person2 = Person("Momo")

print(person1.name)
person1.introduce()

print(person2.name)
person2.introduce()