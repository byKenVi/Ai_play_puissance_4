from graphical_arena import GraphicalArena, RandomAI
from mon_ia import CustomAI  # Importe TA classe (change le nom du fichier si besoin)

# Création des joueurs
# Tu es le Joueur 1 (Rouge), l'IA Hasard est le Joueur 2 (Jaune)
mon_robot = CustomAI(1)
sparring_partner = RandomAI(2)

# Lancement de l'arène
print("Lancement du match d'entraînement...")
arena = GraphicalArena(mon_robot, sparring_partner)
arena.play()