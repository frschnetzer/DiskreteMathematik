def comp(list1, list2):
    result = []
    for x1,y1 in list1:
        for x2, y2 in list2:
            if y1 == x2:
                result.append((x1, y2))
    return result

def main():
    print(list(comp({(1,2), (2,3)}, {(2,10), (3,5)}))) # erwartung: (1,10), (2,5)
main()