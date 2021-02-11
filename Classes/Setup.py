from pathlib import Path
import os
import shutil


class Setupper:

    def __init__(self, config):
        self.root = config['data_root']
        self.seasons = config['yyss']
        self.journals = config['journals']


        for season in self.seasons:
            for day in range(1,39):
                p = self.root.joinpath(season).joinpath(str(day))
                if not os.path.exists(p):
                    os.makedirs(p)






