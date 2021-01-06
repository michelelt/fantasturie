import requests
import pandas as pd
import re
import numpy as np
from .DataScraper import DataScraper


class Fanta3plusDataScraper(DataScraper):

    def __init__(self, config):
        DataScraper.__init__(self, config)
        self.header = config['header']
        self.data_types = config['data_types']


    def parse_html(self, yyss):
        self.html = self.html.replace('\n', '').replace('\t', '')

        html_list = self.html.split('</tr>')

        records = []
        for i in range(len(html_list)):
            try:
                entry = html_list[i]\
                            .replace('</td>', '') \
                            .replace('<!--', '') \
                            .replace('-->', '') \
                            .replace(',','.')  \
                            .split('<td>')
                entry[0] = re.search('GIORNATA (\d+)', entry[0]).group(1)
                record = {}
                for i, e in enumerate(entry): record[self.header[i]] = 0 if len(e) == 0 or e == '-' else e
                records.append(record)
            except AttributeError:
                pass

        df = pd.DataFrame(data=records, columns=self.header, ).sort_values(by='dots')
        df = df.replace({'S.V.': np.nan, 'SV':np.nan})
        df = df.astype(self.data_types)

        df = df.drop('?', axis=1)
        df = df[df.giocatore != 'nan']
        df['yyss'] = yyss

        if 'numero' in df.columns:
            print('\t-->', yyss)
        for dots in df.dots.unique():
            df[df.dots == dots]\
                .to_csv(self.data_root\
                .joinpath(yyss)\
                .joinpath(str(dots))\
                .joinpath('%s_dots_%d.csv'%(yyss,dots)),
                    index=True)



    def standardize_yyss(self, yyss):
        return yyss[0:5] + '20' + yyss[5:]


    def download_data(self):

        print('Start data download %s' % self.journal)
        for yyss in self.yyss:

            if yyss != self.current_yyss:
                self.get_request(self.url % ( self.standardize_yyss(yyss)) )
                self.parse_html(yyss)

            print('\t%s - %s downloaded' % (self.journal, yyss))
        print('End data download %s' % self.journal)
        print()

        self.make_one_file_from_raw_data()
