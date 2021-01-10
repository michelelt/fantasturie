from configurations.config import gazzetta_config, corriere_dello_sport_config, \
    tuttosport_config,fantagazzetta_config,gazzetta3plus_config

from Classes.GazzettaDataScraper import GazzettaDataScraper
from Classes.Fanta3plusDataScraper import Fanta3plusDataScraper

import shutil

if __name__== '__main__':

    print('Download Historic Data\n')
    # shutil.rmtree('./data/')
    
    
    # GazzettaDataScraper(gazzetta_config).download_data()
    
    Fanta3plusDataScraper(corriere_dello_sport_config).download_data()
    Fanta3plusDataScraper(tuttosport_config).download_data()
    Fanta3plusDataScraper(fantagazzetta_config).download_data()
    Fanta3plusDataScraper(gazzetta3plus_config).download_data()
