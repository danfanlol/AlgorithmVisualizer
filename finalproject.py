from graphics import *
import random, math
def search(win,source,target,algo):
    visited = []
    for i in range(rows):
        add = []
        for j in range(columns):
            add.append(False)
        visited.append(add)
    si,sj = source[0],source[1]
    ti,tj = target[0],target[1]
    visited[si][sj] = True
    fifo = []
    fifo.append([si,sj,[]])
    while len(fifo) != 0:
        if algo == "bfs":
            node = fifo.pop(0)
        else:
            node = fifo.pop()
        si = node[0]
        sj = node[1]
        if si == ti and sj == tj:
            return path
        path = node[2]
        if si + 1 in range(rows) and not visited[si+1][sj]:
            if si + 1 == ti and sj == tj:
                return path
            fifo.append([si+1,sj,path + [[si+1,sj]]])
            visited[si+1][sj] = True
            grid[si+1][sj].setFill("cyan")
            update(time)
        if si - 1 in range(rows) and not visited[si-1][sj]:
            if si - 1 == ti and sj == tj:
                return path
            fifo.append([si-1,sj,path + [[si-1,sj]]])
            visited[si-1][sj] = True
            grid[si-1][sj].setFill("cyan")
            update(time)
        if sj + 1 in range(columns) and not visited[si][sj+1]:
            if si == ti and sj + 1 == tj:
                return path
            fifo.append([si,sj+1,path + [[si,sj+1]]])
            visited[si][sj+1] = True
            grid[si][sj+1].setFill("cyan")
            update(time)
        if sj - 1 in range(columns) and not visited[si][sj-1]:
            if si == ti and sj - 1 == tj:
                return path
            fifo.append([si,sj-1,path + [[si,sj-1]]])
            visited[si][sj-1] = True
            grid[si][sj-1].setFill("cyan")
            update(time)
    return []
def dijkstra(win,source,target):
    global visited
    paths = []
    for i in range(rows):
        add = []
        for j in range(columns):
            add.append([])
        paths.append(add)
    visited = []
    for i in range(rows):
        add = []
        for j in range(columns):
            add.append(False)
        visited.append(add)
    si,sj = source[0],source[1]
    ti,tj = target[0],target[1]
    dist = []
    for i in range(rows):
        add = []
        for j in range(columns):
            add.append(10000)
        dist.append(add)
    si,sj = source[0],source[1]
    ti,tj = target[0],target[1]
    visited[si][sj] = True
    dist[si][sj] = 0
    mnumi = si
    mnumj = sj
    if si == ti and sj == tj:
        return []
    while True:
        si = mnumi
        sj = mnumj
        if si + 1 in range(rows) and not visited[si+1][sj]:
            if not visited[si+1][sj]:
                if dist[si][sj] + 1 < dist[si+1][sj]:
                    dist[si+1][sj] = dist[si][sj] + 1
                    paths[si+1][sj] = paths[si][sj] + [[si,sj]]
            if si + 1 == ti and sj == tj:
                return paths[si+1][sj]
            grid[si+1][sj].setFill("cyan")
            update(time+7)
        if si - 1 in range(rows) and not visited[si-1][sj]:
            if not visited[si-1][sj]:
                if dist[si][sj] + 1 < dist[si-1][sj]:
                    dist[si-1][sj] = dist[si][sj] + 1
                    paths[si-1][sj] = paths[si][sj] + [[si,sj]]
            if si - 1 == ti and sj == tj:
                return paths[si-1][sj]
            grid[si-1][sj].setFill("cyan")
            update(time+7)
        if sj + 1 in range(columns) and not visited[si][sj+1]:
            if not visited[si][sj+1]:
                if dist[si][sj] + 1 < dist[si][sj+1]:
                    dist[si][sj+1] = dist[si][sj] + 1
                    paths[si][sj+1] = paths[si][sj] + [[si,sj]]
            if si == ti and sj + 1 == tj:
                return paths[si][sj+1]
            grid[si][sj+1].setFill("cyan")
            update(time+7)
        if sj - 1 in range(columns) and not visited[si][sj-1]:
            if not visited[si][sj-1]:
                if dist[si][sj] + 1 < dist[si][sj-1]:
                    dist[si][sj-1] = dist[si][sj] + 1
                    paths[si][sj-1] = paths[si][sj] + [[si,sj]]
            if si == ti and sj - 1 == tj:
                return paths[si][sj-1]
            grid[si][sj-1].setFill("cyan")
            update(time+7)
        visited[si][sj] = True
        if si == ti and sj == tj:
            return path
        min1 = 10000;
        mnumi = 0
        mnumj = 0
        for i in range(len(visited)):
            for j in range(len(visited[0])):
                if not visited[i][j] and dist[i][j] < min1:
                    min1 = min(dist[i][j],min1)
                    mnumi = i
                    mnumj = j 
