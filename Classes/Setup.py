from pathlib import Path
import os
import shutil


class Setup:

    def __init__(self, config):
        self.root = config['data_root']
        self.seasons = config['yyss']
        self.journals = config['journals']

        # shutil.rmtree(self.root)

        # for season in self.seasons:
        #     # p_player = self.root.joinpath('players').joinpath(season)
        #     # if not os.path.exists(p_player):
        #     #     os.makedirs(p_player)


        for season in self.seasons:
            for day in range(1,39):
                p = self.root.joinpath(season).joinpath(str(day))
                if not os.path.exists(p):
                    os.makedirs(p)






