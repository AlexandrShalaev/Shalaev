import requests
from PySide6 import QtWidgets
from ui_main_menu import Ui_MainWindow
from ui_team import Ui_Dialog
from ui_tournament import Ui_Tournament
from ui_noinfo import Ui_Ui_warning
from main import All_data
from PySide6.QtWidgets import QApplication, QMainWindow
import sqlite3
import sys


class Mygui(QMainWindow):
    def __init__(self):
        super(Mygui, self).__init__()
        self.all_data = All_data
        self.ui_main_menu = Ui_MainWindow()
        self.ui_main_menu.setupUi(self)
        self.warning = QtWidgets.QDialog()
        self.ui_warning = Ui_Ui_warning()
        self.ui_warning.setupUi(self.warning)
        self.tournament_window = QtWidgets.QDialog()
        self.ui_tournament = Ui_Tournament()
        self.ui_tournament.setupUi(self.tournament_window)
        self.load_football_data()
        self.load_hockey_data()
        connection = sqlite3.connect('football.db')
        connection.close()
        connection = sqlite3.connect('hockey.db')
        connection.close()
        self.ui_main_menu.Update_btn.clicked.connect(All_data)
        self.ui_main_menu.apply_btn.clicked.connect(self.load_football_data)
        self.ui_main_menu.apply_btn.clicked.connect(self.load_hockey_data)
        self.ui_main_menu.tableWidget_football.cellDoubleClicked.connect(self.expandShipments_football)
        self.ui_main_menu.tableWidget_hockey.cellDoubleClicked.connect(self.expandShipments_hockey)
        # self.ui_main_menu.tableWidget.cellDoubleClicked.connect(self.open_team_window)

    def get_team_number(self, db_name, team_name):
        team_number = []
        connection = sqlite3.connect(f'{db_name}.db')
        cursor = connection.cursor()
        sql_query = f"SELECT all_team FROM team_info WHERE all_url = '{team_name}'"
        cursor.execute(sql_query)
        rez = cursor.fetchone()
        team_number.append(rez[0])
        # self.all_data.players(self, db_name, rez[0])
        connection.close()
        return team_number[0]

    def expandShipments_football(self, row, column):
        connection = sqlite3.connect(f'football.db')
        item = self.ui_main_menu.tableWidget_football.item(row, column)
        if item.column() == 2 or item.column() == 5:
            team_name = item.text()
            team_number = self.get_team_number('football', team_name)
            if team_number == 'NULL' or team_number is None:
                self.warning.show()
            else:
                self.players(f'football', team_number)
                self.open_team_window('football')

        elif item.column() == 1:
            team_item = self.ui_main_menu.tableWidget_football.item(item.row(), 2)
            self.event_data('football', item.text(), team_item.text())
            self.get_event_data('football', self.event_data('football', item.text(), team_item.text()))
            self.open_tournament_window('football')
            if self.ui_tournament.tournament_tableWidget.rowCount() != 0:
                pass
            else:
                self.tournament_window.close()
                self.warning.show()

        connection.close()

    def expandShipments_hockey(self, row, column):
        connection = sqlite3.connect(f'hockey.db')
        item = self.ui_main_menu.tableWidget_hockey.item(row, column)
        if item.column() == 2 or item.column() == 5:
            team_name = item.text()
            team_number = self.get_team_number('hockey', team_name)
            if self.get_team_number('hockey', team_name) != 'NULL':
                self.players('hockey', team_number)
                self.open_team_window('hockey')
            else:
                self.warning.show()
        # elif item.column() == 1:
        #     team_item = self.ui_main_menu.tableWidget_hockey.item(item.row(), 2)
        #     self.event_data('hockey', item.text(), team_item.text())
        #     self.get_event_data('hockey', self.event_data('hockey', item.text(), team_item.text()))
        #     self.open_tournament_window('hockey')
        connection.close()

    def open_tournament_window(self, db_name):
        try:
            self.load_event_data(db_name)
            self.tournament_window.show()
        except Exception:
            self.warning.show()

        if self.tournament_window.close:
            connection = sqlite3.connect(f'football.db')
            cursor = connection.cursor()
            sql_query = "DELETE FROM event"
            cursor.execute(sql_query)
            connection.commit()
            connection.close()

    def open_team_window(self, db_name):
        self.team_window = QtWidgets.QDialog()
        self.ui_team = Ui_Dialog()
        self.ui_team.setupUi(self.team_window)
        self.load_player_data()
        self.team_window.show()

        connection = sqlite3.connect(f'{db_name}.db')
        cursor = connection.cursor()
        sql_count = "SELECT COUNT(*) FROM players"
        cursor.execute(sql_count)
        # time.sleep(0.1)
        for i in cursor.execute(sql_count):
            row_count = i[0]
            if row_count == 0:
                self.warning.show()
                self.team_window.close()
            else:
                pass

        if self.team_window.close:
            connection = sqlite3.connect(f'{db_name}.db')
            cursor = connection.cursor()
            sql_query = "DELETE FROM players"
            cursor.execute(sql_query)
            connection.commit()
            connection.close()
        connection.close()

    def load_football_data(self):
        connection = sqlite3.connect('football.db')
        cursor = connection.cursor()
        sql_query = "SELECT start_time, tournament_name, team_home, score_home, score_away, team_away, coef_1, " \
                    "coef_x, coef_2 FROM games"
        sql_count = "SELECT COUNT(*) FROM games"
        cursor.execute(sql_count)
        row_count = 0
        for i in cursor.execute(sql_count):
            row_count = i[0]
        self.ui_main_menu.tableWidget_football.setRowCount(row_count)
        tablerow = 0
        for row in cursor.execute(sql_query):
            self.ui_main_menu.tableWidget_football.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui_main_menu.tableWidget_football.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui_main_menu.tableWidget_football.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui_main_menu.tableWidget_football.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui_main_menu.tableWidget_football.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui_main_menu.tableWidget_football.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui_main_menu.tableWidget_football.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui_main_menu.tableWidget_football.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.ui_main_menu.tableWidget_football.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[8]))
            tablerow += 1
        self.ui_main_menu.tableWidget_football.resizeColumnsToContents()
        connection.close()

    def load_hockey_data(self):
        connection = sqlite3.connect('hockey.db')
        cursor = connection.cursor()
        sql_query = "SELECT start_time, tournament_name, team_home, score_home, score_away, team_away, coef_1, " \
                    "coef_x, coef_2 FROM games"
        sql_count = "SELECT COUNT(*) FROM games"
        cursor.execute(sql_count)
        row_count = 0
        for i in cursor.execute(sql_count):
            row_count = i[0]
        self.ui_main_menu.tableWidget_hockey.setRowCount(row_count)
        tablerow = 0
        for row in cursor.execute(sql_query):
            self.ui_main_menu.tableWidget_hockey.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui_main_menu.tableWidget_hockey.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui_main_menu.tableWidget_hockey.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui_main_menu.tableWidget_hockey.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui_main_menu.tableWidget_hockey.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui_main_menu.tableWidget_hockey.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui_main_menu.tableWidget_hockey.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui_main_menu.tableWidget_hockey.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.ui_main_menu.tableWidget_hockey.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[8]))
            tablerow += 1
        self.ui_main_menu.tableWidget_hockey.resizeColumnsToContents()
        connection.close()

    def load_player_data(self):
        db_name = self.ui_main_menu.FOOTBALL.objectName()
        connection = sqlite3.connect(f'{db_name}.db')
        cursor = connection.cursor()
        sql_query = "SELECT player_name, jersey_number, player_country, player_role, player_date_of_birth, " \
                    "season_name, matches_played, goals_scored, yellow_cards, red_cards FROM players"
        sql_count = "SELECT COUNT(*) FROM players"
        cursor.execute(sql_count)
        row_count = 0
        for i in cursor.execute(sql_count):
            row_count = i[0]
        self.ui_team.tableWidget.setRowCount(row_count)
        tablerow = 0
        for row in cursor.execute(sql_query):
            self.ui_team.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui_team.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui_team.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui_team.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui_team.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui_team.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui_team.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui_team.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.ui_team.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[8]))
            self.ui_team.tableWidget.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(row[9]))
            tablerow += 1
        self.ui_team.tableWidget.resizeColumnsToContents()
        connection.close()

    def load_event_data(self, db_name):
        connection = sqlite3.connect(f'{db_name}.db')
        cursor = connection.cursor()
        sql_query = "SELECT rank, competitor, played, win, loss, draw, goals_for, goals_against, points FROM " \
                    "event"
        sql_count = "SELECT COUNT(*) FROM event"
        cursor.execute(sql_count)
        row_count = 0
        for i in cursor.execute(sql_count):
            row_count = i[0]
        self.ui_tournament.tournament_tableWidget.setRowCount(row_count)
        tablerow = 0
        for row in cursor.execute(sql_query):
            self.ui_tournament.tournament_tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui_tournament.tournament_tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui_tournament.tournament_tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui_tournament.tournament_tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui_tournament.tournament_tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui_tournament.tournament_tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui_tournament.tournament_tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui_tournament.tournament_tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.ui_tournament.tournament_tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[8]))
            tablerow += 1
        self.ui_tournament.tournament_tableWidget.resizeColumnsToContents()
        connection.close()

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

    def get_event_data(self, db_name, event_url):
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
        try:
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
        except Exception:
            pass
        query_insert = list(zip(rank, played, win, loss, draw, goals_for, goals_against, competitor, points))
        for i in range(len(query_insert)):
            self.execute_event_query(query_insert[i], db_name)

    def event_data(self, db_name, tournament_name, team_name):
        req = []
        connection = sqlite3.connect(f'{db_name}.db')
        cursor = connection.cursor()
        sql_query = f"SELECT event_url FROM games WHERE tournament_name = '{tournament_name}' AND team_home = '{team_name}'"
        for query in cursor.execute(sql_query):
            req.append(query[0])
        connection.close()

        return req[0]



    def execute_players_query(self, query_insert, db_name):
        connection = sqlite3.connect(f'{db_name}.db')
        cursor = connection.cursor()
        sql_query = "INSERT OR REPLACE INTO players (player_date_of_birth, player_name, jersey_number, " \
                    "player_country, player_role, player_date_of_birth, season_name, matches_played, goals_scored, " \
                    "yellow_cards, red_cards) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(sql_query, query_insert)
        connection.commit()
        connection.close()

    def execute_event_query(self, query_insert, db_name):
        connection = sqlite3.connect(f'{db_name}.db')
        cursor = connection.cursor()
        sql_query = "INSERT OR REPLACE INTO event (rank, played, win, loss, draw, goals_for, goals_against, " \
                    "competitor, points) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(sql_query, query_insert)
        connection.commit()
        connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mygui()
    window.show()

    sys.exit(app.exec())
