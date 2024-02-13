def collect_possible_path(matrix, buffer_size):
    def check_move(row, col):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and (row, col) not in used

    def find_path(row, col, curr_buffer_length, vertical):
        used.add((row, col))
        curr_token.append(matrix[row][col]) 
        curr_coor.append((col + 1, row + 1))
        if curr_buffer_length == buffer_size - 1:
            seq.append(curr_token[:])
            coor.append(curr_coor[:])
        else:
            if vertical:
                moves = [(1, 0), (-1, 0)]
            else:
                moves = [(0, 1), (0, -1)]

            for i, j in moves:
                curr_row, curr_col = row, col
                for _ in range(buffer_size - curr_buffer_length):
                    curr_row, curr_col = curr_row + i, curr_col + j
                    if check_move(curr_row, curr_col):
                        find_path(curr_row, curr_col, curr_buffer_length + 1, not vertical)

        used.remove((row, col))
        curr_token.pop()
        curr_coor.pop()

    seq, coor = [], [] # Store semua path
    curr_coor, curr_token = [], [] # Store per path
    used = set() # Buat detect dia udah pernah dipake ato belom, kalo udah berarti diskip
    
    for k in range(len(matrix[0])):
        find_path(0, k, 0, True)
    return seq, coor


# Buat cek apakah sequence ada di path
def is_subsequence(sequence, path):
    sequence_length = len(sequence)
    path_length = len(path)

    for i in range(path_length - sequence_length + 1):
        if path[i:i+sequence_length] == sequence:
            return True
    return False


# Buat hitung point dari setiap path sesuai dengan sequence yang ada
def count_points(seq, path):
    points = {tuple(sequence[0]): 0 for sequence in seq}  # Convert list to tuple here
    for sub_path in seq:
        if is_subsequence(sub_path[0], path):
            points[tuple(sub_path[0])] += sub_path[1]  # Convert list to tuple here
    return points


# Buat store semua point dari setiap path yang mungkin
def collect_possible_point(seq, path):
    arr_point = []
    for i in range(len(path)):
        points = count_points(seq, path[i])
        total_points = sum(points.values())
        arr_point.append(total_points)
    return arr_point
