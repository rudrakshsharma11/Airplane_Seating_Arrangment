filled = 0
number = int(input("Enter no of passengers"))
row = 0
tempFilled = -1
size = int(input("Enter size"))
seatsGrid = []
inQueue = 0
total = 0
# input
for x in range(size):
    seatsGrid.append([int(y) for y in input().split()])

for i in range(len(seatsGrid)):
    for j in range(len(seatsGrid[i]) - 1):
        total += seatsGrid[i][j] * seatsGrid[i][j + 1]

# print('total', total)
if (total <= number):
    inQueue = number - total
else:
    inQueue = 0


def construct(seatsGrid):
    seats = []
    for i in seatsGrid:
        rows = i[1]
        cols = i[0]
        # mat = [[-1]*cols]*rows
        mat = []
        for i in range(rows):
            mat.append([-1] * cols)
        seats.append(mat)
    return seats

 # Print Seat.
def printSeats(seats):
    blksize = len(str(number))
    rows = [x[1] for x in seatsGrid]
    cols = [x[0] for x in seatsGrid]
    maximum = max(rows)
    top = True
    for i in range(maximum):
        rowlist = []
        rowlistl = []
        for j in range(length):
            row = ' '
            rowl = ' '
            if len(seats[j]) <= i:
                for k in range(cols[j]):
                    row += ' ' * blksize
                    rowl += ' ' * blksize
                    row += ' '
                    rowl += ' '
            else:
                row = '|'
                rowl = '+'
                for k in seats[j][i]:
                    if k == -1:
                        row += ' ' * blksize
                        rowl += '-' * blksize
                        row += '|'
                        rowl += '+'
                    else:
                        row += str(k) + (' ' * (blksize - len(str(k))))
                        rowl += '-' * blksize
                        row += '|'
                        rowl += '+'

            rowlist.append(row)
            rowlistl.append(rowl)
        if top:
            print('    '.join(rowlistl))
            top = False
        print('    '.join(rowlist))
        print('    '.join(rowlistl))

#Aisle Seat

def fill_aisle_seats():
    # filled = 0
    global filled
    row = 0
    tempFilled = -1
    while filled < number and filled != tempFilled:
        tempFilled = filled
        for i in range(length):
            if seatsGrid[i][1] > row:
                if i == 0 and seatsGrid[i][0] > 1:
                    filled += 1
                    aisleCol = seatsGrid[i][0] - 1
                    seats[i][row][aisleCol] = filled
                    if filled >= number:
                        break
                elif i == length - 1 and seatsGrid[i][0] > 1:
                    filled += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = filled
                    if filled >= number:
                        break
                else:
                    filled += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = filled
                    if filled >= number:
                        break
                    if seatsGrid[i][0] > 1:
                        filled += 1
                        aisleCol = seatsGrid[i][0] - 1
                        seats[i][row][aisleCol] = filled
                        if filled >= number:
                            break
        row += 1

# Window Seat
def fill_window_seats():
    row = 0
    global filled
    global number
    tempFilled = 0
    while filled < number and filled != tempFilled:
        tempFilled = filled
        if seatsGrid[0][1] > row:
            filled += 1
            window = 0
            seats[0][row][window] = filled
            if filled >= number:
                break
        if seatsGrid[length - 1][1] > row:
            filled += 1
            window = seatsGrid[length - 1][0] - 1
            seats[length - 1][row][window] = filled
            if filled >= number:
                break
        row += 1

# Middle Seat
def fill_middle_seats():
    row = 0
    tempFilled = 0
    global filled
    while filled < number and filled != tempFilled:
        tempFilled = filled
        for i in range(length):
            if seatsGrid[i][1] > row:
                if seatsGrid[i][0] > 2:
                    for col in range(1, seatsGrid[i][0] - 1):
                        filled += 1
                        seats[i][row][col] = filled
                        if filled >= number:
                            break
        row += 1


seats = construct(seatsGrid)
# print seats
length = len(seatsGrid)

# Aisle
fill_aisle_seats()

# Window

fill_window_seats()

# Center
row = 0
tempFilled = 0
fill_middle_seats()

printSeats(seats)
print("number of passengers in queue", inQueue)