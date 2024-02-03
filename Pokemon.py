class Pokemon:
    def __init__(self, name, pok_type, hp, attack, defense, height, weight, moves):
        self.name = name
        self.pok_type = pok_type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.height = height
        self.weight = weight
        self.moves = moves.copy()
    
    # Creating getters and setters
    
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name
    
    def get_type(self):
        return self.pok_type
    
    def set_type(self, value):
        self.pok_type = value
        
    def get_hp(self):
        return self.hp

    def set_hp(self, value):
        self.hp = value

    def get_attack(self):
        return self.attack
    
    def attack(self, value):
        self.attack = value
        
    def get_defense(self):
        return self.defense

    def defense(self, value):
        self.defense = value
    
    def get_height(self):
        return self.height
    
    def height(self, value):
        self.height = value

    def get_weight(self):
        return self.weight
    
    
    def weight(self, value):
        self.weight = value
    
    def get_moves(self):
        return self.moves
    
    def moves(self, value):
        self.moves = value.copy()

    # def check_type(self, pokemon):
    #     if self.get_type() == pokemon.get_type():
    #         return True
    #     else:
    #         return False 
    
    
    # Displaying  the pokemon information
    def  display_info(self):
        print("Name: ", self.name)
        print("Type: ", self.pok_type)
        print("HP: ", self.hp)
        print("Attack: ", self.attack)
        print("Defense: ", self.defense)
        print("Height:  ", self.height)
        print("Weight: ", self.weight)
        print("Moves: [", end ='')
        last_item = self.moves[-1]  # Get the last item of the list
        for x in (self.moves):
            if x == last_item:
                print(x, end='')
            else:
                print(x, end=', ')
        print("]")  
                    
