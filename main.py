class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


def create_cells():
    created_cells = [" "] * 9
    return created_cells


def print_board(cell_list):
    print(f"{"\n"*3}")
    for row in range(0, 3):
        print(
            f" {cell_list[row*3]} | {cell_list[row*3+1]} | {cell_list[row*3+2]}\n-----------"
        )


def input_cell(cell_list):
    # sample_cells = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # print_board(sample_cells)
    cell = int(input("State row number 1-9: \n")) - 1
    if cell_list[cell] == " ":
        sign = (input("state sign (x\\o): \n")).upper()
        cell_list[cell] = sign
    else:
        print("That cell is already taken! Try again")
    return cell_list


def check_marks(a, b, c):
    return a == b and b == c


def check_if_game_over():
    if cells[0] != " " and (
        check_marks(cells[0], cells[1], cells[2])
        or check_marks(cells[0], cells[3], cells[6])
        or check_marks(cells[0], cells[4], cells[8])
    ):
        return True
    if cells[4] != " " and (
        check_marks(cells[3], cells[4], cells[5])
        or check_marks(cells[2], cells[4], cells[6])
        or check_marks(cells[1], cells[4], cells[7])
    ):
        return True
    if cells[8] != " " and (
        check_marks(cells[6], cells[7], cells[8])
        or check_marks(cells[2], cells[5], cells[8])
    ):
        return True
    return False


def next_turn(player):
    
    pass


cells = create_cells()
player1 = Player("Ari", "X")
player2 = Player("Computer", "Y")
print(player1.name, player1.sign)


game_on = True
while game_on:
    input_cell(cells)
    print_board(cells)
