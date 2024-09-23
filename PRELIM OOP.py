class AnimeCharacter():
    def __init__(self, username, power_level, special_move):
        self.username = username
        self.power_level = power_level
        self.special_move = special_move

    def introduce(self):
            print(f"Introducing {self.username}: \nCharacter name:{self.username} \nPower Level:{self.power_level} and \nSpecial Move:{self.special_move}\n")
    def __str__(self):
         return f"Character name:{self.username} \nPower Level:{self.power_level}"

class SuperSaiyan(AnimeCharacter):
    def __init__(self, username, power_level, special_move, transformation_stage):
        super().__init__(username, power_level, special_move)
        self.transformation_stage = transformation_stage
    def transform(self):
        self.power_level = self.transformation_stage * 10000 + int(self.power_level)

mainCharac = AnimeCharacter("Naruto","5000","Sage Art Jutsu")
sideCharac = SuperSaiyan("Goku","9000","Supersaiyan 3",3)

mainCharac.introduce()
sideCharac.introduce()

sideCharac.transform()
sideCharac.introduce()