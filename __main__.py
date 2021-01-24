from configurations.config import gazzetta_config, corriere_dello_sport_config, data_std_fantapiu,\
    tuttosport_config,fantagazzetta_config,gazzetta3plus_config

from Classes.GazzettaDataScraper import GazzettaDataScraper
from Classes.Fanta3plusDataScraper import Fanta3plusDataScraper

import shutil

if __name__== '__main__':

    print('Download Historic Data\n')
    shutil.rmtree('./data/')
    
    

    Fanta3plusDataScraper(corriere_dello_sport_config, data_std_fantapiu).download_data()
    # Fanta3plusDataScraper(corriere_dello_sport_config).download_data_last_day()

    Fanta3plusDataScraper(tuttosport_config, data_std_fantapiu).download_data()
    # Fanta3plusDataScraper(tuttosport_config).download_data_last_day()

    Fanta3plusDataScraper(fantagazzetta_config, data_std_fantapiu).download_data()
    # Fanta3plusDataScraper(tuttosport_config).download_data_last_day()

    Fanta3plusDataScraper(gazzetta3plus_config, data_std_fantapiu).download_data()
    # Fanta3plusDataScraper(tuttosport_config).download_data_last_day()

