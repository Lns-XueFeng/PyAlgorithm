
def sum_(li):
    total_sum = 0
    for i in li:
        total_sum += i
    return total_sum


def r_sum_(li):
    if not li:
        return None
    if len(li) == 1:
        return li[0]
    return li[0] + r_sum_(li[1:])


l = [1, 2, 3, 4, 5]
sum_(l)   # 15
r_sum_(l)   # 15
