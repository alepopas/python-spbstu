list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

numberPlayers = len(list_players)
peopleInFirstTeam = numberPlayers//2
peopleInSecondTeam = numberPlayers - peopleInFirstTeam

firstTeam = list_players[:peopleInFirstTeam]
secondTeam = list_players[peopleInSecondTeam:]

print(firstTeam)
print(secondTeam)