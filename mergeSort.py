from arrays import Array

def mergeSort(lyst):
    # lyst          list being sorted
    for i in xrange(1, 10)
    # copyBuffer    temporary space needed during merge
    copyBuffer = Array(len(lyst))
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst) - 1)

def mergeSortHelper(lyst, copyBuffer, low, high):
    # lyst          list being sorted
    # copyBuffer    temporary space needed during merge
    # low, high     bounds of sublist
    # middle        midpoint of sublist
    if low < high:
        low = lyst[0]
        high = lyst[len(lyst) - 1]
        middle = (low + high) / 2
        mergeSortHelper(lyst, copyBuffer, low, middle)
        mergeSortHelper(lyst, copyBuffer, middle + 1, high)
        merge(lyst, copyBuffer, low, middle, high)

def merge(lyst, copyBuffer, low, middle, high):
    # lyst          list being sorted
    # copyBuffer    temporary space needed during merge
    # low, high     bounds of sublist
    # middle        midpoint of sublist
    # middle + 1    beginning of the second sorted sublist
    # high          end of second sorted sublist

    # Initialize i1 and i2 to the first items in each sublist
    i1 = low
    i2 = middle + 1

    # Interleave items from the esublists into the
    # copyBuffer in such a way that order is maintained.
    for i in xrange(low, high + 1):
        if i1 > middle:
            copyBuffer[i] = lyst[i2]
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = lyst[i1]
            i1 += 1
        elif lyst[i1] > lyst[i2]:
            copyBuffer[i] = lyst[i1]
            i1 += 1
        else:
            copyBuffer[i] = lyst[i2]
            i2 += 1
    for i in xrange(low, high + 1):
        lyst[i] = copyBuffer[i]
