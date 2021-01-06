import pandas as pd
from .Player import Player

class Players:
    def __init__(self, players_df):
        self.players_list = []
        print(type(players_df))
        for index, row in players_df.iterrows():
            print(index)
            self.players_list.append(Player(row))

        self.code = players_df.code.tolist()
        self.squadra = players_df.squadra.tolist()
        self.giocatore = players_df.giocatore.tolist()
        self.ruolo = players_df.ruolo.tolist()
        self.quotazione = players_df.quotazione.tolist()
        self.partite_giocate = players_df.partite_giocate.tolist()
        self.gol_fatti_subiti = players_df.gol_fatti_subiti.tolist()
        self.assist = players_df.assist.tolist()
        self.ammonizioni = players_df.ammonizioni.tolist()
        self.espulsioni = players_df.espulsioni.tolist()
        self.rigori_tirati = players_df.rigori_tirati.tolist()
        self.rigori_realizzati = players_df.rigori_realizzati.tolist()
        self.rigori_sbagliati = players_df.rigori_sbagliati.tolist()
        self.rigori_parati = players_df.rigori_parati.tolist()
        self.media_voto = players_df.media_voto.tolist()
        self.media_magic_voto = players_df.media_magic_voto.tolist()
        self.media_punti = players_df.media_punti.tolist()
        self.yyss = players_df.yyss.tolist()
        self.is_T = players_df.is_T.tolist()
        self.w_media_magic_voto = players_df.w_media_magic_voto.tolist()
        self.w_media_punti = players_df.w_media_punti.tolist()
        self.forcast_quotazione = players_df.forcast_quotazione.tolist()

