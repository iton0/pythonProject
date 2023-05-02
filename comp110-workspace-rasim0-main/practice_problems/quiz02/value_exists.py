

def value_exists(dic: dict[str,int], val: int) -> bool:
    """Returns True or False if value is in dictionary."""
    exist: bool = False
    for keys in dic:
        if val == dic[keys]:
            exist = True
    return exist

