"""
Program: FloydsAlgorithm.py
Programmer: Daniel Botz
Pre-condition: A natural number for the number of vertices in a graph,
    then for each vertex, the weight (cost of movement) from that vertex
    to another vertex. If no adjected connection exists, then enter 'w'.
    After that, the numbers of 2 vertices so to find the shortest path 
    between them.
Post-condition: The weight adjacency matrix, the resulting table of weights,
    and the resulting tables of the shortest paths possible to compute.
    After that, it returns the shortest path between the 2 selected vertices.
"""

def isnumber(n):
    """Determines if the entry (integer or string) is a number."""
    N = str(n)
    if N.isdigit():
        return True
    else:
        return False

def weighMatrix(M):
    """Determines and returns two matrices: The first one represents the 
    costs of traveling for one vertex (corresponding to the row of the matrix)
    to another matrix (corresponding to the column of the matrix).
    The second matrix represent the highest index of a vertex traveled on
    from one vertex (row) to another (column)."""
    rows = len(M)
    cols = len(M[0])
    Weighed = M
    ShortPath = []
    totalM = 1
    for k in range(rows):
        ShortPath.append([])
        for j in range(cols):
            ShortPath[k].append(0)
            if isnumber(M[k][j]):
                totalM += int(M[k][j])
    for k in range(rows):
        for j in range(cols):
            if not isnumber(M[k][j]):
                Weighed[k][j] = totalM
    for mid in range(cols):
        for k in range(rows):
            for j in range(cols):
                if int(M[k][j]) > int(M[k][mid]) + int(M[mid][j]):
                    Weighed[k][j] = int(M[k][mid]) + int(M[mid][j])
                    ShortPath[k][j] = mid + 1
                else:
                    Weighed[k][j] = int(M[k][j])
    twoMatrices = [Weighed, ShortPath]
    return twoMatrices
    
def pathFinder(M, start, end):
    """Computes the shortest path for one vertex 'start' to another 'end'."""
    point = M[start-1][end-1]
    if point != 0:
        pathFinder(M, start, point)
        print "V" + str(point)
        pathFinder(M, point, end)
    
def main():
    adjMatrix = []
    ourEntry = raw_input("Enter n (the number of vertices in your graph): ")
    n = int(ourEntry)
    for count in range(n):
        adjMatrix.append([])
    print "Enter a list of numbers to represent the weights from\n\
    each vertex to all other vertices. If one connection does\n\
    not exists from one vertex to another, print 'w' in its place."
    for i in range(n):
        print "For vertex(" + str(i+1) + ")"
        adjRow = raw_input("Enter list (separate with spaces): ")
        adjMatrix[i] = adjRow.split()
        while len(adjMatrix[i]) != n:
            print "Remember that you must have a row length of " + str(n)
            adjRow = raw_input("Enter list: ")
            adjMatrix[i] = adjRow.split()
        adjMatrix[i][i] = 0
    for i in range(len(adjMatrix)):
        print adjMatrix[i]
    ourMatrices = weighMatrix(adjMatrix)
    print "Table of Weights"
    for row in range(n):
        print ourMatrices[0][row]
    print "Highest Indexes Passed Through"
    for row in range(n):
        print ourMatrices[1][row]
    print "Enter a pair of vertices (numbers only)."
    SecondToLastEntry = int(raw_input("Starting Vertex: "))
    LastEntry = int(raw_input("Ending Vertex: "))
    pathFinder(ourMatrices[1], SecondToLastEntry, LastEntry)
    
main()
