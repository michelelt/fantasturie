from pathlib import Path


data_structure_config={
    'data_root': Path('./data/'),
    # 'yyss': ['2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21'],
    # 'journals': ['gazzetta_dello_sport', 'corriere_dello_sport', 'tuttosport', 'fantagazzetta', 'gazzetta3plus']
}


players_config={
    'url': 'https://www.gazzetta.it/calcio/fantanews/statistiche/serie-a-%s/',
    'yyss': ['2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21'],
    'data_root': data_structure_config['data_root']
}

gazzetta_config={
    'data_root': data_structure_config['data_root'],
    'url': 'https://www.gazzetta.it/calcio/fantanews/voti/serie-a-%s/giornata-%d',
    'http_header': {
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    },
    'yyss': ['2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20'],
    'days_of_the_season': range(1, 39),
    'file_header': 'code,numero,giocatore,ruolo,ruolo_cod,voto,gol_fatti_subiti,assist,rigori_realizzati,rigori_sbagliati,autogol,ammonizioni,espulsioni,fantavoto,squadra,dots,yyss\n',
    'journal':'gazzetta_dello_sport'
}

corriere_dello_sport_config ={
    'data_root' : data_structure_config['data_root'],
    'url': 'https://www.fantapiu3.com/fantacalcio-storico-voti-corriere-sport-%s.php',
    'http_header' : {
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    },
    'yyss': ['2016-17', '2017-18', '2018-19', '2019-20', '2020-21'],
    'days_of_the_season': range(1, 39),
    'data_types' : {
        'dots':int,'giocatore':str, 'squadra':str, '?':str, 'ruolo':str, 'fantavoto':float,
        'voto':float, 'gol_fatti_subiti':float, 'ammonizioni':float, 'espulsioni':float, 'rigori_parati_segnati':float,
        'autogol':float, 'portiere_imbattuto':float
    },
    'header': ['dots','giocatore', 'squadra', '?', 'ruolo', 'fantavoto', 'voto', 'gol_fatti_subiti', 'ammonizioni', 'espulsioni',
               'rigori_parati_segnati', 'autogol', 'portiere_imbattuto'],
    'file_header': 'code,dots,giocatore,squadra,ruolo,fantavoto,voto,gol_fatti_subiti,ammonizioni,espulsioni,rigori_parati_segnati,autogol,portiere_imbattuto,yyss\n',
    'journal': 'corriere_dello_sport'
    }


tuttosport_config ={
    'data_root' : data_structure_config['data_root'],
    'url': 'https://www.fantapiu3.com/fantacalcio-storico-voti-tuttosport-%s.php',
    'http_header' : {
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    },
    'yyss': ['2016-17', '2017-18', '2018-19', '2019-20', '2020-21'],
    'days_of_the_season': range(1, 39),
    'data_types' : {
        'dots':int,'giocatore':str, 'squadra':str, '?':str, 'ruolo':str, 'fantavoto':float,
        'voto':float, 'gol_fatti_subiti':float, 'ammonizioni':float, 'espulsioni':float, 'rigori_parati_segnati':float,
        'autogol':float, 'portiere_imbattuto':float
    },
    'header': ['dots','giocatore', 'squadra', '?', 'ruolo', 'fantavoto', 'voto', 'gol_fatti_subiti', 'ammonizioni', 'espulsioni',
               'rigori_parati_segnati', 'autogol', 'portiere_imbattuto'],
    'file_header': 'code,dots,giocatore,squadra,ruolo,fantavoto,voto,gol_fatti_subiti,ammonizioni,espulsioni,rigori_parati_segnati,autogol,portiere_imbattuto,yyss\n',
    'journal': 'tuttosport'

}

fantagazzetta_config ={
    'data_root' : data_structure_config['data_root'],
    'url': 'https://www.fantapiu3.com/fantacalcio-storico-voti-fantagazzetta-%s.php',
    'http_header' : {
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    },
    'yyss': ['2018-19', '2019-20', '2020-21'],
    'days_of_the_season': range(1, 39),
    'data_types' : {
        'dots':int,'giocatore':str, 'squadra':str, '?':str, 'ruolo':str, 'fantavoto':float,
        'voto':float, 'gol_fatti_subiti':float, 'ammonizioni':float, 'espulsioni':float, 'rigori_parati_segnati':float,
        'autogol':float, 'portiere_imbattuto':float
    },
    'header': ['dots','giocatore', 'squadra', '?', 'ruolo', 'fantavoto', 'voto', 'gol_fatti_subiti', 'ammonizioni', 'espulsioni',
               'rigori_parati_segnati', 'autogol', 'portiere_imbattuto'],
    'file_header': 'code,dots,giocatore,squadra,ruolo,fantavoto,voto,gol_fatti_subiti,ammonizioni,espulsioni,rigori_parati_segnati,autogol,portiere_imbattuto,yyss\n',
    'journal': 'fantagazzetta'

}

gazzetta3plus_config ={
    'data_root' : data_structure_config['data_root'],
    'url': 'https://www.fantapiu3.com/fantacalcio-storico-voti-gazzetta-sport-%s.php',
    'http_header' : {
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    },
    'yyss': ['2005-06', '2006-07', '2007-08', '2008-09', '2009-10', '2010-11', '2011-12', '2012-13',
             '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21'],
    'days_of_the_season': range(1, 39),
    'data_types' : {
        'dots':int,'giocatore':str, 'squadra':str, '?':str, 'ruolo':str, 'fantavoto':float,
        'voto':float, 'gol_fatti_subiti':float, 'ammonizioni':float, 'espulsioni':float, 'rigori_parati_segnati':float,
        'autogol':float, 'portiere_imbattuto':float
    },
    'header': ['dots','giocatore', 'squadra', '?', 'ruolo', 'fantavoto', 'voto', 'gol_fatti_subiti', 'ammonizioni', 'espulsioni',
               'rigori_parati_segnati', 'autogol', 'portiere_imbattuto'],
    'file_header': 'code,dots,giocatore,squadra,ruolo,fantavoto,voto,gol_fatti_subiti,ammonizioni,espulsioni,rigori_parati_segnati,autogol,portiere_imbattuto,yyss\n',
    'journal': 'gazzetta_dello_sport_3plus'

}
