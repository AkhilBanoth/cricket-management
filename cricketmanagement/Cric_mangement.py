class CricketManagement:
    def __init__(self, player_id, name, age, role, team, jersey_no, bowling_style):
        self.player_id = player_id
        self.name = name
        self.age = age
        self.role = role
        self.team = team
        self.jersey_no =jersey_no
        self.bowling_style = bowling_style

    def display (self):
        print("========================")
        print("player details")
        print("player_id:",self.player_id)
        print("name:",self.name)
        print("age:",self.age)
        print("role:",self.role)
        print("team:",self.team)
        print("jersey_no:",self.jersey_no)
        print("bowling_style:",self.bowling_style)

    def update_wickets(self, wickets):
        self.wickets += wickets
        print ("Wickets updated successfully.")

    def update_matches(self, matches):
        self.matches += matches
        print("Matches updated successfully.")

    def update_team(self, team):
        self.team = team
        print("Team updated successfully.")

    def update_role(self, role):
        self.role = role
        print("Role updated successsfully.")

    def calculate_performance(self):
        if self.runs >= 500:
            return "wowww"
        elif self.runs <= 250:
            return "nice"
        else:
            return "okay"

    def player_summary(self):
        print("===== PLAYER SUMMARY =====")
        print("Player ID:", self.player_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Role:", self.role)
        print("Team:", self.team)
        print("Jersey No:", self.jersey_no)
        print("Bowling Style:", self.bowling_style)
        print("Matches Played:", self.matches_played)
        print("Wickets:", self.wickets)
        print("Performance:", self.calculate_performance())

    def get_runs(self):
        return self.runs

players = []

def add_players():
    print("Enter player details:")
    player_id = int(input("Player_id:"))
    name = input("name:")
    age = int(input("age:"))
    role = input("role:")
    team = input("team:")
    jersey_no = int(input("jersey_no:"))
    bowling_style = input("bowling_style:")

    player = CricketManagement(player_id, name, age, role, team, jersey_no, bowling_style)
    players.append(player)
    print("Player added successfully.")

def view_players():
    if len(players) == 0:
        print("no players found.")
        return

    for player in players:
        player.display()

def serach_player():
    player_id = int(input("enter player id to serach:"))
    for player in players:
        if player.player_id == player_id:
            player.display()
            return player
    print("player not found.")
    return None

def remove_player():
    player_id = int(input("enter player id to remove:"))
    for player in players:
        if player.player_id == player_id:
            players.remove(players)
            print("player removed successfully.")
            return
    print ("players not found.")

def update_wickets():
    player = serach_player()
    if player:
        wickets = int(input("enter wickets to Add:"))
        player.update_wickets(wickets)

def update_matches():
    player = serach_player()
    if player:
        matches = int(input("enter matches to Add:"))
        player.update_matches(matches)

def update_team():
    player = serach_player()
    if player:
        team = input("enter new team to Add:")
        player.update_team(team)

def update_role():
    player = serach_player()
    if player:
        role = input("enter new role to Add:")
        player.update_role(role)

def calculate_performance():
    player = serach_player()
    if player:
        print("performance:",player.calculate_performance())

def player_summary():
    player = serach_player()
    if player:
        player.player_summary()

def get_runs():
    player = serach_player()
    if player:
        print("runs:",player.get_runs())


while True:
    print("=========================================")
    print(" CRICKET MANAGEMENT SYSTEM ")
    print("==========================================")
    print("1. Add player")
    print("2. View players")
    print("3. Search player")
    print("4. Remove player")
    print("5. Update wickets")
    print("6. Update matches")
    print("7. Update team")
    print("8  Update role")
    print("9. Calculate performance")
    print("10. Player  summary")
    print("11. Player get runs")
    print("12. Exit")

    choice = int(input("enter choioce:"))

    if choice == 1:
        add_players()

    elif choice == 2:
        view_players()
    elif choice == 3:
        serach_player()
    elif choice == 4:
        remove_player()
    elif choice == 5:
        update_wickets()
    elif choice == 6:
        update_matches()
    elif choice == 7:
        update_team()
    elif choice == 8:
        update_role()
    elif choice == 9:
        calculate_performance()
    elif choice == 10:
        player_summary()
    elif choice == 11:
        get_runs()
    elif choice == 12:
        print("exit...")
        break
    else:
        print("invaild choice")


        