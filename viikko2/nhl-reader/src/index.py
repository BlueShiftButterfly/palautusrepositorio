import requests
from player import Player

def main():
    def player_score(player):
        return player.points

    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN:")
    players.sort(key=player_score, reverse=True)
    for player in players:
        if player.nationality != "FIN":
            continue
        print(player)


if __name__ == "__main__":
    main()
