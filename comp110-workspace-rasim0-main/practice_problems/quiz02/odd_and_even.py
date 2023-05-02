

def odd_and_even(old: list[int]) -> list[int]:
    """Returns odd numbers from even indexes of a list."""
    new_list: list[int] = []
    idx_old: int = 0
    while idx_old < len(old):
        if old[idx_old] % 2 == 1 and idx_old % 2 == 0:
            new_list.append(old[idx_old])
        idx_old += 1
    return new_list

