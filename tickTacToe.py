def sum(a, b, c):
    return a + b + c
def printBorad(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print("<--------------->")
    print(f"{zero} | {one} | {two}")
    print(f"--|---|---")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")

def checkWin(xState,zState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            return 1
        if (sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O won the game")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    trun = 1 # 1 for X and 0 for O
    available = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    while True:
        printBorad(xState, zState)
        print("------Welcome to Tick Tac Toe------")
        print(f"Choose value from the availble points: {available}")
        if trun == 1:
            print("X's Chances")
            value = int(input("Enter the value: "))
            xState[value] = 1
            available.remove(value)
        else:
            print("O's Chances")
            value = int(input("Enter the value: "))
            zState[value] = 1
            available.remove(value)
        result = checkWin(xState,zState)
        if result != -1:
            printBorad(xState,zState)
            if result == 1:
                print("X won the game")
            elif result == 0:
                print("O won the game")
            print("Match over...")
            break
        trun = 1 - trun