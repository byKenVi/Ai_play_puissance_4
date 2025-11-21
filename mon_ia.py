import random

class CustomAI:
    def __init__(self, player_id):
        """
        Initialisation de l'IA.
        player_id : 1 (Rouge) ou 2 (Jaune).
        """
        self.player_id = player_id
        # Tu peux initialiser d'autres variables ici si besoin

    def get_best_move(self, board):
        """
        C'est ici que la magie opère.
        :param board: Tableau 6x7 (0=vide, 1=J1, 2=J2)
        :return: Un entier entre 0 et 6 (la colonne choisie)
        """
  