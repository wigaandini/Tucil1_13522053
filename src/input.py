import numpy as np
import random

def readFile(fileName):
    with open(fileName, "r") as file:
        buffer1 = int(file.readline().strip())
        row1, col1 = map(int, file.readline().split())
        matrix1 = []
        for _ in range(row1):
            row_data = list(map(str, file.readline().strip().split()))
            matrix1.append(row_data)
        matrix1 = np.array(matrix1)
        seqNum1 = int(file.readline().strip())
        sequences1 = []
        for _ in range(seqNum1):
            seq = str(file.readline().strip().split())
            points = int(file.readline().strip())
            sequences1.append((seq, points))
    
    return buffer1, row1, col1, matrix1, seqNum1, sequences1


def manualInput():
    token2 = int(input("Enter the number of unique tokens: "))
    tokenName2 = input("Enter the tokens: ").split()
    buffer2 = int(input("Enter the buffer size: "))
    row2, col2 = map(int, input("Enter the row and column size: ").split())
    seqNum2 = int(input("Enter the number of sequences: "))
    maxSeqSize2 = int(input("Enter the max size of the sequence: "))
    matrix2 = np.random.choice(tokenName2, size=(row2, col2)) # Random matriks dari tokenName2
    sequences2 = arrangeSeq(seqNum2, maxSeqSize2, tokenName2)
    sequences2 = [(str(sequence), points) for sequence, points in sequences2] # Formatting jadi array of tuple (sequence, points) 
    print("Random sequences:", sequences2)

    return token2, tokenName2, buffer2, row2, col2, seqNum2, maxSeqSize2, matrix2, sequences2


def randomSeq(tokenName, maxSeqSize):
    seqSize = random.randint(2, maxSeqSize) # Ukuran sequence dibuat random antara 2 - maxSeqSize
    return random.sample(tokenName, seqSize) # Sequence dibuat random dari tokenName yang ada


def arrangeSeq(seqNum, maxSeqSize, tokenName):
    sequences = []
    for _ in range(seqNum):
        sequence = randomSeq(tokenName, maxSeqSize)
        points = random.randint(10, 50) # Poin dibuat random antara 10 - 50
        sequences.append((sequence, points))
    return sequences

# def getMatrix(matrix, row, col):
#     for i in range(row):
#         for j in range(col):
#             print(matrix[i][j], end=" ")
#         print() 