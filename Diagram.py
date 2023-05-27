class Diagram:

    def __init__(self):
        self.dict_criterions = {}

    def add(self, new_criterion, flag=False):
        self.dict_criterions[new_criterion] = flag

    def show_diagram(self):
        pass

    def show_criterions(self):
        for i, j in self.dict_criterions.items():
            print(f'{i}: {j}')

    def change_status_of_criterion(self, name_criterion, flag):
        self.dict_criterions[name_criterion] = flag


english_Diagram = Diagram()

english_Diagram.add('Present Simple', True)
english_Diagram.add('Present Continuous')
english_Diagram.add('Present Perfect Continuous')

english_Diagram.show_criterions()

english_Diagram.change_status_of_criterion('Present Continuous', True)
print()
english_Diagram.show_criterions()