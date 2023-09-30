from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.basketball-reference.com/teams/DEN/2024.html').text;
soup = BeautifulSoup(html_text, 'lxml');
player_cards = soup.find_all('td', attrs={"data-stat": "player"});
firstPlayerName = player_cards[0].find('a').text;

for player in player_cards:
    print(player.find('a').text);
