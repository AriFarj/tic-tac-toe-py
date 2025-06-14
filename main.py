def create_cells():
    created_cells = []
    for _ in range(0, 3):
        row = []
        for _ in range(0, 3):
            row.append(" ")
        created_cells.append(row)
    return created_cells


def print_board(cell_list):
    for row in range(0, 3):
        print(
            f" {cell_list[row][0]} | {cell_list[row][1]} | {cell_list[row][2]}\n-----------"
        )


def input_cell(cell_list):
    row = int(input("State row number 1-3: \n")) - 1
    item = int(input("State item number 1-3: \n")) - 1
    sign = (input("state sign (x\\y): \n")).upper()

    cell_list[row][item] = sign
    return cell_list


cells = create_cells()
print_board(cells)
input_cell(cells)
print_board(cells)
