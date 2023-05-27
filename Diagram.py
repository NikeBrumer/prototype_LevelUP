class Diagram:

    def __init__(self, name):
        self.dict_criterions = {}
        self.name = name

    def add(self, new_criterion, flag=False):
        self.dict_criterions[new_criterion] = flag

    def show_diagram(self):
        all_diagram = len(self.dict_criterions)
        #lst = list(self.dict_criterions.values())
        fulled = len(list(filter(lambda x: x, self.dict_criterions.values())))
        fulled = fulled/all_diagram
        print(f'{"|" * int(fulled*100)}{"-"*int((1-fulled)*100)}')

    def show_criterions(self):
        for i, j in self.dict_criterions.items():
            print(f'{i}: {j}')

    def change_status_of_criterion(self, name_criterion, flag):
        self.dict_criterions[name_criterion] = flag


english_Diagram = Diagram('English')

english_Diagram.add('Present Simple', True)
english_Diagram.add('Present Continuous')
english_Diagram.add('Present Perfect Continuous')
print()
print(f'Навык: {english_Diagram.name}')
print()
english_Diagram.show_criterions()
english_Diagram.show_diagram()

english_Diagram.change_status_of_criterion('Present Continuous', True)
print()
english_Diagram.show_criterions()

english_Diagram.show_diagram()