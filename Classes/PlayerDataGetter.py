import requests
import numpy as np
import pandas as pd
import hashlib


class PlayerDataScraper:
    def __init__(self, config):
        self.url = config['url']
        self.data_root = config['data_root']
        self.yyss = config['yyss']
        self.html = None

    def get_request(self, url):
        self.html = requests.get(url).text

    def parse_players_html(self, yyss):
        df = pd.read_html(self.html)[0]
        df = df.drop('Unnamed: 0', axis=1)

        columns_to_rename = {}
        for c in df.columns:
            columns_to_rename[c] = c[3:-3].strip()
        df = df.rename(columns=columns_to_rename)

        df['code'] = df['Sqd'] + '-' + df['Giocatore']
        df['code'] = df.apply(lambda x: self.player_to_code(x.code), axis=1)
        df['yyss'] = yyss
        df = df.replace('-', np.nan)
        df[df.columns[3:-1]] = df[df.columns[3:-1]].astype(float)

        print('yyss:',yyss)
        print('len df:', len(df))
        print('unique code:', len(df.code.unique()))

        df.to_csv(self.data_root.joinpath('players').joinpath(yyss).joinpath('playereval_%s.csv' % yyss),
                  index=False)

    def make_one_file_from_data(self):

        f2 = open('%s/players.csv' % self.data_root.joinpath('players'), 'w+')
        f2.write(
            'squadra,giocatore,ruolo,quotazione,partite_giocate,gol_fatti_subiti,assist,ammonizioni,espulsioni,rigori_tirati,rigori_realizzati,rigori_sbagliati,rigori_parati,media_voto,media_magic_voto,media_punti,yyss\n')

        for ys in self.yyss:
            path2 = self.data_root.joinpath('players').joinpath(ys).joinpath('playereval_%s.csv' % ys)
            with open(path2, 'r') as temp:
                table = temp.readlines()
                table = table[1:]
                for line in table: f2.write(line)

        f2.close()

    def download_data(self):

        for yyss in self.yyss:
            self.get_request(self.url % (yyss))
            self.parse_players_html(yyss)

        self.make_one_file_from_data()

    def player_to_code(self, s):
        return int(hashlib.sha1(s.encode('utf-8')).hexdigest(), 16) % (10 ** 8)

