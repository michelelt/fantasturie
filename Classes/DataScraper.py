import requests
from collections import defaultdict
import json
from datetime import date


class DataScraper:

    def __init__(self, config):
        self.data_root = config['data_root'].joinpath(config['journal'])
        self.url = config['url']
        self.http_header = config['http_header']
        self.yyss = config['yyss']
        self.days_of_the_season = config['days_of_the_season']
        # self.file_header = config['file_header']
        self.journal = config['journal']

        data_structure_config = {
            'data_root': self.data_root,
            'yyss': self.yyss,
            'journals': [self.journal]
        }

        self.current_yyss = self.compute_current_yyss()

    def compute_current_yyss(self):
        current_date = date.today()
        if current_date.month >= 8:
            first = str(current_date.year)
            second= str(current_date.year+1)[2:4]
        else:
            first = str(current_date.year-1)
            second= str(current_date.year)[2:4]
        return first+'-'+second

    def get_request(self, url):
        self.html = requests.get(url, headers=self.http_header).text


    def parse_html(self):
        pass

    def export_to_csv(self, df, yyss):

        for dots in df.dots.unique():
            df[df.dots == dots]\
                .to_csv(self.data_root \
                    .joinpath(yyss) \
                    .joinpath(str(int(dots))) \
                    .joinpath('%s_dots_%d.csv' % (yyss, int(dots)) ),
                index=True)

        return

    def table_2_json(self, df, nesting_fields, output_filename):

        results = defaultdict(lambda: defaultdict(dict))
        grp = df.set_index(nesting_fields)

        for index, value in grp.iterrows():

            for i, key in enumerate(index):
                if i == 0:
                    nested = results[key]
                elif i == len(index) - 1:
                    nested[key] = value.to_dict()
                else:
                    nested = nested[key]

        if len (str(output_filename)) > 0:
            with open(output_filename, "w") as outfile:
                json.dump(results, outfile)

        return json.dumps(results)


    def make_one_file_from_raw_data(self):
        # create empty file:
        csv_filename = self.data_root.joinpath(self.journal + '_stats_per_dots.csv')
        f1 = open(csv_filename, 'w+')
        f1.write(self.file_header)

        for yyss in self.yyss:
            if yyss != self.current_yyss:
                for dots in self.days_of_the_season:

                    path1 = self.data_root\
                        .joinpath(yyss)\
                        .joinpath(str(dots))\
                        .joinpath('%s_dots_%d.csv' % (yyss, dots))
                    with open(path1, 'r') as temp:
                        table = temp.readlines()
                    table = table[1:]
                    for line in table: f1.write(line)

        f1.close()

    def find_string_between(self, s, start, end):
        i_start = s.find(start)
        i_end = s.find(end, i_start + 1)
        return s[i_start + len(start): i_end]

    def download_data(self):
        pass

    def dump_locally(self):
        pass

    def dump_on_firebase(self):
        pass





