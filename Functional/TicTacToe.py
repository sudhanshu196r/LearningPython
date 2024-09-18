
'''
    @Author: Sudhanshu Kumar
    @Date: 17-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 17-09-2024
    @Title : Python program for tic tac toe

'''


import random
class Util:
    @staticmethod
    def main():
        Util.startgame()

    @staticmethod
    def startgame():
        board = [['-' for _ in range(3)] for _ in range(3)]
        Util.printBoard(board)
        player = 'X'
        gameOver = False

        while not gameOver:
            Util.printBoard(board)
            print("\n\n")
            if player=='X':
                print("Enter row and column to insert : ")
                row = int(input())
                col = int(input())
                if board[row][col]=='-':
                    board[row][col]='X'
                    gameOver = Util.whoWon(board,player)
                    if gameOver:
                        print("You Won")
                    else:
                        player='O'
                else:
                    print("Already Filled")

            else:
                Util.printBoard(board)
                print("\n\n")
                row = random.randrange(0,3)
                col = random.randrange(0,3)
                if(board[row][col]=='-'):
                    board[row][col]='O'
                    gameOver = Util.whoWon(board,player)
                    if gameOver:
                        print("Computer Won")
                    else:
                        player='X'
                else:
                    print("Already Filled")


    @staticmethod
    def whoWon(board,player):
        """
        Description:
            Funtion to decide winner
        Parameters:
            board : it represents the current status of board
            player : it represents the current player
        Returns:
            It will return true or false if the current player is winner or not

    """


        for row in range(0,len(board)):
            if board[row][0]==player and board[row][1]==player and board[row][2]==player:
                return True
		
        for col in range(0,len(board)):
            if board[0][col]==player and board[1][col]==player and board[2][col]==player:
                return True
		
        if board[0][0]==player and board[1][1]==player and board[2][2]==player :
            return True
		
        if board[0][2]==player and board[1][1]==player and board[2][0]==player: 
            return True

        return False

    @staticmethod
    def printBoard(board):
        """
        Description:
            Funtion to print the board
        Parameters:
            board: It takes board as an inout
        Returns:
            It returns nothing

        """


        for row in board:
            print(" | ".join(row))
            print("-" * 9)


if __name__=="__main__":
    Util.main()
