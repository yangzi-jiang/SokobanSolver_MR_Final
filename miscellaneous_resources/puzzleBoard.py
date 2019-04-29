import random
import math

POSSIBLE_MOVES = dict()
# generatedProblems = []
POSSIBLE_MOVES[0] = [1,3]
POSSIBLE_MOVES[1] = [0,2,4]
POSSIBLE_MOVES[2] = [1,5]
POSSIBLE_MOVES[3] = [0,4,6]
POSSIBLE_MOVES[4] = [1,3,5,7]
POSSIBLE_MOVES[5] = [2,4,8]
POSSIBLE_MOVES[6] = [3,7]
POSSIBLE_MOVES[7] = [4,6,8]
POSSIBLE_MOVES[8] = [5,7]

class Board(object):
   
    # boardState = [0,1,2,3,4,5,6,7,8,9]

    def __init__(self, numMoves, boardState):
        self.numMoves = numMoves
        self.boardState = boardState
        self.dimension = 3
        self.prevState = None
        self.h1Val = None
        self.h2Val = None
        self.h3Val = None


        
    def getMoves(self, tileIndex):
        return POSSIBLE_MOVES[tileIndex]

    
    def getRow(self,index):

        if(index < 3):
            return 0
        elif (index < 6):
            return 1
        else:
            return 2

    def calch1(self):

        numMisplaced = 0
        for i in range(len(self.boardState)):
            
            if (self.boardState[i] != i and self.boardState[i] != 0):
                numMisplaced += 1

        return numMisplaced

    def calch2(self):

        numMisplaced = 0
        bleh = []
        for i in range(len(self.boardState)):
            if (self.boardState[i] != i and self.boardState[i] != 0):

                #column + row
                numMisplaced += math.fabs(self.boardState[i] % 3 - i % 3) + math.fabs( self.getRow(self.boardState[i]) - self.getRow(i) )
                # bleh.append(math.fabs(self.boardState[i] % 3 - i % 3) + math.fabs( self.getRow(self.boardState[i]) - self.getRow(i) ))


        # print (bleh)
        return numMisplaced
    
    def calch3(self):
        tempList = self.boardState[:]
        count = 0
        for i in range(len(tempList)):
            if (i != 0):
                blankInd = tempList.index(0)
                source = tempList.index(blankInd)

                tempVal = tempList[source]
                tempList[source] = tempList[blankInd]
                tempList[blankInd] = tempVal

                count+=1
        return count


    #Commit the move to the board
    def doMove(self, source, target):

        blankInd = self.boardState.index(0)

        if (source != blankInd):
            #Invalid move!!!!!
            return False

        else:

            self.prevState = self.boardState

            tempVal = self.boardState[target]
            self.boardState[target] = self.boardState[blankInd]
            self.boardState[blankInd] = tempVal

            #Fair move!!!!
            return True



    # def updateBoard(newBoard):
    #     return

    # def switchTiles(self, sourceInd, targetV):
    #     sourceInd = self.boardState.index(source)
    #     targetInd = self.boardState.index(targetVal)
    #     temp = targetInd
    #     sourceInd = 

    def simMoves(self):
        numSimMoves = random.randrange(1, 50, 1)
        # print("Simulated moves:", numSimMoves)

        for i in range(numSimMoves):
            blankInd = self.boardState.index(0)
            possibleMoves = self.getMoves(blankInd)
            chosenMove = random.choice(possibleMoves)

            tempVal = self.boardState[chosenMove]
            self.boardState[chosenMove] = self.boardState[blankInd]
            self.boardState[blankInd] = tempVal

        # print("New Board State:", self.boardState)
        return self.boardState

    def printBoard(self):
        for i in range(3):
            if (i == 0):
                print (self.boardState[0], self.boardState[1], self.boardState[2])
                # print()
            elif (i == 1):
                print (self.boardState[3], self.boardState[4], self.boardState[5])
                # print()
            else:
                print (self.boardState[6], self.boardState[7], self.boardState[8])
                # print()

        return




# def main():
#     # print("Test")

#     # problemList generatedProblems

#     board = Board(-1, [0,1,2,3,4,5,6,7,8] )
#     board.createDict()
    
#     # problemSet =  genRandProblems(board)


#     for item in problemSet:
#         # print(item.boardState)
#         item.printBoard()
#         # print(item)
#         print("_________________________")
#         continue

# if __name__ == "__main__":
#     main()
