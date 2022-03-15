def unite_dict_arrays(dict1, dict2):
    for key in dict1.keys():
        dict1[key].append(dict2[key])