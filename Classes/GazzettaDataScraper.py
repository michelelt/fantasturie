import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from .DataScraper import DataScraper


class GazzettaDataScraper(DataScraper):




    def parse_html(self, yyss, dots):

        soup = BeautifulSoup(self.html, 'html.parser')
        teams = soup.findAll('ul', {'class': 'magicTeamList'})
        teams_s = []
        for i, team in enumerate(teams):
            teams_s.append(list(team.stripped_strings))

        teams_s.sort()
        teams_s = teams_s[0:20]

        final_df = pd.DataFrame()
        for team in teams_s:

            team_name = team.pop(0)
            team.insert(0,'position_cod')
            team.insert(0,'position')
            team.insert(0,'name')
            team.insert(0,'number')
            for n in range(team.count('\uf114')): team.remove('\uf114')
            for n in range(team.count('\uf115')): team.remove('\uf115')

            data = np.array(team)
            shape = (int(len(data)/13), 13)
            try:
                data = data.reshape(shape)
                df = pd.DataFrame(data[1:], columns=data[0])
                df = df.replace('-', np.nan)

                df[['V', 'G', 'A', 'R', 'RS', 'AG', 'AM', 'ES', 'FV']] = \
                    df[['V', 'G', 'A', 'R', 'RS', 'AG', 'AM', 'ES', 'FV']].astype(float)
                df['team'] = team_name
                df['dots'] = dots
                df['yyss'] = yyss
                final_df = final_df.append(df)
            except ValueError:
                print('\t error %s %d - %s' %(yyss, dots, team_name))


        final_df.to_csv(self.data_root\
                            .joinpath(yyss)\
                            .joinpath(str(dots))\
                            .joinpath('%s_dots_%d.csv'%(yyss,dots)),
                        index=True)

    # def make_one_file_from_raw_data(self):
    #     #create empty file:
    #     f1 = open('%s/stats_per_dots.csv'%self.data_root, 'w+')
    #     # f1.write('code,numero,giocatore,ruolo,ruolo_cod,voto,gol_fatti_subiti,assist,rigori_realizzati,rigori_sbagliati,autogol,ammonizioni,espulsioni,fantavoto,squadra,dots,yyss\n')
    #     f1.write(self.file_header)
    #
    #     for yyss in self.yyss:
    #         if yyss != self.current_yyss:
    #             for dots in self.days_of_the_season:
    #
    #                 path1 = self.data_root.joinpath(yyss).joinpath(str(dots)).joinpath('%s_dots_%d.csv'%(yyss,dots))
    #                 with open(path1, 'r') as temp: table = temp.readlines()
    #                 table = table[1:]
    #                 for line in table: f1.write(line)
    #
    #     f1.close()


    def download_data(self):

        print('Start data_ok download %s' % self.journal)
        for yyss in self.yyss:
            if yyss != self.current_yyss:
                for dots in self.days_of_the_season:

                    self.get_request(self.url%(yyss, dots))
                    self.parse_html(yyss, dots)

            print('\t%s - %s %d downloaded' % (self.journal, yyss, dots))
        print('End data_ok download %s' % self.journal)
        print()

        self.make_one_file_from_raw_data()




























