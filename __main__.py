from configurations.config import gazzetta_config, corriere_dello_sport_config, data_std_fantapiu,\
    tuttosport_config,fantagazzetta_config,gazzetta3plus_config, data_structure_config

from Classes.GazzettaDataScraper import GazzettaDataScraper
from Classes.Fanta3plusDataScraper import Fanta3plusDataScraper
from Classes import Setup
import os


import shutil

if __name__== '__main__':

    print('Download Historic Data\n')
    # try:
    #     shutil.rmtree(data_structure_config['data_root'])
    # except FileNotFoundError:
    #     os.mkdir(data_structure_config['data_root'])
    

    s = Fanta3plusDataScraper(corriere_dello_sport_config, data_std_fantapiu)
    s.download_data()
    s.dump_locally()
    # s.download_last_day()
    # s.dump_on_firebase()

    s = Fanta3plusDataScraper(tuttosport_config, data_std_fantapiu)
    s.download_data()
    s.dump_locally()
    # s.download_last_day()
    # s.dump_on  _firebase()

    s = Fanta3plusDataScraper(fantagazzetta_config, data_std_fantapiu)
    s.download_data()
    s.dump_locally()
    # s.download_last_day()
    # s.dump_on_firebase()

    s = Fanta3plusDataScraper(gazzetta3plus_config, data_std_fantapiu)
    s.download_data()
    s.dump_locally()
    # s.download_last_day()
    # s.dump_on_firebase()

