import random

class Player():
    def __init__(self):
        # Open the first and last name txt files and get first / last names
        with open("first_names.txt") as f:
            lines = f.readlines()
            first = random.choice(lines).strip("\n") # Strip the first name of any spaces or newlines
            first.strip(" ")
        with open("last_names.txt") as f:
            lines = f.readlines()
            last = random.choice(lines).strip("\n")  # Strip the last name of any spaces or newlines
            last.strip(" ")

        self.name = "".join(first+" "+last)
        self.shooting = random.randint(50,99)
        self.layup = random.randint(50,99)
        self.dunk = random.randint(50,99)
        self.defence = random.randint(50,99)
        self.rebounding = random.randint(50,99)

        self.overall = round((self.shooting+self.layup+self.dunk+self.defence+self.rebounding)/5)

        self.feet = random.randint(5,7)
        self.inches = random.randint(0,11)
        self.height = str(self.feet)+"'"+str(self.inches)+'""'

class Team():
    def __init__(self):
        self.roster = []
        self.name = ""
        self.wins = 0
        self.losses = 0
        self.record = "0-0"

class League():
    def __init__(self):
        self.teams = []

nba = League()

def generate_team(name_index):
    #Create and Name Team
    team = Team()
    for i in range(10):
        team.roster.append(Player())
    with open("nba.txt") as f:
        content = f.readlines()
        team.name = content[name_index]
        team.name = team.name[0:-1]
    team.roster.sort(key=lambda x: x.overall, reverse=True)
    nba.teams.append(team)

def generate_league():
    for i in range(30):
        generate_team(i)

def list_names(league):
    names = []
    for team in league:
        names.append(team.name)
    return names

def list_overall(team):
    names = []
    for player in team:
        names.append(player.name+" ("+str(player.overall)+")")
    return names

def main():
    generate_league()
    for team in nba.teams:
        print(team.name)
        print(list_overall(team.roster))


main()