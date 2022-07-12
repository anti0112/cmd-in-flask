def get_query(cmd, val, file_list):
    if cmd == "filter":
        res = [x for x in file_list if val in x]
        return res
    
    if cmd == "map":
        res = [x.split()[int(val)] for x in file_list]
        return res
    
    if cmd == "unique":
        res = list(set(file_list))
        return res
    
    if cmd == "sort":
        reverse = val == "desc"
        res = sorted(file_list, reverse=reverse)
        return res
        
    if cmd == "limit":
        val = int(val)
        res = list(file_list)[:val]
        return res