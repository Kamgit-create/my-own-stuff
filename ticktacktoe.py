import itertools


def board_to_str(board: list) -> str:
    returning_list = []
    for i, cell in enumerate(board):
        if cell.owner == "":
            returning_list.append(i + 1)
        else:
            returning_list.append(cell.owner)

    returning_value = (f"{returning_list[0]} {returning_list[1]} {returning_list[2]}\n"
                       f"{returning_list[3]} {returning_list[4]} {returning_list[5]}\n"
                       f"{returning_list[6]} {returning_list[7]} {returning_list[8]}")

    return returning_value


class Player:
    def __init__(self, player_id: str, name: str, amount_of_wins: int):
        self.id = player_id  # "X" | "O" | ""
        self.name = name
        self.amount_of_wins = amount_of_wins

    def get_a_move(self) -> int:
        return int(input())


class Cell:
    def __init__(self, number: int):
        self.number: int = number
        self.owner: str = str(number)


class Board:
    def __init__(self):
        """
        1 2 3
        4 5 6
        7 8 9
        """
        self.cells = [Cell(i) for i in range(1, 10)]

    def change_cell_by_number(self, player: Player, cell_number: int):
        self.cells[cell_number - 1].owner = player.id

    def check_winner(self) -> str:
        """Returns "X" if X won, "O" if O won, "D" if draw and "" if none of these"""
        cells = self.cells

        def check_for_winner(player_id: str):
            """Checks if player with `player_id` is winner"""
            # checking rows
            if cells[0].owner == cells[1].owner == cells[2].owner == player_id or \
                    cells[3].owner == cells[4].owner == cells[5].owner == player_id or \
                    cells[6].owner == cells[7].owner == cells[8].owner == player_id:
                return player_id
            # checking columns
            if cells[0].owner == cells[3].owner == cells[6].owner == player_id or \
                    cells[1].owner == cells[4].owner == cells[7].owner == player_id or \
                    cells[2].owner == cells[5].owner == cells[8].owner == player_id:
                return player_id
            # checking diagonals
            if cells[0].owner == cells[4].owner == cells[8].owner == player_id or \
                    cells[2].owner == cells[4].owner == cells[6].owner == player_id:
                print(f"line 75, winner = {player_id}")

            return ""  # empty string = no winner

        winner = check_for_winner("X")
        if winner:
            return winner
        winner = check_for_winner("O")
        if winner:
            return winner
        for cell in cells:
            if cell.owner not in ("X", "O"):
                return ""
        return "D"


class Game:
    def __init__(self):
        self.state = Board()
        player_1 = Player("X", "player_1_default_name", 0)
        player_2 = Player("O", "player_2_default_name", 0)
        self.players = [player_1, player_2]

    def print_board(self):
        print(board_to_str(self.state.cells))

    def make_a_move(self, player: Player):
        while True:
            print()
            self.print_board()
            try:
                player_move = int(
                    input(f"It's {player.name}'s turn! Enter number of cell "))
                if player_move < 1 or player_move > 9:
                    print("Invalid move!")
                    continue
            except ValueError:
                print("Wrong value!")
            else:
                if self.state.cells[player_move - 1].owner in ("X", "O"):
                    print("Invalid move!")
                    continue
                else:
                    return player_move

    def launch_one_game(self, _multiple: bool = False):
        if not _multiple:
            player_1_name = input("Enter player 1 name: ")
            player_2_name = input("Enter player 2 name: ")
            self.players[0].name = player_1_name
            self.players[1].name = player_2_name

        # making a move iteration
        for player in itertools.cycle(self.players):
            # safely getting a move from a player
            player_move = self.make_a_move(player)

            self.state.change_cell_by_number(
                player, self.state.cells[player_move - 1].number)  # making a move

            # checking if there is a winner and if so closing session
            winner = self.state.check_winner()
            if winner == "X":
                winner = self.players[0]
            elif winner == "O":
                winner = self.players[1]

            if winner == "D":
                print("It's draw! Nice play!")
                if _multiple:
                    print(
                        f"{self.players[0].name} won {self.players[0].amount_of_wins} times")
                    print(
                        f"{self.players[1].name} won {self.players[1].amount_of_wins} times")
                    self.state = Board()
                break
            elif winner:  # if not draw and there is a winner
                self.print_board()
                print(f"{winner.name} is the winner! Congrats!")
                winner.amount_of_wins += 1
                if _multiple:
                    print(
                        f"{self.players[0].name} won {self.players[0].amount_of_wins} times")
                    print(
                        f"{self.players[1].name} won {self.players[1].amount_of_wins} times")
                    self.state = Board()
                if winner != self.players[0]:
                    self.players = self.players[::-1]
                break

    def launch_games(self):
        player_1_name = input("Enter player 1 name: ")
        player_2_name = input("Enter player 2 name: ")
        self.players[0].name = player_1_name
        self.players[1].name = player_2_name

        while True:
            self.launch_one_game(_multiple=True)

            replay = input("Do you want to play again? (yes/no) ")
            if replay.lower() in ("yes", "y"):
                print("Launching another one")
            else:
                print("Got it. See you later!")
                return


if __name__ == "__main__":
    game = Game()
    game_mode = input("Launch single game (s) or multiple games (m)? ")
    if game_mode.lower() == "s":
        print("Launching single game")
        game.launch_one_game()
    elif game_mode.lower() == "m":
        print("Launching a series of games")
        game.launch_games()
