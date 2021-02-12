from pathlib import Path
import os
import shutil


class Setupper:

    def __init__(self, config, season, journal):
        self.root = config['data_root']
        self.seasons = season
        self.journal = journal

        self.create_path_if_not_exists(self.root.joinpath(self.journal))


        for season in self.seasons:
            self.create_path_if_not_exists(self.root.joinpath(self.journal).joinpath(season))
            for day in range(1,39):
                self.create_path_if_not_exists\
                (
                    self.root\
                        .joinpath(self.journal)\
                        .joinpath(season)\
                        .joinpath(str(day))
                )

    def create_path_if_not_exists(self, p):
        if not os.path.exists(p):
            os.makedirs(p)




