import pandas as pd

class Player:
    def __init__(self, series):
        self.code = series.code
        self.squadra = series.squadra
        self.giocatore = series.giocatore
        self.ruolo = series.ruolo
        self.quotazione = series.quotazione
        self.partite_giocate = series.partite_giocate
        self.gol_fatti_subiti = series.gol_fatti_subiti
        self.assist = series.assist
        self.ammonizioni = series.ammonizioni
        self.espulsioni = series.espulsioni
        self.rigori_tirati = series.rigori_tirati
        self.rigori_realizzati = series.rigori_realizzati
        self.rigori_sbagliati = series.rigori_sbagliati
        self.rigori_parati = series.rigori_parati
        self.media_voto = series.media_voto
        self.media_magic_voto = series.media_magic_voto
        self.media_punti = series.media_punti
        self.yyss = series.yyss
        self.is_T = series.is_T
        self.w_media_magic_voto = series.w_media_magic_voto
        self.w_media_punti = series.w_media_punti
        self.forcast_quotazione = series.forcast_quotazione


