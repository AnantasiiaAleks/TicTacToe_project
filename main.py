import Game
import Player


player1 = Player.Player('Игрок 1', 'X')
player2 = Player.Player('Игрок 2', 'O')

game = Game.Game(player1, player2)
game.start_games()