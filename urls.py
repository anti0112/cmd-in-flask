import re
from typing import Iterator, List, Any

def get_query(cmd: str, val: str, file_list: Iterator)-> List[Any]:
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
        res = list(file_list)[:int(val)]
        return res
    
    if cmd == "regex":
        reg = re.compile(val)
        res = list(filter(lambda x: reg.search(x), file_list))
        return res
    return []
    