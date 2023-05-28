class Skill:
    skills = []

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        cls.skills.append(obj)
        return obj

    def __init__(self, name):
        self.dict_criterions = {}
        self.name = name

    def add(self, new_criterion, flag=False):
        self.dict_criterions[new_criterion] = flag

    def progress_percent(self):
        all_diagram = len(self.dict_criterions)
        fulled = len(list(filter(lambda x: x, self.dict_criterions.values())))
        fulled = fulled / all_diagram

        return int(fulled * 100)

    def show_criterions(self):
        for i, j in self.dict_criterions.items():
            print(f'{i}: {j}')

    def change_status_of_criterion(self, name_criterion, flag):
        self.dict_criterions[name_criterion] = flag


english = Skill('Английский')

english.add('Present Simple', True)
english.add('Present Continuous', True)
english.add('Present Perfect Continuous')
english.add('Present Future Continuous')

python = Skill('Python')

python.add('Числа и операции над ними', True)
python.add('Переменные', True)
python.add('Функции input() и print()', True)
python.add('Декораторы')
python.add('Циклы (while, for, do while', True)
python.add("Регулярные выражения")

oop = Skill('ООП')

oop.add('Метод __init__(self)', True)
oop.add('Метод __new__(cls)', True)
oop.add('Режимы доступа')
oop.add('Магические методы классов')
oop.add('Наследование')
oop.add('Полиморфизм')
oop.add('Исключения')
oop.add('Менеджеры контекста')

dream = Skill('Сон 12 часов\nв сутки')
dream.add('Сонливость', True)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

skills = [i.name + f'\n({i.progress_percent()}%)' for i in Skill.skills]
counts = [i.progress_percent() for i in Skill.skills]

bar_colors = list(map(lambda x: 'tab:green' if x==100 else 'firebrick', counts))
ax.axis([None, None, 0, 100])

# str_label = '\n\n'.join(english.dict_criterions.keys()) # легенда, отображающая элементы навыка
ax.bar(skills, counts, color=bar_colors, align='center')

ax.set_ylabel('Прогресс изучения, %')
ax.set_title('Диаграммы навыков')
# ax.legend(title='Fruit color')

# ax.legend()

plt.show()
