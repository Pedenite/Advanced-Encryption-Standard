def convert_matrix(block):
    res = [[] for _ in range(4)]
    for i in range(len(res)):
        for j in range(4):
            res[i].append(block[i+(4*j)])

    return res
