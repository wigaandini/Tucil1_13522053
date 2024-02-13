import numpy as np
import random

def read_file(filename):
    with open(filename, "r") as f:
        buffer_size = int(f.readline().strip())
        matrix_width, matrix_height = map(int, f.readline().split())
        matrix = []
        for _ in range(matrix_height):
            row = f.readline().split()
            matrix.append(row)
        number_of_sequences = int(f.readline().strip())
        sequences = []
        for _ in range(number_of_sequences):
            sequence = f.readline().split()
            reward = int(f.readline().strip())
            sequences.append((sequence, reward))
    return buffer_size, matrix, sequences, matrix_width, matrix_height


def arrange_seq(seq_num, max_seq_size, token_name):
    sequences_with_points = []
    for _ in range(seq_num):
        seq_size = random.randint(2, max_seq_size)
        seq = random.sample(token_name, k=seq_size)
        points = random.randint(-50, 50)
        sequences_with_points.append((seq, points))
    return sequences_with_points


def arrange_matrix(matrix_height, matrix_width, tokens):
    matrix = []
    for i in range(matrix_height):
        row = [random.choice(tokens) for j in range(matrix_width)]
        matrix.append(row)
    return matrix


def manual_input():
    number_of_unique_tokens = int(input("\nEnter the number of unique tokens: "))
    tokens = []
    while True:
        token_name = input("Enter the tokens: ").split()
        tokens.extend(token_name)
        # Cek jumlah token sama/ga sama number unique tokens
        if len(token_name) == number_of_unique_tokens:
            break
        else:
            print("The total number of tokens does not match the number of unique tokens. Please try again.")
    buffer_size = int(input("Enter the buffer size: "))
    matrix_height, matrix_width = map(int, input("Enter the matrix_height and matrix_width (separated by space): ").split())
    seq_num = int(input("Enter the number of sequences: "))
    max_seq_size = int(input("Enter the max size of the sequence: "))
    matrix = arrange_matrix(matrix_height, matrix_width, tokens)
    sequences = arrange_seq(seq_num, max_seq_size, token_name)
    
    return buffer_size, matrix, sequences, matrix_width, matrix_height, tokens, seq_num, max_seq_size


