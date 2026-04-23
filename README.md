# Football Match Finder

A simple Python CLI tool that fetches the next scheduled football match for a given team using the Football-Data.org API.

## Features
Search for a team by name, short name, or TLA (e.g., "Man Utd", "MUFC")
Supports multiple leagues and regions
Displays:
Competition name
Match teams
Local date & time (Africa/Johannesburg timezone)
Fetches only the next scheduled match
## Installation
1. Clone the repository
git clone https://github.com/map-r123/football-match-finder.git
cd football-match-finder
2. Install dependencies
pip install requests pytz
🔑 API Key Setup

This project uses the Football-Data.org API.

Sign up at: https://www.football-data.org/
Get your API key
Replace the API key in the code:
header = {"X-Auth-Token": "YOUR_API_KEY"}
▶️ Usage
Default (Premier League)
python project.py

You will be prompted:

Team: Arsenal
Specify a league
python project.py "La Liga"
Specify a league and region
python project.py "Premier League" "England"
## How It Works
Determines the competition code
Finds the team ID based on user input
Fetches the next scheduled match
Converts UTC time to local Johannesburg time
Displays formatted match info
## Example Output
***********************************
Premier League
(ARS) Arsenal vs Chelsea (CHE)

Date: 2026-05-12 Time: 18:30:00
***********************************
## Error Handling

The script will exit if:

Team is not found
League is not found
Region is invalid
No scheduled matches exist
API request fails
## Dependencies
requests
pytz
Python 3.8+
## Notes
API requests are rate-limited (1-second delay between calls)
Timezone is fixed to Africa/Johannesburg
