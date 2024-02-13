import os

# Saving file to folder "saved"
def save_file(filename, possible_point, max_point, path_choosen, coordinates, matrix, exe_time, over_capacity):
    save_folder = "saved"
    os.makedirs(save_folder, exist_ok=True)
    filepath = os.path.join(save_folder, filename)
    with open(filepath, "w") as f:
        if not possible_point:
            f.write("No possible path found.")
        else:
            f.write("{} \n".format(max_point))
            for i in range(len(path_choosen)):
                f.write(path_choosen[i])
                if i != len(path_choosen) - 1:
                    f.write(" ")
            f.write("\n")
            for i in range(len(coordinates)):
                f.write("{} , {}\n".format(coordinates[i][0], coordinates[i][1]))
            f.write("{} ms\n".format(exe_time))
