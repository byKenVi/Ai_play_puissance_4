import pygame
import sys
import time
import math

# --- CONFIGURATION GRAPHIQUE ---
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100  # Taille d'une case en pixels
RADIUS = int(SQUARESIZE / 2 - 5)

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)

# --- LOGIQUE DU JEU ---
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2

class GraphicalArena:
    def __init__(self, ai_player_1, ai_player_2):
        self.board = [[EMPTY for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
        self.players = {1: ai_player_1, 2: ai_player_2}
        self.turn = PLAYER_1
        
        # Initialisation Pygame
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Challenge IA Puissance 4")
        self.font = pygame.font.SysFont("monospace", 75)

    def draw_board(self):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                # Dessiner le rectangle bleu (le plateau)
                rect = (c * SQUARESIZE, (r + 1) * SQUARESIZE, SQUARESIZE, SQUARESIZE)
                pygame.draw.rect(self.screen, BLUE, rect)
                
                # Dessiner le cercle (vide ou pion)
                # Attention: Pygame dessine de haut en bas, notre logique est aussi de haut (0) en bas (5)
                center = (int(c * SQUARESIZE + SQUARESIZE / 2), int((r + 1) * SQUARESIZE + SQUARESIZE / 2))
                
                if self.board[r][c] == EMPTY:
                    pygame.draw.circle(self.screen, BLACK, center, RADIUS)
                elif self.board[r][c] == PLAYER_1:
                    pygame.draw.circle(self.screen, RED, center, RADIUS)
                elif self.board[r][c] == PLAYER_2:
                    pygame.draw.circle(self.screen, YELLOW, center, RADIUS)
        
        pygame.display.update()

    def is_valid_location(self, col):
        return self.board[0][col] == EMPTY

    def get_next_open_row(self, col):
        for r in range(ROW_COUNT-1, -1, -1):
            if self.board[r][col] == EMPTY:
                return r

    def winning_move(self, piece):
        # Vérification horizontale
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True
        # Vérification verticale
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True
        # Diagonales positives
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True
        # Diagonales négatives
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True
        return False

    def is_full(self):
        return all(self.board[0][c] != EMPTY for c in range(COLUMN_COUNT))

    def play(self):
        self.draw_board()
        game_over = False

        while not game_over:
            # Gestion des événements (pour pouvoir fermer la fenêtre)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if self.is_full():
                print("Match Nul !")
                game_over = True
                break

            current_ai = self.players[self.turn]
            
            # Petit délai pour que ce soit visible à l'oeil humain (500ms)
            pygame.time.wait(500) 
            
            # Copie du board pour l'IA
            board_copy = [row[:] for row in self.board]
            
            # L'IA réfléchit
            col = current_ai.get_best_move(board_copy)

            if col is not None and self.is_valid_location(col):
                row = self.get_next_open_row(col)
                self.board[row][col] = self.turn
                
                if self.winning_move(self.turn):
                    label = self.font.render(f"JOUEUR {self.turn} GAGNE!", 1, RED if self.turn == 1 else YELLOW)
                    self.screen.blit(label, (40, 10))
                    game_over = True
                
                self.turn = PLAYER_1 if self.turn == PLAYER_2 else PLAYER_2
                self.draw_board()
            else:
                print(f"Coup invalide ou crash IA Joueur {self.turn}")
                game_over = True

        # Attendre 5 secondes avant de fermer à la fin du match
        pygame.time.wait(5000)

# --- IA DE TEST (A REMPLACER PAR LES VOTRES) ---
import random
class RandomAI:
    def __init__(self, player_id):
        self.player_id = player_id
    def get_best_move(self, board):
        valid_cols = [c for c in range(7) if board[0][c] == 0]
        return random.choice(valid_cols) if valid_cols else None

if __name__ == "__main__":
    # C'est ici que tu importes ton IA et celle de ton pote
    # from mon_ia import MyAI
    # from son_ia import HisAI
    
    p1 = RandomAI(1)
    p2 = RandomAI(2)
    
    game = GraphicalArena(p1, p2)
    game.play()