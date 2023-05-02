

def short_words(old: list[str]) -> list[str]:
    """Returns words in list that are shorter than 5 characters. If the character is 5 characters or more will say that it is too long."""
    new_list: list[str] = []
    idx: int = 0
    while idx < len(old):
        if len(old[idx]) >= 5:
            print(f"{old[idx]} is too long!")
        else: 
            new_list.append(old[idx])
        idx += 1
    return new_list

