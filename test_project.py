import pytest
from project import get_team_id, get_matches, get_competition_code, get_region

# This pytest is going to break as the live API data was used
# It was tested as of 17/04/2026 at 21:50

def test_get_team_id():
    assert get_team_id("Arsenal", "PL") == 57
    assert get_team_id("CHE", "PL") == 61
    assert get_team_id("rb leipzig","BL1")
    with pytest.raises(SystemExit):
        get_team_id("rb leipzig","PL")
    
def test_get_matches():
    result = get_matches(1)
    assert result["home"] == "1. FC Köln"
    assert result["away"] == "Bayer 04 Leverkusen"
    assert result["comp"] == "Bundesliga"

def test_get_competition_code():
    assert get_competition_code("PL") == "PL"
    assert get_competition_code("Bundesliga") == "BL1"
    with pytest.raises(SystemExit):
        get_competition_code("la liga",2224)

def test_get_region():
    assert get_region("Europe") == 2077
    with pytest.raises(SystemExit):
        get_region("Spain")

