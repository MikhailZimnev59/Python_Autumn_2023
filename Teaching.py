class Data:
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]
class Teacher:
    def __init__(self):
        self.work = 0
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1
class Pupil:
    def __init__(self):
        self.knowledge = []
    def take(self, info):
        self.knowledge.append(info)
lesson = Data('class', 'object', 'inheritance', 'polymorphism', 'encapsulation')

marIvanna = Teacher()
vasya = Pupil()
petya = Pupil()

marIvanna.teach(lesson[2], vasya, petya)
marIvanna.teach(lesson[0], petya)

print(vasya.knowledge)
print(petya.knowledge)
