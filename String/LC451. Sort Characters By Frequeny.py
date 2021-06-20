def frequenctSort(s):
    d1 = Counter(s).most_common()
    new_str = ''
    for i in d1:
        new_str += i[0]*i[1]
    return new_str

