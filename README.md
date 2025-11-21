#  CHALLENGE DEV : DUEL D'IA PUISSANCE 4

##  Objectif du Challenge
Le but est de développer la meilleure Intelligence Artificielle (IA) possible pour jouer et gagner au Puissance 4. Votre IA devra implémenter l'algorithme Minimax et son optimisation Alpha-Beta Pruning pour anticiper les coups de l'adversaire.

 1. Prérequis et InstallationVous devez tous les deux installer la librairie graphique pygame pour utiliser l'arène visuelle.Installez Pygame :Ouvrez votre terminal et exécutez la commande :Bashpip install pygame

Structure du Répertoire :Assurez-vous que votre dossier de travail contient ces trois fichiers pour pouvoir 

 ├── 📄 graphical_arena.py   # Le moteur de jeu (L'Arbitre - NE PAS MODIFIER)
 ├── 📄 mon_ia.py            # Votre code d'IA
 └── 📄 test_run.py          # Le script pour lancer un match

## 2. Le Contrat de Code (Votre Tâche)
Votre unique mission est de remplir la classe CustomAI située dans votre fichier (mon_ia.py).Le contrat de méthode est strict : toute déviation entraînera une disqualification.

```python
__init__(self, player_id)Constructeur. Stocke si vous êtes le joueur 1 (Rouge) ou 2 (Jaune).get_best_move(self, board)La fonction clé. Elle reçoit l'état du plateau et doit renvoyer la meilleure colonne à jouer (un entier entre 0 et 6).La Signature Requise :Pythonclass CustomAI:
    def __init__(self, player_id):
        # Ici, vous pouvez définir la profondeur de calcul souhaitée, etc.
        pass 

    def get_best_move(self, board):
        # Vous devez implémenter ici l'algorithme Minimax / Alpha-Beta.
        # N'oubliez pas de gérer les colonnes qui sont déjà pleines !
        return colonne_choisie # (Entier 0 à 6)

```

##  3. Lancement et DuelPour tester votre IA contre celle de votre ami ou contre l'IA RandomAI :

Placez les fichiers : Placez la classe CustomAI de votre ami (renommée en PoteAI par exemple) dans le même dossier (fichier pote_ia.py).Éditez test_run.py pour importer les deux classes et les instancier avant de les passer à l'arène :
```python
Exemple de lancement dans test_run.py
from graphical_arena import GraphicalArena
from mon_ia import CustomAI as MonIA
from pote_ia import CustomAI as PoteIA # Si vous testez avec l'IA du pote

p1 = MonIA(1)
p2 = PoteIA(2) # Ou RandomAI(2) si vous jouez contre le hasard

arena = GraphicalArena(p1, p2)
arena.play()
```

### Lancez le match : 
```python
test_run.py
```

 4. Critères de Victoire
 Le duel sera jugé sur une série de 10 parties, en alternant l'ordre de jeu (Joueur 1 vs Joueur 2) à chaque manche pour éliminer l'avantage du premier coup.
 
 - Efficacité (60%) : Le nombre de victoires total.
 
 - Vitesse/Optimisation (30%) : L'IA qui arrive à calculer le plus profondément (Minimax Alpha-Beta) dans la limite de temps impartie.
 
 - Qualité du Code (10%) : Clarté et propreté du code source.Que le meilleur algorithme gagne !