def setuppathfinding():
    global win, grid
    win = GraphWin("Pathfinding", 1800, 800)
    win.setBackground("white")
def display(win):
    square = Rectangle(Point(900,310),Point(1060,380))
    square.setFill("light blue")
    square.draw(win)
    text = Text(Point(980,345),"GO BACK")
    text.setTextColor("black")
    text.setSize(20)
    text.draw(win)
    square = Rectangle(Point(800,210),Point(1200,260))
    square.setFill("light blue")
    square.draw(win)
    square = Rectangle(Point(830,30),Point(970,100))
    square.setFill("light blue")
    square.draw(win)
    text = Text(Point(900,65),"BFS")
    text.setTextColor("black")
    text.setSize(20)
    text.draw(win)
    square = Rectangle(Point(990,30),Point(1130,100))
    square.setFill("light blue")
    square.draw(win)
    text = Text(Point(1060,65),"DFS")
    text.setTextColor("black")
    text.setSize(20)
    text.draw(win)
    square = Rectangle(Point(900,110),Point(1060,180))
    square.setFill("light blue")
    square.draw(win)
    text = Text(Point(980,145),"DIJKSTRA")
    text.setTextColor("black")
    text.setSize(20)
    text.draw(win)
def initialalgo(mousePoint):
    if mousePoint.getX() in range(100,501) and mousePoint.getY() in range(200,501):
        return "pathfinding"
    if mousePoint.getX() in range(700,1101) and mousePoint.getY() in range(200,501):
        return "binary"
    if mousePoint.getX() in range(1300,1701) and mousePoint.getY() in range(200,501):
        return "sorting"
    if mousePoint.getX() in range(1400,1601) and mousePoint.getY() in range(600,701):
        return "HELP"
    if mousePoint.getX() in range(800,981) and mousePoint.getY() in range(600,701):
        return "EXIT"
    return "0"
        
def initial():
    global initialwindow
    initialwindow = GraphWin("Algorithm", 1800, 800)
    win = initialwindow
    win.setBackground("white")
    text = Text(Point(900,100),"Welcome to the algorithms visualizer. Here, we offer multiple algorithms that, although complex in nature, will be expressed in an appealing way through visual simulation. Please choose your algorithm below.")
    text.setTextColor("black")
    text.setSize(15)
    text.draw(win)
    boxcolor = "light blue"
    square = Rectangle(Point(100,200),Point(500,500))
    square.setFill(boxcolor)
    square.draw(win)
    square = Rectangle(Point(700,200),Point(1100,500))
    square.setFill(boxcolor)
    square.draw(win)
    square = Rectangle(Point(1300,200),Point(1700,500))
    square.setFill(boxcolor)
    square.draw(win)
    square = Rectangle(Point(1400,600),Point(1600,700))
    square.setFill(boxcolor)
    square.draw(win)
    text = Text(Point(295,350),"Pathfinding and graph")
    text.setTextColor("black")
    text.setSize(20)
    text.draw(win)
    text = Text(Point(1500,350),"Sorting")
    text.setTextColor("black")
    text.setSize(20)
    text.draw(win)
    text = Text(Point(1500,650),"HELP")
    text.setTextColor("black")
    text.setSize(20)
    text.draw(win)
    text = Text(Point(890,350),"Binary Searching")
    text.setTextColor("black")
    text.setSize(20)
    text.draw(win)
    square = Rectangle(Point(800,650),Point(980,750))
    square.setFill(boxcolor)
    square.draw(win)
    text = Text(Point(890,700),"EXIT")
    text.setTextColor("black")
    text.setSize(20)
    text.draw(win)
