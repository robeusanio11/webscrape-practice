from bs4 import BeautifulSoup
import requests

teams = ["ATL", "BOS", "BRK", "CHO", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOH", "NYK", "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]
for team in teams:
    html_text = requests.get(f"https://www.basketball-reference.com/teams/{team}/2024.html").text;
    soup = BeautifulSoup(html_text, 'lxml');
    player_cards = soup.find_all('td', attrs={"data-stat": "player"});

    print (team + " 2024 Roster:");
    for player in player_cards:
        print(player.find('a').text);

