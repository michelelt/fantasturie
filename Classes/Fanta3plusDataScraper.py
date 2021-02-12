import requests
import pandas as pd
import re
import numpy as np
from .DataScraper import DataScraper
from Classes import Setup
import json


class Fanta3plusDataScraper(DataScraper):

    def __init__(self, config, config_std):
        super().__init__(config)
        self.config = config
        self.config_std = config_std
        self.all_data = pd.DataFrame()
        self.last_day = pd.DataFrame()


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

        new_header = []
        for field in header:
            new_field = self.standardize_field(field)
            new_header.append(new_field)
        return new_header



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
        df = df.replace({'S.V.': np.nan, 'SV': np.nan})

        for c in df.columns:
            df[c] = df[c].astype(self.config_std['data_types'][c])

        df.giocatore = df.giocatore.str.lower().str.strip()
        df.squadra = df.squadra.str.lower().str.strip()
        df.ruolo = df.ruolo.str.strip()

        df = df[df.giocatore != 'nan']
        df['yyss'] = yyss

        return df


    def standardize_yyss(self, yyss):
        return yyss[0:5] + '20' + yyss[5:]


    def download_data(self):

        print('Start data_ok download %s' % self.journal)
        dfs = []
        for yyss in self.yyss:

            if yyss != self.current_yyss:
                url = self.url % ( self.standardize_yyss(yyss))
                self.get_request(url)
                dfs.append(self.parse_html(yyss))

            else:
                url = self.url.replace('-storico', '') % 'serie-a'
                self.get_request(url)
                dfs.append(self.parse_html(yyss))


            print('\t%s - %s downloaded' % (self.journal, yyss))
        print('End data_ok download %s' % self.journal)
        print()
        self.all_data = pd.concat(dfs, axis=0)
        return self.all_data

    def download_last_day(self):
        url = self.url.replace('-storico', '') % 'serie-a'
        self.get_request(url)
        df = self.parse_html(self.current_yyss)

        df = df[df.dots == df.dots.max()]

        print('%s - %s LAST DAY downloaded' % (self.journal, self.current_yyss))
        self.last_day=df
        return df

    def standardize_field(self, field):

        return self.config_std['column_names_lower'][field.lower()]


    def dump_locally(self):

        if len(self.all_data) > 0:

            Setup.Setupper(self.config, self.all_data.yyss.unique(), self.journal)
            for yyss in self.all_data.yyss.unique():
                tmp = self.all_data[self.all_data.yyss == yyss]
                self.export_to_csv(tmp,yyss)

                for dots in tmp.dots.unique():
                    self.table_2_json(
                        tmp[tmp.dots==dots],
                        ['yyss', 'dots', 'giocatore'],
                        self.data_root \
                            .joinpath(yyss)\
                            .joinpath(str(dots))\
                            .joinpath('%s_dots_%d.json' % (yyss, dots ))
                    )


            self.all_data.to_csv(self.data_root.joinpath(self.journal + '_stats_per_dots.csv'))
            self.table_2_json(self.all_data,
                              ['yyss', 'dots', 'giocatore'],
                              self.data_root.joinpath(self.journal + '_stats_per_dots.json')
            )


        if len(self.last_day) > 0:

            Setup.Setupper(self.config, self.last_day.yyss.unique(), self.journal)
            self.export_to_csv(
                self.last_day,
                self.current_yyss
            )

            dots = int(self.last_day.dots.max())
            self.table_2_json(
                self.last_day,
                ['yyss', 'dots', 'giocatore'],
                self.data_root \
                    .joinpath(self.current_yyss) \
                    .joinpath(str(dots)) \
                    .joinpath('%s_dots_%d.json' % (self.current_yyss, dots))
            )
        return


    def dump_on_firebase(self):
        json_str_all_data = ""
        json_str_last_day = ""
        if len(self.all_data) > 0:
            json_str_all_data = self.table_2_json(
                self.all_data,
                ['yyss', 'dots', 'giocatore'],
                ""
            )

        if len(self.last_day) > 0:
            json_str_last_day = self.table_2_json(
                self.last_day,
                ['yyss', 'dots', 'giocatore'],
                ""
            )
        return json_str_all_data, json_str_last_day












