def add_team():
    team_name = input("Enter team name you want to add: ")
    if team_name and team_name not in team_list:
        team_list[team_name] = []
        print(f"Team {team_name} added.")
    else:
        print(f"Team {team_name} already exists or invalid team name.")


def remove_team():
    team_name = input("Enter team name you want to remove: ")
    if team_name and team_name in team_list:
        del team_list[team_name]
        print(f"Team {team_name} removed.")
    else:
        print(f"Team {team_name} does not exist.")


def list_teams():
    if team_list:
        for key, value in team_list.items():
            print(f"{key}: {value}")
    else:
        print("Team list is empty.")


def add_player():
    team_name = input("Enter the team you want to add the player to: ")
    for key, value in team_list.items():
        if team_name == key:
            player_name = input("Enter the player name you want to add: ")
            value.append(player_name)
            print(f"Player {player_name} added.")
        else:
            print(f"Team {team_name} does not exist.")


def remove_player():
    team_name = input("Enter the team you want to remove the player from: ")
    for key, value in team_list.items():
        if team_name == key:
            player_name = input("Enter the player name you want to remove: ")
            value.remove(player_name)
            print(f"Player {player_name} removed.")
        else:
            print(f"Team {team_name} does not exist.")


def list_players():
    team_name = input("Enter the team you want to list the player names from: ")
    for key, value in team_list.items():
        if team_name == key:
            print(f"{value}")
        else:
            print(f"Team {team_name} does not exist.")


# Main

team_list = {}
loop = True
print("Welcome to Final Exercise Module 1! | Team Management")
while loop:
    print("\n1. Add Team\n2. Remove Team\n3. List Teams\n4. Add Player\n5. Remove Player.\n6. List Players\n7. Exit")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        add_team()
    elif choice == 2:
        remove_team()
    elif choice == 3:
        list_teams()
    elif choice == 4:
        add_player()
    elif choice == 5:
        remove_player()
    elif choice == 6:
        list_players()
    else:
        loop = False
