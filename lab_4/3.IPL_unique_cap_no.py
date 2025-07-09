players = {}
class Player:
    def __init__(self, cap, name, team, skill):
        self.cap = cap
        self.name = name
        self.team = team
        self.skill = skill
    def __str__(self):
        return f"Cap: {self.cap}, Name: {self.name}, Team: {self.team}, Skill: {self.skill}"
n = int(input("Enter The Number of Players: "))

for i in range(n):
    cap = input(f"Enter Cap Number for Player {i+1}: ")
    name = input("Enter Player Name: ")
    team = input("Enter Player Team: ")
    skill = input("Enter Player Skill: ")
    players[cap] = Player(cap, name, team, skill)
print("\nPlayer Details:")
for cap, player in players.items():
    print(player)
