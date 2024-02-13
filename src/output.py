import os
from pathlib import Path

# Saving file to folder "saved"
def save_file(file_name, possible_point, max_point, path_choosen, coordinates, exe_time):
    path = Path().absolute()
    file_path = str(path) + "\\src\\" + "\\saved\\" + file_name
    with open(filepath, "w") as f:
        f.write(" ___  _ _  ___  ___  ___  ___  _ _  _ _  _ __   ___  ___  ___  ___    ___  ___  ___  ___  ___  _ _    ___  ___  ___  ___  ___  ___  ___  _  \n") 
        f.write("|  _]| | || . ]| __]| . \| . \| | || \ || / /  [_  ]|   ||_  ||_  |  | . ]| . \| __]| . ||  _]| | |  | . \| . \| . ||_ _|| . ||  _]| . || |  \n")
        f.write("| [__\   /| . \| _] |   /|  _/| | ||   ||  \    / / | / | / /  / /   | . \|   /| _] |   || [__|   |  |  _/|   /| | | | | | | || [__| | || |_ \n")
        f.write("`___/ |_| |___/|___]|_\_\|_|   \__||_\_||_\_\  [___] \__|/_/  /_/    |___/|_\_\|___]|_|_|`___/|_|_|  |_|  |_\_\`___' |_| `___'`___/`___'|___|\n\n")
        if not possible_point:
            f.write("No possible path found.")
        else:
            f.write("Maximum point: {} \n".format(max_point))
            f.write("Final sequence: ")
            for i in range(len(path_choosen)):
                f.write(path_choosen[i])
                if i != len(path_choosen) - 1:
                    f.write(" ")
            f.write("\n")
            f.write("Steps that used: {}\n".format(len(coordinates) - 1))
            f.write("Final coordinate: \n")
            for i in range(len(coordinates)):
                f.write("{} , {}\n".format(coordinates[i][0], coordinates[i][1]))
            f.write("Execution time: {} ms\n".format(exe_time))