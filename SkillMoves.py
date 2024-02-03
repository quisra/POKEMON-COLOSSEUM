class SkillMoves:
    def __init__(self, name,type,category,contest,pp,power,accuracy):
        self._name = name
        self._move_type= type
        self._category = category
        self._contest = contest
        self._pp = pp
        self._power = power
        self._accuracy = accuracy
        
    def get_name(self):
        return self._name

    def get_move_type(self):
        return self._move_type

    def get_category(self):
        return self._category

    def get_contest(self):
        return self._contest

    def get_PP(self):
        return self._pp

    def get_power(self):
        return self._power

    def get_accuracy(self):
        return self._accuracy

    def set_name(self, value):
        self._name = value

    def set_move_type(self, value):
        self._move_type = value

    def set_category(self, value):
        self._category = value

    def set_contest(self, value):
        self._contest = value

    def set_PP(self, value):
        self._pp = value

    def set_power(self, value):
        self._power = value

    def set_accuracy(self, value):
        self._accuracy = value
        
    # self, name,type,category,contest,pp,power,accuracy
    def displayMoves_info(self):
        print("Name: ", self._name)
        print("Type: ", self._move_type)
        print("Category: ",  self._category)
        print("Contest:  ", self._contest)
        print("Power Points (PP): ", self.getPP())
        print("Power: ", self._power)
        print("Accuracy: ", self._accuracy)