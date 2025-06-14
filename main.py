def create_cells():
    created_cells = []
    for _ in range(0, 9):
        created_cells.append(" ")
    return created_cells


def print_board(cell_list):
    print(f"{"\n"*3}")
    for row in range(0, 3):
        print(
            f" {cell_list[row*3]} | {cell_list[row*3+1]} | {cell_list[row*3+2]}\n-----------"
        )



def input_cell(cell_list):
    sample_cells = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print_board(sample_cells)
    cell = int(input("State row number 1-9: \n")) - 1
    sign = (input("state sign (x\\o): \n")).upper()
    cell_list[cell] = sign
    return cell_list


cells = create_cells()
# cells[0] = "1"
# cells[1] = "2"
# cells[2] = "3"
# cells[3] = "4"
# cells[4] = "5"
# cells[5] = "6"
# cells[6] = "7"
# cells[7] = "8"
# cells[8] = "9"

# print_board(cells)
# input_cell(cells)
# print_board(cells)

game_on = True
while game_on:
    input_cell(cells)
    print_board(cells)