# Main Program

from input import *
from solver import *
from output import *
import os
import time
from pathlib import Path


# Inizialiation
print()
print("                                                Welcome to the Cyberpunk Hacker!                                  ")                                                                                                                                             
print(" ___  _ _  ___  ___  ___  ___  _ _  _ _  _ __   ___  ___  ___  ___    ___  ___  ___  ___  ___  _ _    ___  ___  ___  ___  ___  ___  ___  _  ") 
print("|  _]| | || . ]| __]| . \| . \| | || \ || / /  [_  ]|   ||_  ||_  |  | . ]| . \| __]| . ||  _]| | |  | . \| . \| . ||_ _|| . ||  _]| . || |  ")
print("| [__\   /| . \| _] |   /|  _/| | ||   ||  \    / / | / | / /  / /   | . \|   /| _] |   || [__|   |  |  _/|   /| | | | | | | || [__| | || |_ ")
print("`___/ |_| |___/|___]|_\_\|_|   \__||_\_||_\_\  [___] \__|/_/  /_/    |___/|_\_\|___]|_|_|`___/|_|_|  |_|  |_\_\`___' |_| `___'`___/`___'|___|")

print()
print("                 This program will help you to find the maximum point and the steps from the given matrix and sequences.                ")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                   Erdianti Wiga Putri Andini                                  ")
print("                                                         13522053 - K1                                          ")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
print()

# Input
print("=========== CHOOSE INPUT MODE ===========")
print("             File Input (1)")
print("            Manual Input (2)")
print("=========================================")
input_mode = int(input("\nChoice: "))

check = False
import os

while not check:
    # File input
    if input_mode == 1:
        check = True
        path = Path().absolute()
        file_name = input("Enter the file name: ")
        file_path = str(path) + "\\test\\" + file_name
        while not os.path.exists(file_path):
            print("File not found. Please try again.")
            file_name = input("Enter the file name: ")
            file_path = str(path) + "\\test\\" + file_name
        buffer_size, matrix, sequence, matrix_width, matrix_height = read_file(file_path)
        print()


    # Manual input
    elif input_mode == 2:
        check = True
        buffer_size, matrix, sequence, matrix_width, matrix_height, tokens, seq_num, max_seq_size = manual_input()
        print("\nMatrix: ")
        for i in range(matrix_height):
            for j in range(matrix_width):
                print(matrix[i][j], end=' ')
            print()
        print("\nSequences that used: ")
        for i in range(seq_num):
            print("Sequence:", sequence[i][0], "Point:", sequence[i][1])

    else:
        print("\nInvalid input. Please try again.")
        print("Choose the input mode: ")
        print("File Input (1)")
        print("Manual Input (2)")
        input_mode = int(input("\nChoice: "))

start = time.time()

# Cari kemungkinan semua path yang bisa dibuat dari elemen-elemen di matrix baris pertama
possible_path, coordinate = collect_possible_path(matrix, buffer_size)
possible_point = collect_possible_point(sequence, possible_path) # Cari point dari setiap path yang mungkin

print("=========== RESULT ===========")
if not possible_point:
    print("No possible path found.")
else:
    max_point = possible_point[0]
    for i in range(len(possible_point)):
        if possible_point[i] > max_point:
            max_point = possible_point[i]
            max_index = i
    print("Maximum point:", max_point)
    print("Steps that used:", len(possible_path[max_index]) - 1)

    # Print final sequence and coordinate
    print("Final sequence: ", end='')
    final_sequence = possible_path[max_index]
    for token in final_sequence:
        print(token, end=' ')

    print("\nFinal coordinate: ")
    final_coordinate = coordinate[max_index]
    for coor in final_coordinate:
        print(coor)

end = time.time()
total_waktu = round((end - start) * 1000, 3)
print()
print("Total waktu:", total_waktu, "ms")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
print("Do you want to save the result as text file? (Y/N)")
save = input("Choice: ")
if save == "Y" or save == "y":
    file_name = input("Enter the file name: ")
    save_file(file_name, possible_point, max_point, possible_path[max_index], coordinate[max_index], total_waktu)
    print("File has been saved as", file_name, "in the folder 'saved'.")
else:
    print("File not saved.")
print("Thank you for using this program!")