def checkalgo(mousePoint):
    if mousePoint.getX() in range(830,971) and mousePoint.getY() in range(30,101):
        return "bfs"
    if mousePoint.getX() in range(990,1131) and mousePoint.getY() in range(30,101):
        return "dfs"
    if mousePoint.getX()  in range(900,1061) and mousePoint.getY() in range(110,181):
        return "dijkstra"
    if mousePoint.getX() in range(900,1061) and mousePoint.getY() in range(310,381):
        return "terminate"
    if mousePoint.getX() in range(800) and mousePoint.getY() in range(800):
        return None
    return "NOTIN"
def pathfinder():
    global rows,columns,grid, cd, rd, time
    setuppathfinding()
    rows = 9
    columns = 10
    time = 15
    grid = []
    y = 0
    for i in range(rows):
        row = []
        x = 0
        for j in range(columns):
            square = Rectangle(Point(x,y),Point(x+800//columns,y+800//rows))
            square.setFill("white")
            square.draw(win)
            row.append(square)
            x += 800//columns
        grid.append(row)
        y += 800//rows
    cd = 800//columns
    rd = 800//rows
    while True:
        display(win)
        while True:
            wantstoswitch = True
            sx,sy,tx,ty = None,None,None,None
            algo = None
            while True:
                mousePoint = win.getMouse()
                algo = checkalgo(mousePoint)
                if algo != None and algo != "NOTIN":
                    break
            if algo == "terminate":
                win.close()
                return None
            x,y = None,None
            while True:
                if wantstoswitch:
                    square = Rectangle(Point(800,210),Point(1200,260))
                    square.setFill("light blue")
                    square.draw(win)
                    text = Text(Point(980,230),algo.upper() + " SELECTED")
                    text.setTextColor("black")
                    text.setSize(20)
                    text.draw(win)
                if wantstoswitch:
                    while True:
                        mousePoint = win.getMouse()
                        x = mousePoint.getX()
                        y = mousePoint.getY()
                        if x in range(800) and y in range(800):
                            break
                    grid[int(y/rd)][int(x/cd)].setFill("grey")
                wantstoswitch = False
                x2,y2 = None,None
                while True:
                    mousePoint = win.getMouse()
                    x2 = mousePoint.getX()
                    y2 = mousePoint.getY()
                    if x2 in range(800) and y2 in range(800) and (int(y2/rd) != int(y/rd) or int(x2/cd) != int(x/cd)):
                        break
                grid[int(y2/rd)][int(x2/cd)].setFill("grey")
                if int(x/cd) != int(x2/cd) or int(y2/rd) != int(y/rd):
                    sx = int(x/cd)
                    tx = int(x2/cd)
                    sy = int(y/rd)
                    ty = int(y2/rd)
                else:
                    mousePoint = win.getMouse()
                    grid[int(y/rd)][int(x2/cd)].setFill("white") 
                    break
                if algo == "bfs":
                    path = search(win,[sy,sx],[ty,tx],"bfs")
                elif algo == "dfs":
                    path = search(win,[sy,sx],[ty,tx],"dfs")
                elif algo == "dijkstra":
                    path = dijkstra(win,[sy,sx],[ty,tx])
                    path.pop(0)
                for coord in path:
                    x = coord[0]
                    y = coord[1]
                    grid[x][y].setFill("yellow")
                    update(time)
                mousePoint = win.getMouse()
                for i in range(rows):
                    for j in range(columns):
                        grid[i][j].setFill("white")
                while True:
                    mousePoint = win.getMouse()
                    pos = checkalgo(mousePoint)
                    if pos == "terminate":
                        win.close()
                        return None
                    if pos == "NOTIN":
                        continue
                    if pos != None:
                        algo = pos
                        wantstoswitch = True
                    else:
                        grid[int(mousePoint.getY()/rd)][int(mousePoint.getX()/cd)].setFill("grey")
                        x = mousePoint.getX()
                        y = mousePoint.getY()
                    break

def bogosort(numbers):
    while True:
        random.shuffle(numbers) 
        undraw()
        draw(numbers)
        issorted = False
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                allsorted = True
                break
        if issorted:
            break
#bogo sort first shuffles the numbers randomly, undraws the current set of numbers, draws the new set of numbers, then checks if the shuffled list is sorted.
def bubblesort(numbers):
    while True:
        allsorted = True
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                allsorted = False
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
                undraw()
                draw(numbers)
        if allsorted: 
            return numbers
#goes through the list and sorts every consecutive pair of numbers going up. As it repeats, the largest numbers will go to the end while the smaller ones go to the beginning. Finally, it checks if it is sorted.
def undraw():
    for rectangle in rectangles:
        rectangle.undraw()
#undraws the current set of rectangles which represent the numbers
def selectionsort(numbers):
    curi = 0
    for i in range(curi,len(numbers)):
        minidx = i
        minnum = numbers[minidx]
        for j in range(curi,len(numbers)):
            if numbers[j] < minnum:
                minnum = numbers[j]
                minidx = j
        numbers[i],numbers[minidx] = numbers[minidx],numbers[i]
        undraw()
        draw(numbers)
        curi += 1
    return numbers
#loops through the list going through each index. At every index, from that index to the end of the list the program will return the smallest value. That value will then go to that index. The end result is a sorted list 
def insertionsort(numbers):
    i = 1
    while i < len(numbers):
        j = i
        while numbers[i] < numbers[j-1] and j > 0:
            j -= 1
        element = numbers[i]
        del numbers[i]
        numbers.insert(j,element)
        undraw()
        draw(numbers)
        i += 1
    return numbers 
def quickSort(arr,low,high):
    if high > low:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
def partition(arr, low, high):
    i = low-1
    pivot = arr[high]     
    for j in range(low, high):
        if arr[j] <= pivot:
            i+= 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    undraw()
    draw(arr)
    return i+1

#helper function to quicksort. Assists with determining where to split the list 
def setupsorting():
    global win, grid
    win = GraphWin("Sorting", 1800, 1000,autoflush=False)
    win.setBackground("white")
    rectangle = Rectangle(Point(0,0),Point(1200,800))
    rectangle.setFill("white")
    rectangle.draw(win)
#sets the window up and turns autoflush off (very important)
def draw(numbers):
    global rectangles
    rectangles = []
    global width,factor
    factor = 800/max(numbers)
    curx = 0
    width = int(1200/len(numbers))
    for num in numbers:
        rectangle = Rectangle(Point(curx,800-factor*num),Point(curx+width,800))
        rectangle.setFill("light blue")
        rectangle.draw(win)
        rectangles.append(rectangle)
        curx += width
    update(5)
    sortings = ["selection ","insertion","bubble","quick","bogo"]
    cur = 30
    for i in range(5):
        rectangle = Rectangle(Point(cur,850),Point(cur+180,950))
        rectangle.setFill("light blue")
        rectangle.draw(win)
        text = Text(Point(cur+90,900),sortings[i] + " sort")
        text.setTextColor("black")
        text.setSize(20)
        text.draw(win)
        cur += 240
    rectangle = Rectangle(Point(cur,850),Point(cur+180,950))
    rectangle.setFill("light blue")
    rectangle.draw(win)
    text = Text(Point(cur+90,900),"GO BACK")
    text.setTextColor("black")
    text.setSize(20)
    text.draw(win)
    cur += 240
def check(mousePoint):
    cur = 30
    sortings = ["selection","insertion","bubble","quick","bogo","GO BACK"] #all possible sorting algorithms to choose
    for i in range(6):
        if mousePoint.getX() in range(cur,cur+180) and mousePoint.getY() in range(850,950): #coordinates for sorting boxes
            return sortings[i]
        cur += 240
    return "NONE"
def sorting():
    setupsorting()
    while True:
        numbers =  [] 
        rectangle = Rectangle(Point(1200,0),Point(1800,800))
        rectangle.setFill("white")
        for i in range(15):
            numbers.append(random.randint(0,9)) #adds 15 random numbers to the list 
        draw(numbers) #draws the numbers
        mousePoint = win.getMouse() #waits for user to click 
        algo = check(mousePoint) #which algorithm the person clicked on. If they chose none, returns NONE
        if algo == "NONE": # if they didn't choose an algo, repeat the process until they choose one
            print("NONE")
            while algo == "NONE":
                mousePoint = win.getMouse()
                algo = check(mousePoint)
        if algo == "bubble": #chose bubble sort
            text = Text(Point(1500,100),"Another poor sorting algorithm that is used primarily for \n educational purposes, bubble sort iterates through the list sorting \n every pair of consecutive integers \n until the list is sorted")
            text.setTextColor("black")
            text.setSize(15)
            text.draw(win)
            bubblesort(numbers) #simulate bubble sort
        elif algo == "selection": #chose selection sort 
            text = Text(Point(1500,100),"Starting from the front to the end, it takes the smallest element at \n every index and adds it to its current position. \n It has O(N^2) time complexity on average.")
            text.setTextColor("black")
            text.setSize(15)
            text.draw(win)
            selectionsort(numbers) #simulates selection sort
        elif algo == "insertion": #chose insertion sort
            text = Text(Point(1500,100),"This algorithm sorts the list as if it were a deck of cards. \n It has O(N^2) time complexity on average and takes each element \n and finds where it belongs in the list.")
            text.setTextColor("black")
            text.setSize(15)
            text.draw(win)
            insertionsort(numbers) #simulates insertion sort
        elif algo == "bogo": #chose bogo sort
            text = Text(Point(1500,100),"Created as a joke by computer science researchers, \n Bogosort was developed to be the slowest sorting algorithm in \n the world. If bogosort began at the beginning of Earth's formation \n sorting a list of 1000 numbers, it still wouldn't be finished now.")
            text.setTextColor("black")
            text.setSize(15)
            text.draw(win)
            text = Text(Point(1500,500),"It works by taking a random shuffle of the list it is sorting \n and checking if the shuffle is sorted. \n Other names for it are stupid sort and monkey sort")
            text.setTextColor("black")
            text.setSize(15)
            text.draw(win)
            bogosort(numbers) #simulates bogo sort
        elif algo == "GO BACK":
            win.close()
            return None
        else: #chose quick sort 
            text = Text(Point(1500,100),"One of the fastest sorting algorithms, \n it operates through divide and conquer. By using a pivot, \n it can be implemented to be \n faster than both merge sort and heap sort. ")
            text.setTextColor("black")
            text.setSize(15)
            text.draw(win) #simulates quick sort 
            quickSort(numbers,0,len(numbers)-1)
        mousePoint = win.getMouse() #waits for user to click 
        rectangle.draw(win) #resets the screen 
        undraw() #undraws the numbers
def simulatebs(number, numbers, rectangles):
    low = 0
    high = len(numbers)-1
    while low <= high:
        mid = (low + high) // 2
        print(mid)
        prevs = [low,high]
        rectangles[low].setFill("light blue")
        rectangles[high].setFill("light blue")
        update(2)
        if numbers[mid] == number:
            break
        if numbers[mid] > number:
            high = mid - 1
        else:
            low = mid + 1
        rectangles[prevs[0]].setFill("light yellow")
        rectangles[prevs[1]].setFill("light yellow")
    mp = win.getMouse()
    for i in range(len(rectangles)):
        rectangles[i].setFill("light yellow")
    
def binarysearching():
    global win 
    win = GraphWin("binarysearching", 1800, 1000,autoflush=False)
    win.setBackground("white")
    text = Text(Point(900,200),"Binary searching is one of the most powerful and fastest algorithms in the world. It's O(Log N) runtime allows for many problems to be solved efficiently and correctly.")
    text.setTextColor("black")
    text.setSize(15)
    text.draw(win) 
    numbers = []
    for i in range(18):
        numbers.append(i+1)
    x = 0
    rectangles = []
    for i in range(len(numbers)):
        rectangle = Rectangle(Point(x,600),Point(x+100,700))
        rectangle.setFill("light yellow")
        rectangle.draw(win)
        rectangles.append(rectangle)
        x += 100
        text = Text(Point(x-50,650),str(numbers[i]))
        text.setTextColor("black")
        text.setSize(15)
        text.draw(win) 
    rectangle = Rectangle(Point(800,800),Point(1000,850))
    rectangle.setFill("white")
    rectangle.draw(win)
    text = Text(Point(900,825),"EXIT")
    text.setTextColor("black")
    text.setSize(15)
    text.draw(win)
    while True:
        mousepoint = win.getMouse()
        if mousepoint.getY() in range(600,701):
            simulatebs(math.floor(mousepoint.getX()/100)+1,numbers,rectangles)
        elif mousepoint.getY() in range(800,851) and mousepoint.getX() in range(800,1001):
            win.close()
            return None
def displayhelp():
    win = GraphWin("Help Window", 1800, 1000,autoflush=False)
    win.setBackground("white")
    hashmap = {0:"Upon opening the program, you will prompted to the main menu where you will be given three options in the red boxes.",1:"Two of them are for algorithm visualization while the other is the exit button.",
               2: "If you pick the option for graphs, a new window will open where four additional buttons in red show up.",
               3: "The top three are all algorithms that you can visualize while the bottom one exits the window and returns to the main menu.",
               4: "Upon picking an algorithm, select two different spots in the blue grid. The first will be where the selected algorithm starts while the last one will be where it ends.",
               5:"Immediately after picking the last spot, the algorithm will start searching from the first node until it reaches the target node (your last spot).",
               6: "After the searching is over, you will be shown the final result (including a path being drawn from the first node to the final node) until you click.",
               7: "Afterwards, you can either reselect two different nodes which will result in the process above, choose another algorithm to visualize, or exit the window.",
               8: "If you pick the option for sorting, another window will also show up where you will be given options for different sorting algorithms in green along with an exit button.",
               9: "Picking any of the sorting buttons will simulate the desired algorithm in front of you. The finished result will be shown as long as you want before you click.",
               10: "After clicking, a new random list will be generated and shown and you are free to pick any new algorithm or exit to the main menu."}
    pos = 200
    for i in range(11):
        text = Text(Point(900,pos),hashmap[i])
        text.setTextColor("black")
        text.setSize(15)
        text.draw(win)
        pos += 50
    rectangle = Rectangle(Point(800,800),Point(1000,850))
    rectangle.setFill("white")
    rectangle.draw(win)
    text = Text(Point(900,825),"EXIT")
    text.setTextColor("black")
    text.setSize(15)
    text.draw(win)
    while True:
        mousepoint = win.getMouse()
        if mousepoint.getY() in range(800,851) and mousepoint.getX() in range(800,1001):
            win.close()
            return None
def main():
    initial()
    win = initialwindow
    while True:
        mousePoint = win.getMouse()
        if initialalgo(mousePoint) == "pathfinding":
            pathfinder()
        elif initialalgo(mousePoint) == "sorting":
            sorting()
        elif initialalgo(mousePoint) == "binary":
            binarysearching()
        elif initialalgo(mousePoint) == "HELP":
            displayhelp()
        elif initialalgo(mousePoint) == "EXIT":
            win.close()
            break
main()
