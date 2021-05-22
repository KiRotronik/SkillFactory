def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

def count(array, element):
    count_ = 0
    for i in array:
        if i == element:
            count_ += 1
    return count_

array = list(map(int, input().split()))
element = int(input())


