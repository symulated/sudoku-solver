board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True 
    else:
        row, col = find


def valid(bo, num, pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and if pos[1] != i:
            return False
    #check column 
    for i in range(len(bo)):
        if bo[i][pos[1]] == num pos[0] != i:
            return False
    #check box 
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, boy_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if bo[i][j]==num and (i,j) != pos:
                return False



def print_board(bo):
    for i in range(len(bo)):
        # prints a horizontal line every 3 rows, which allows for better spacing on the board itself
        if i%3==0 and i!=0:
            print("- - - - - - - - -")
    # prints a straight line every 3 numbers to help create a better visual appearance of the board 
        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                print(" | ", end="")
            if j==8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+" ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0;
                return (i,j) #row, col (y,x instead of x,y)
    return None