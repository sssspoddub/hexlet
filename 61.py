def get_intersection_of_sorted_lists(data1: list, data2: list) -> list:
    index1, index2 = 0, 0
    intersection: list = []

    while index1 < len(data1) and index2 < len(data2):
        if data1[index1] == data2[index2]:
            if not intersection or intersection[-1] != data1[index1]:
                intersection.append(data1[index1])
            index1 += 1
            index2 += 1
        elif data1[index1] < data2[index2]:
            index1 += 1
        else:
            index2 += 1

    return intersection
