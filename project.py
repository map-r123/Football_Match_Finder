import requests
import sys
from datetime import datetime
import pytz
import time


def get_team_id(team_name, competition_code):
    url = f"http://api.football-data.org/v4/competitions/{competition_code}/teams"
    data = API(url)
    teams = data["teams"]

    user_team = team_name.lower()
    # return ID
    # check long and short name

    for team in teams:
        if (
            user_team in team["name"].lower()
            or user_team in team["shortName"].lower()
            or user_team in team["tla"].lower()
        ):
            return team["id"]

    sys.exit("Team not found")


def get_matches(team_id):
    url = f"https://api.football-data.org/v4/teams/{team_id}/matches?status=SCHEDULED&limit=1"
    data = API(url)
    matches = data["matches"]

    if not matches:
        sys.exit("No scheduled match found")

    # return match information
    competition = matches[0]["competition"]["name"]
    home = matches[0]["homeTeam"]
    away = matches[0]["awayTeam"]
    time = matches[0]["utcDate"]
    return {
        "home": home["name"],
        "homeTLA": home["tla"],
        "away": away["name"],
        "awayTLA": away["tla"],
        "time": time,
        "comp": competition,
    }


def get_competition_code(competition_name="PL", region_id=2077):
    if competition_name == "PL":
        return competition_name

    url = f"https://api.football-data.org/v4/competitions/?areas={region_id}"
    data = API(url)

    for comp in data["competitions"]:
        if competition_name.lower() in comp["name"].lower():
            return comp["code"]

    sys.exit("League not found")


def get_region(region_name):

    url = "https://api.football-data.org/v4/areas/2267"
    data = API(url)

    areas = data["childAreas"]

    for area in areas:
        if region_name.lower() == area["name"].lower():
            return area["id"]

    sys.exit("Could not find Region")


def main():

    if len(sys.argv) > 3:
        sys.exit("Too many arguments\nUsage: project.py <competition/league name> <region>")
    elif len(sys.argv) == 2:
        competition_code = get_competition_code(sys.argv[1])
        match_id = get_team_id(input("Team: "), competition_code)
        game = get_matches(match_id)
    elif len(sys.argv) == 3:
        region_id = get_region(sys.argv[2])
        competition_code = get_competition_code(sys.argv[1], region_id)
        match_id = get_team_id(input("Team: "), competition_code)
        game = get_matches(match_id)
    else:
        competition_code = get_competition_code()
        match_id = get_team_id(input("Team: "), competition_code)
        game = get_matches(match_id)

    output(game)


def output(game):

    ddatetime = datetime.fromisoformat(game["time"].replace("Z", "+00:00"))
    localTime = ddatetime.astimezone(pytz.timezone("Africa/Johannesburg"))

    print("\n" + "*" * 35)
    print(game["comp"])
    print(f"({game['homeTLA']}) {game['home']} vs {game['away']} ({game['awayTLA']})\n")
    print(f"Date: {localTime.date()} Time: {localTime.time()}")
    print("*" * 35)


def API(url):
    header = {"X-Auth-Token": "YOUR_API_KEY"}
    try:
        time.sleep(1)
        response = requests.get(url, headers=header)
        if response.status_code != 200:
            sys.exit(f"API Error: {response.status_code}")
    except requests.RequestException:
        sys.exit("API Request Error")
    else:
        return response.json()

if __name__ == "__main__":
    main()

