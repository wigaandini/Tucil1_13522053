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
    matrix2 = np.random.choice(tokenName2, size=(row2, col2))
    sequences2 = generate_sequences(seqNum2, maxSeqSize2, tokenName2)
    sequences2 = [(str(sequence), points) for sequence, points in sequences2]
    print("Random sequences:", sequences2)

    return token2, tokenName2, buffer2, row2, col2, seqNum2, maxSeqSize2, matrix2, sequences2

def generate_random_sequence(token_names, max_size):
    sequence_size = random.randint(2, max_size)  # At least 2 tokens in a sequence
    return random.sample(token_names, sequence_size)  # Randomly select tokens for the sequence

def generate_sequences(num_sequences, max_seq_size, token_names):
    sequences = []
    for _ in range(num_sequences):
        sequence = generate_random_sequence(token_names, max_seq_size)
        points = random.randint(10, 50)  # Random points between 10 and 50
        sequences.append((sequence, points))
    return sequences

# def getMatrix(matrix, row, col):
#     for i in range(row):
#         for j in range(col):
#             print(matrix[i][j], end=" ")
#         print() 