testlist = [9,5,2,6,8,10,14,13]

def insertionSort(list):
    for i in range(1, len(list)):
        prev = i-1
        while (prev >= 0 and list[i] < list[prev]):
            temp = list[prev]
            list[prev] = list[i]
            list[i] = temp
            prev -= 1 #prev = prev-1
            i -= 1
    print(list)

if __name__ == "__main__":
    insertionSort(testlist)
