import requests
import pandas as pd
import re
import numpy as np
from .DataScraper import DataScraper
from collections import defaultdict
import json


class Fanta3plusDataScraper(DataScraper):

    def __init__(self, config, config_std):
        DataScraper.__init__(self, config)
        self.config = config
        self.config_std = config_std


    def find_header_from_html(self, html):
        start = '<thead>'
        end = '</thead>'
        header_str = self.find_string_between(html, start, end)

        start = '<tr name="theader">'
        end = '</tr>'
        header_str = self.find_string_between(header_str, start, end)

        start = '>'
        end = '<'
        header_str = header_str.split('\n')
        header = []
        for line in header_str:
            field = self.find_string_between(line, start, end).strip()
            if len(field) > 0:
                header.append(field.strip())
        header.insert(0, 'dots')
        return header



    def parse_html(self, yyss):
        header = self.find_header_from_html(self.html)

        self.html = self.find_string_between(self.html, '<tbody>', '</tbody>')
        if yyss == self.current_yyss:
            # HTML CODE HAS PROBLEM -> tbody has space AFTER
            self.html = self.find_string_between(self.html, '<tbody >', '</tbody>')

        self.html = self.html.replace('\n', '').replace('\t', '')

        html_list = self.html.split('</tr>')


        records = []
        for i in range(len(html_list)):
            try:

                # careful on space before align
                html_list[i] = html_list[i].replace(' align="center"', '')
                html_list[i] = re.sub('<!--.*?-->', '', html_list[i])

                entries = html_list[i]\
                            .replace('</td>', '') \
                            .replace(',','.')  \
                            .split('<td>')


                entries[0] = re.search('GIORNATA (\d+)', entries[0]).group(1)
                record = {}
                for i, e in enumerate(entries):
                    e = e.replace('<!--', '')
                    if e == '-->':
                        i=i-1
                        continue
                    elif len(e) == 0 or e == '-':
                        record[header[i]] = 0
                    else:
                        record[header[i]] = e

                records.append(record)
            except AttributeError:
                pass

        df = pd.DataFrame(data=records, columns=header).sort_values(by='dots')
        df = df.replace({'S.V.': np.nan, 'SV':np.nan})

        print(df.columns)
        for c in df.columns:
            df[c] = df[c].astype(self.config_std['data_types'][c])
            df = df.rename(columns={c:self.config_std['column_names'][c]})


        df.giocatore = df.giocatore.str.lower().str.strip()
        df.squadra = df.squadra.str.lower().str.strip()
        df.ruolo = df.ruolo.str.strip()

        df = df[df.giocatore != 'nan']
        df['yyss'] = yyss




        for dots in df.dots.unique():
            df[df.dots == dots]\
                .to_csv(self.data_root\
                    .joinpath(yyss)\
                    .joinpath(str(int(dots)))\
                    .joinpath('%s_dots_%d.csv' % (yyss, int(dots)) ),
                index=True)

        return



    def standardize_yyss(self, yyss):
        return yyss[0:5] + '20' + yyss[5:]


    def download_data(self):

        print('Start data download %s' % self.journal)
        for yyss in self.yyss:

            if yyss != self.current_yyss:
                url = self.url % ( self.standardize_yyss(yyss))
                self.get_request(url)
                self.parse_html(yyss)
                a=1

            else:
                print(yyss)
                url = self.url.replace('-storico', '') % 'serie-a'
                self.get_request(url)
                self.parse_html(yyss)



            print('\t%s - %s downloaded' % (self.journal, yyss))
        print('End data download %s' % self.journal)
        print()

        # self.make_one_file_from_raw_data()
        #
        # df = pd.read_csv(self.data_root.joinpath(self.journal + '_stats_per_dots.csv'))
        # df['nome_giocatore']=df['giocatore']
        #
        # self.table_2_json(
        #     df,
        #     ['yyss', 'dots', 'giocatore'],
        #     self.data_root.joinpath(self.journal + '_stats_per_dots.json')
        # )


