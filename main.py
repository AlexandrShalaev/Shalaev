import requests
import sqlite3
from datetime import datetime


class All_data:
    def __init__(self):
        super(All_data, self).__init__()
        self.create_connection('football')
        self.games('https://myscore.club/api/sport/football/', 'football')
        self.create_connection('hockey')
        self.games('https://myscore.club/api/sport/hockey/', 'hockey')

    def create_connection(self, db_name):
        connection = sqlite3.connect(db_name + '.db')
        cursor = connection.cursor()
        connection.execute("DROP TABLE games")
        connection.commit()
        connection.execute("DROP TABLE players")
        connection.commit()
        connection.execute("DROP TABLE event")
        connection.commit()
        connection.execute("DROP TABLE team_info")
        connection.commit()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS `games` (
        `id` INTEGER PRYMARY KEY,
        `team_home_url` VARCHAR(45) NULL,
        `team_away_url` VARCHAR(45) NULL,
        `score_home` VARCHAR(45) NULL,
        `score_away` VARCHAR(45) NULL,
        `status` VARCHAR(45) NULL,
        `tournament_name` VARCHAR(45) NULL,
        `start_time` VARCHAR(45) NULL,
        `team_home` VARCHAR(45) NULL,
        `team_away` VARCHAR(45) NULL,
        `coef_1` VARCHAR(45) NULL,
        `coef_2` VARCHAR(45) NULL,
        `coef_x` VARCHAR(45) NULL,
        `yellow_home` VARCHAR(45) NULL,
        `yellow_away` VARCHAR(45) NULL,
        `red_home` VARCHAR(45) NULL,
        `red_away` VARCHAR(45) NULL,
        `event_url` VARCHAR(45) NULL)
        ''')
        connection.commit()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS `players` (
        `idgames` INT,
        `player_name` VARCHAR(45) NULL,
        `jersey_number` VARCHAR(45) NULL,
        `player_country` VARCHAR(45) NULL,
        `player_role` VARCHAR(45) NULL,
        `player_date_of_birth` VARCHAR(45) NULL,
        `season_name` VARCHAR(45) NULL,
        `matches_played` VARCHAR(45) NULL,
        `goals_scored` VARCHAR(45) NULL,
        `yellow_cards` VARCHAR(45) NULL,
        `red_cards` VARCHAR(45) NULL,
        PRIMARY KEY (`idgames`))
        ''')
        connection.commit()
        # rank, played, win, loss, draw, goals_for, goals_against, competitor
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS `event` (
        `idgames` INT,
        `rank` VARCHAR(45) NULL,
        `played` VARCHAR(45) NULL,
        `win` VARCHAR(45) NULL,
        `loss` VARCHAR(45) NULL,
        `draw` VARCHAR(45) NULL,
        `goals_for` VARCHAR(45) NULL,
        `goals_against` VARCHAR(45) NULL,
        `competitor` VARCHAR(45) NULL,
        `points` VARCHAR(45) NULL,
        PRIMARY KEY (`idgames`))
        ''')
        connection.commit()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS `team_info` (
                `idinfo` INT,
                `all_url` VARCHAR(45) NULL,
                `all_team` VARCHAR(45) NULL,
                PRIMARY KEY (`idinfo`))
                ''')
        connection.commit()
        connection.close()

    def games(self, url, db_name):
        req = requests.get(url)
        response = req.json()
        # print(response)
        event_url = []
        team_home_url = []
        team_away_url = []
        score_home = []
        score_away = []
        status = []
        tournament_name = []
        yellow_home = []
        yellow_away = []
        red_home = []
        red_away = []
        start_time = []
        team_home = []
        team_away = []
        coef_1 = []
        coef_2 = []
        coef_x = []
        for info in response:
            for i in info['games']:
                try:
                    event_url.append(i['event_url'])
                    score_home.append(i['score']['team_home'])
                    score_away.append(i['score']['team_away'])
                    start_time.append(str(datetime.fromtimestamp(i['start_time'])))
                    status.append(i['status'])
                    team_home.append(i['team_home'][0]['name'])
                    team_away.append(i['team_away'][0]['name'])
                    tournament_name.append(i['tournamentName'])
                    coef_1.append(i['coefficient']['1']['old'])
                    coef_x.append(i['coefficient']['x']['old'])
                    coef_2.append(i['coefficient']['2']['old'])
                    if 'cards' in i:
                        yellow_home.append(i['cards']['team_home']['yellow'])
                        red_home.append(i['cards']['team_home']['red'])
                        yellow_away.append(i['cards']['team_away']['yellow'])
                        red_away.append(i['cards']['team_away']['red'])
                    else:
                        yellow_home.append('NULL')
                        red_home.append('NULL')
                        yellow_away.append('NULL')
                        red_away.append('NULL')
                except Exception:
                    pass

        for i in event_url:
            response_for_event = requests.get(f'https://myscore.club/api{i}menu/').json()
            if 'route' in response_for_event['team_home'][0] or 'route' in response_for_event['team_away'][0]:
                team_home_url.append(response_for_event['team_home'][0]['route'])
                team_away_url.append(response_for_event['team_away'][0]['route'])
            else:
                team_home_url.append('NULL')
                team_away_url.append('NULL')
        all_url = team_home + team_away
        all_team = team_home_url + team_away_url
        sql_query = list(zip(all_url, all_team))
        for i in range(len(sql_query)):
            self.execute_all_url_and_team(sql_query[i], db_name)

        query_insert = list(
            zip(team_home_url, team_away_url, score_home, score_away, status, tournament_name, yellow_home, yellow_away,
                red_home, red_away, start_time, team_home, team_away, coef_1, coef_2, coef_x, event_url))
        # # print(query_insert)
        for i in range(len(query_insert)):
            self.execute_games_query(query_insert[i], db_name)
        #     print(f'Yes {i} sir')
        #     for key in i.keys():
        #         print(key)
        # all_keys = list(k for d in info['games'] for k in d.keys())
        #
        # for x in all_keys:
        #     if x not in temp:
        #         temp.append(x)

    def players(self, db_name, team_name):
        response = requests.get(f'https://myscore.club/api{team_name}squad/').json()
        all_player_keys = []
        player_name = []
        jersey_number = []
        player_country = []
        player_role = []
        player_date_of_birth = []
        season_name = []
        matches_played = []
        goals_scored = []
        yellow_cards = []
        red_cards = []

        try:
            for key in response['squad'].keys():
                all_player_keys.append(key)
            for i in all_player_keys:
                player_name.append(response['squad'][i]['player_name'])
                jersey_number.append(response['squad'][i]['jersey_number'])
                player_country.append(response['squad'][i]['player_country'])
                player_role.append(response['squad'][i]['player_role'])
                player_date_of_birth.append(response['squad'][i]['player_date_of_birth'])
                season_name.append(response['squad'][i]['seasons'][0]['season_name'])
                matches_played.append(response['squad'][i]['seasons'][0]['statistics']['matches_played'])
                goals_scored.append(response['squad'][i]['seasons'][0]['statistics']['goals_scored'])
                yellow_cards.append(response['squad'][i]['seasons'][0]['statistics']['yellow_cards'])
                red_cards.append(response['squad'][i]['seasons'][0]['statistics']['red_cards'])
        except Exception:
            pass

        query_insert = list(
            zip(player_date_of_birth, player_name, jersey_number, player_country, player_role, player_date_of_birth,
                season_name, matches_played, goals_scored, yellow_cards, red_cards))
        for i in range(len(query_insert)):
            self.execute_players_query(query_insert[i], db_name)

    def get_team_number(self, db_name, team_name):
        connection = sqlite3.connect(f'{db_name}.db')
        cursor = connection.cursor()
        sql_query = f"SELECT all_url FROM team_info WHERE all_team = '{team_name}'"
        cursor.execute(sql_query)
        rez = cursor.fetchone()
        connection.close()

        return rez[0]
        # if cursor.fetchone() is not None or "NULL":
        #     print(cursor.fetchone())
        # else:
        #     sql_query = "SELECT team_away_url FROM games WHERE team_away = ?"
        #     cursor.execute(sql_query, (team_name,))
        #     print(cursor.fetchone())
        # cursor.close()

    def get_all_teams(self, number_of_team, db_name):
        req = requests.get(f'https://myscore.club/api/team/{number_of_team}/recentResults/')
        response = req.json()
        all_team_id = []
        all_team_names = []

        if response['recentMatches'][0]['competitor_home']['id'][14:] == str(number_of_team):
            all_team_id.append(response['recentMatches'][0]['competitor_home']['id'][14:])
            all_team_names.append(response['recentMatches'][0]['competitor_home']['name'])
        else:
            all_team_id.append(response['recentMatches'][0]['competitor_away']['id'][14:])
            all_team_names.append(response['recentMatches'][0]['competitor_away']['name'])
        query_insert = list(zip(all_team_id, all_team_names))
        self.execute_all_teams_id(query_insert[0], db_name)

        # self.execute_all_teams_id(query_insert, db_name)
    def get_event_data(self, event_url):
        req = requests.get(f'https://myscore.club/api{event_url}standing/')
        response = req.json()
        rank = []
        played = []
        win = []
        loss = []
        draw = []
        goals_for = []
        goals_against = []
        competitor = []
        points = []
        for games in response['standing']['standings']:
            rank.append(games['rank'])
            played.append(games['played'])
            win.append(games['win'])
            loss.append(games['loss'])
            draw.append(games['draw'])
            goals_for.append(games['goals_for'])
            goals_against.append(games['goals_against'])
            competitor.append(games['competitor']['name'])
            points.append(games['points'])
        query_insert = list(zip(rank, played, win, loss, draw, goals_for, goals_against, competitor, points))
        for i in range(len(query_insert)):
            self.execute_even_query(query_insert[i], 'obar')

    def execute_even_query(self, query_insert, db_name):
        connection = sqlite3.connect(db_name + '.db')
        cursor = connection.cursor()
        sql_query = "INSERT OR REPLACE INTO event (rank, played, win, loss, draw, goals_for, goals_against, " \
                    "competitor, points) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(sql_query, query_insert)
        connection.commit()
        connection.close()

    def execute_players_query(self, query_insert, db_name):
        connection = sqlite3.connect(db_name + '.db')
        cursor = connection.cursor()
        sql_query = "INSERT OR REPLACE INTO players (player_date_of_birth, player_name, jersey_number, " \
                    "player_country, player_role, player_date_of_birth, season_name, matches_played, goals_scored, " \
                    "yellow_cards, red_cards) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(sql_query, query_insert)
        connection.commit()
        connection.close()

    def execute_all_teams_id(self, query_insert, db_name):
        connection = sqlite3.connect(db_name + '.db')
        cursor = connection.cursor()
        sql_query = "INSERT INTO squad_info (id, team_name) VALUES(?, ?);"
        cursor.execute(sql_query, query_insert)
        connection.commit()
        connection.close()

    def execute_all_url_and_team(self, query_insert, db_name):
        connection = sqlite3.connect(db_name + '.db')
        cursor = connection.cursor()
        sql_query = "INSERT INTO team_info (all_url, all_team) VALUES(?, ?);"
        cursor.execute(sql_query, query_insert)
        connection.commit()
        connection.close()

    def execute_games_query(self, query_insert, db_name):
        connection = sqlite3.connect(db_name + '.db')
        cursor = connection.cursor()
        sql_query = "INSERT INTO games (team_home_url, team_away_url, score_home, score_away, status, " \
                    "tournament_name, yellow_home, yellow_away, red_home, red_away, start_time, team_home, team_away, " \
                    "coef_1, coef_2, coef_x, event_url) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(sql_query, query_insert)
        connection.commit()
        connection.close()


if __name__ == '__main__':
    All_data()
