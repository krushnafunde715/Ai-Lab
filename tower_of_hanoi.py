def tower_of_hanoi(n, source, auxiliry, destination):

    if n == 1:
        print("move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi( n-1, source, destination, auxiliry)

    print("move disk", n, "from", source, "to", destination)

    tower_of_hanoi( n-1, auxiliry, source, destination)

n = int(input("Enter number of disk: "))

tower_of_hanoi(n, 'A','B','C')

print("Total moves required:", 2**n -1 )