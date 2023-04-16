# /*
# The Unibaker.
#
#   The newest fad for party cakes is the cupcake-cake, where many
#      cupcakes are placed side-by-side to make a single cake.
#   The celebrated Unibaker has developed his own version.
#   All of his cupcakes are either White or Chocolate cake.
#   ... and they are square,
#   ... and they are placed together to create a larger square cake,
#   ... with specific requirements.
#     - The White and Chocolate cupcakes each form a shape called a Nurikabe, which means:
#         - No 2x2 set of cupcakes can all be the same type
#         - All cupcakes of the same type must be connected
#              by neighboring full sides.
#              This creates 2 connected regions: one White, one Chocolate
#         - At least one of each cupcake is on the border of the full cake
#              (So you can always grab either a White or Chocolate cupcake
#              from the edge, until they're gone.
#         Side note: 
#         The number of White and Chocolate cupcakes doesn't have to be equal.
#
#   The first line of input is a single integer N (max of 11), the size of the square cake.
#   The next N lines contain N characters, each reprenting:
#     - '.' White cupcakes
#     - '#' Chocolate cupcakes
#     - '?' Unknown cupcakes
# 
#   You must determine all the cupcakes and print the diagram for the full cake.
#   There is only one solution.
# */

debugPrint = False
debugPrint2x2 = False
debugPrintBorder = False
mainGrid = [[(0) for x in range(11)] for x in range(11)] # 11x11 array of cupcakes (max is 11)
guessGrid = [[(0) for x in range(11)] for x in range(11)] # empty grid
exitGrid = [[(0) for x in range(11)] for x in range(11)] # empty grid
gridSize = 11

#-------
# Solving-time variables
newSquareAdded=False
errorFound=False

# Multi-Exit search.  Best spot for guess
me_filled = False
me_r = 0
me_c = 0
me_v = 0 # Value to put into a guess for a multi-exit region
me_count = 50

import sys

#-----------------------------------
# Print the mainGrid
def printGrid():
    for i in range(gridSize):
        for j in range(gridSize):
            val = mainGrid[i][j]
            if val == 11: # White (.)
                char = '.'
            elif val == 12: # Chocolate (#)
                char = '#'
            else:
                char = '?'
            print(char, sep='', end='')
        print ('')

#-----------------------------------
# gridFull will return True if there are no empty squares
def gridFull():
    for i in range(gridSize):
        for j in range(gridSize):
            if mainGrid[i][j] == 0:
                return False
    return True

#-----------------------------------
# emptyThisGrid will fill the grid with 0
def emptyThisGrid(grid):
    for i in range(gridSize):
        for j in range(gridSize):
            grid[i][j] = 0
    return

#-----------------------------------
# emptyThisGridLabel will change matching labels to 0
def emptyThisGridLabel(grid, label):
    for i in range(gridSize):
        for j in range(gridSize):
            if grid[i][j] == label:
                grid[i][j] = 0
    return

#-----------------------------------
# emptyGuesses will change matching guesses to 0
#    and their values to 0
def emptyGuesses(g):
    if debugPrint:
        print("Emptying all guessLevel",g)
        print("Starting Grid:")
        printGrid()
    for i in range(gridSize):
        for j in range(gridSize):
            if guessGrid[i][j] == g:
                guessGrid[i][j] = 0
                mainGrid[i][j] = 0
    if debugPrint:
        print("Resulting Grid:")
        printGrid()
    return

#-----------------------------------------------------------------------------
# 2x2 ANALYSIS FUNCTIONS
#-----------------------------------------------------------------------------
#--------------------
# sum2x2 finds the sum of the 2x2 square with top left at (r,c)
def sum2x2(r,c):
    return mainGrid[r][c] + mainGrid[r][c+1] + mainGrid[r+1][c] + mainGrid[r+1][c+1]

#--------------------
# fillSquare assigns the value to the main grid and the guess grid
def fillSquare(r,c,val,guessLevel):
    global newSquareAdded
    if debugPrint2x2:
        print("2x2 Filling",r,c,"with",val,guessLevel)
    mainGrid[r][c]=val
    guessGrid[r][c]=guessLevel
    newSquareAdded=True       # Flag to tell main loop the grid has changed
    return

#--------------------
# findEmpty2x2 finds the one empty coordinate of the 2x2 square with top left at (r,c)
def findEmpty2x2(r,c):
    for i in range(2):
        for j in range(2):
            if mainGrid[r+i][c+j]==0:
                return r+i,c+j

#--------------------
# fillEmpty2x2 fills the one empty coord of the 2x2 square with top left at (r,c)
def fillEmpty2x2(r,c,val,guessLevel):
    re,ce = findEmpty2x2(r,c)
    fillSquare(re,ce,val,guessLevel)
    return

#--------------------
# checkAll2x2
#    Returns error if a 2x2 is 
#      - all the same color (not allowed), or 
#      - Checkerboard, since it would lead to two disconnected regions of the same color.
#    If 3 are filled, it tries to fill 4th
def checkAll2x2(guessLevel):
    global errorFound
    if debugPrint2x2:
        print("Starting checkAll2x2")
    for i in range(gridSize-1):
        for j in range(gridSize-1):
            sumSq = sum2x2(i,j)
            if ((sumSq==44) or (sumSq==48)):  # All 4 squares are the same.  Return error
                if debugPrint2x2:
                    print("2x2 All 4 Error Found at",i,j,guessLevel)
                errorFound=True
                return
            elif ((sumSq==46) and (mainGrid[i][j] == mainGrid[i+1][j+1])):
                if debugPrint2x2:
                    print("2x2 checkerboard Error Found at",i,j,guessLevel)
                errorFound=True # 2 White, 2 Choc, Opposite corners the same. Loop Exists
                return
            elif (sumSq > 30 and sumSq <40):  # Three squares filled. See if we can fill the 4th
                if sumSq==33:    # Three white. 4th must be choc
                    fillEmpty2x2(i,j,12,guessLevel)
                elif sumSq==36:  # Three choc, 4th must be white
                    fillEmpty2x2(i,j,11,guessLevel)
                elif sumSq==34:  # 2 white, one choc.  Add white only to avoid checkerboard
                    if (mainGrid[i][j]==11 and mainGrid[i+1][j+1]==11) or (mainGrid[i+1][j]==11 and mainGrid[i][j+1]==11):
                        fillEmpty2x2(i,j,11,guessLevel)
                elif sumSq==35:  # 2 choc, one white.  Add choc only to avoid checkerboard
                    if (mainGrid[i][j]==12 and mainGrid[i+1][j+1]==12) or (mainGrid[i+1][j]==12 and mainGrid[i][j+1]==12):
                        fillEmpty2x2(i,j,12,guessLevel)
    return

#-----------------------------------------------------------------------------
# BORDER ANALYSIS FUNCTIONS
#-----------------------------------------------------------------------------
#--------------
# whiteChocCount
#   Update the white or choc count based on the value
def whiteChocCount(w, c, v):
    if v > 0:
        if v == 11:
            w = w + 1
        else:
            c = c + 1
    return w,c

#--------------
# nextBorderSquare
#   Return the r,c for the next border square clockwise
def nextBorderSquare(r,c):
    if r==0:              # Top Row
        if c==gridSize-1: # Top-Right Corner
            return r+1,c  # Start down the right column
        return r, c+1     #   else keep moving right across the top
    if c==gridSize-1:     # Right Column
        if r==gridSize-1: # Bottom-Right Corner
            return r,c-1  # Start left across the bottom
        return r+1,c      #   else keep moving Down the right column
    if r==gridSize-1:     # Bottom Row
        if c==0:          # Bottom-Left Corner
            return r-1,c  # Start up the left column
        return r, c-1     #   else keep moving left across the bottom
    if c==0:              # Left Column
        if r==0:          # Top-Left Corner
            return r,c+1  # Start right across the top
        return r-1, c     #   else keep moving up the left column

#----------------------------
# borderIsFull()
#   False if there are any empty squares, True if full
#   Also returns the count of white/choc squares
def borderIsFull():
    wc,cc = whiteChocCount(0,0, mainGrid[0][0])

    r,c = nextBorderSquare(0,0)
    if debugPrintBorder:
        print("borderIsFull: Starting at",r,c)
    while (r!=0) or (c!=0):
        if debugPrintBorder:
            print("Full check:",r,c,":",mainGrid[r][c])
        wc,cc = whiteChocCount(wc,cc, mainGrid[r][c])
        r,c = nextBorderSquare(r,c)
    if (wc+cc)<(4*(gridSize-1)): # A full grid will have 4*(gridSize-1) filled
        return wc,cc,False
    return wc,cc,True

#----------------------------
# findLastFilled()
#   Starting from r,c, scan to the first filled border square where the next is empty (could be r,c)
def findLastFilled(r,c):
    rnext,cnext = nextBorderSquare(r,c)
    while (mainGrid[r][c]==0 or mainGrid[rnext][cnext]>0):
        r,c = rnext,cnext
        rnext,cnext = nextBorderSquare(r,c)
    return r,c

#----------------------------
# findNextFilled()
#   Starting from r,c, scan to the first filled border  (could be r,c)
def findNextFilled(r,c):
    while mainGrid[r][c]==0:
        r,c = nextBorderSquare(r,c)
    return r,c

#-----------------------------
# checkBorder()
#   When done, there are 2 regions along the border: one white, one choc
#      This has to be true, otherwise there would be one 
#          color separated from its common colors.
#   Scan the border.  As long as at least 1 of each color exists,
#      fill in any empties between matching colors.
def checkBorder(guessLevel):
    if debugPrintBorder:
        print("Starting checkBorder")
    whiteCount, chocCount, full = borderIsFull()
    if full:
        if debugPrintBorder:
            print("Border Is Full")
            printGrid()
        return  # No need to analyze if the border is already full.

    # ---- Make sure there is at least 1 of each color on the border
    if whiteCount==0 or chocCount==0:  # Border filling logic only works if both colors exist
        return

    #----- Find each gap and determine if can be filled (both ends the same color)
    r,c = findLastFilled(0,0)   # Scan to the first filled-followed-by-empty border
    gapsNotFilled=0
    while gapsNotFilled<3:  # Scanning around for 3 gaps will always find any to fill.
        v = mainGrid[r][c]
        re,ce = nextBorderSquare(r,c) # Location of the neighboring empty square
        rn,cn = findNextFilled(re,ce)
        vn = mainGrid[rn][cn]
        if debugPrintBorder:
            print("Border: At",r,c,":",v,".  At",re,ce,":",mainGrid[re][ce],".  At",rn,cn,":",vn,".")

        if v==vn:  # Match, so we can fill in the gap.
            if debugPrintBorder:
                print("Border: Filling from",r,c,"to",rn,cn,"with",v)
            r,c = re,ce
            while (r!=rn) or (c!=cn):
                fillSquare(r,c,v,guessLevel)
                r,c = nextBorderSquare(r,c)
            return checkBorder(guessLevel)    # Recursively fill in the border
        # Colors at each end of gap don't match.  This can happen at most twice.
        gapsNotFilled = gapsNotFilled+1
        r1,c1 = findLastFilled(rn,cn)
        if r==r1 and c==c1:                   # We'd be scanning the same gap we just finished
            return
        r=r1
        c=c1
    return


#-----------------------------------------------------------------------------
# SINGLE EXIT ANALYSIS FUNCTIONS
#-----------------------------------------------------------------------------
#  First scan all border regions, marking them as border.
#  Then scan the inner squares.
#    If we scan a piece with zero exits, and it's not the border,
#           we will mark errorFound
#  While scanning, record the number of exits.  
#     If there is a single exit, fill it.
#  Update the "best guess" location with the smallest number of exits.

#---------------------------------
# countLabelFill()
#   A recursive function that counts empty squares next to a contiguous region.
#   Any like-color squares will be labelled similarly
#     so following searches don't use them.
#   If fill==True, it will fill the first it finds with fill_val and exit.
#   If fill==False, it will not fill empties.
def countLabelFill(r,c,v,label,fill,fill_val,guessLevel):
    global me_filled
    if r<0 or c<0 or r>=gridSize or c >=gridSize:  # Out of the grid
        return 0
    val = mainGrid[r][c]
    if (val==0):                    # empty square
        if fill and not me_filled:  # Fill as long multi-exit-filled flag not set yet
            if debugPrint:
                print("countLabelFill: Filling",r,c,"with",fill_val)
            fillSquare(r,c,fill_val,guessLevel)
            me_filled = True        # Only fill one square on each search
            exitGrid[r][c] = label  # Label the new square
            fill = False            # don't fill any more, but continue the count.
            return countNeighborSquares(r,c,v,label,fill,fill_val,guessLevel)
        else:
            return 1                # Found an empty square (and didn't fill it)
    elif (val != v):                # Non matching color
        return 0
    
    # Color matches, we must still be moving through our region
    if exitGrid[r][c] > 0:   # Square already visited, skip
        return 0

    # Recursively search through all connected squares
    exitGrid[r][c] = label
    return countNeighborSquares(r,c,v,label,fill,fill_val,guessLevel)

#--------------------------------
#  countNeighborSquares()
#  Recursively count all neighboring exit (empty) squares
def countNeighborSquares(r,c,v,label,fill,fill_val,guessLevel):
    count = 0
    count = count + countLabelFill(r-1,c,v,label,fill,fill_val,guessLevel)   # Up
    count = count + countLabelFill(r,c+1,v,label,fill,fill_val,guessLevel)   # Right
    count = count + countLabelFill(r+1,c,v,label,fill,fill_val,guessLevel)   # Down
    count = count + countLabelFill(r,c-1,v,label,fill,fill_val,guessLevel)   # Left
    return count

#---------------------------------
# checkAndUpdateMultiExitGlobals()
#   With fewer possible exits from a region, there are less
#     options for guesses, so hopefully a quicker recursive search.
#   This routine records the smallest exit count for a region so far,
#     and one of its exit points to use for a guess.
def checkAndUpdateMultiExitGlobals(r,c,v,count):
    global me_r
    global me_c
    global me_count
    global me_v                                 
    if count>1 and count < me_count:     # Store the best place for a guess (less exit options)
        me_r = r
        me_c = c
        me_count = count
        me_v = v
        if debugPrint:
            print("Best Guess at",me_r,me_c,me_v,". Count:",me_count)

#---------------------------------
# If a region has a single empty neighbor, then the empty must extend that region.
# If an non-border region has no exits, it's isolated so a prior guess is wrong.
# If all regions have more than 1 empty neighbor, record the smallest exit-count
#   for a guess later.
def checkSingleExit(guessLevel):
    global me_filled
    global me_r
    global me_c
    global me_count
    global me_v
    global newSquareAdded
    global errorFound
    emptyThisGrid(exitGrid)
    label = 51             # Just something high, not used yet.
    me_count = 51          # Just a large number, to compare count of multi-exit options

    # First scan the border.  Eventually, there will only be 2 regions.
    r=0
    c=0
    v = mainGrid[r][c]
    if v>0:
        count = countLabelFill(r,c,v,label,False,v,guessLevel)
        checkAndUpdateMultiExitGlobals(r,c,v,count)
    r,c = nextBorderSquare(r,c)
    while r!=0 or c!=0:
        ## Run around the border.  Duplicated code for border and inner analysis.
        if exitGrid[r][c]>0:     # Already visited.  Move to next
            r,c = nextBorderSquare(r,c)
            continue
        v = mainGrid[r][c]
        if v==0:
            r,c = nextBorderSquare(r,c)
            continue             # Only analyze filled squares
        count = countLabelFill(r,c,v,label,False,v,guessLevel)
        if (count == 1):      # Single exit.  Assign the empty and return to restart analysis
            if debugPrint:
                print("Found a single exit connected to",r,c,".  Going to fill it.")
            me_filled = False
            emptyThisGridLabel(exitGrid,label)
            count = countLabelFill(r,c,v,label,True,v,guessLevel)
            return # Rather than try to re-run Single-Exit analysis, start full analysis again.
        label = label+1          # Prep to label the next region
        checkAndUpdateMultiExitGlobals(r,c,v,count)
        r,c = nextBorderSquare(r,c)

    # Then scan inside the border.  Now, any zero-counts are errors.
    for r in range(1,gridSize-1):
        for c in range(1,gridSize-1):
            if exitGrid[r][c]>0:     # Already visited.  Skip
                continue
            v = mainGrid[r][c]
            if v==0:
                continue             # Only analyze filled squares
            count = countLabelFill(r,c,v,label,False,v,guessLevel)
            if (count == 1):      # Single exit.  Assign the empty  and return to restart analysis
                if debugPrint:
                    print("Found a single exit connected to",r,c,".  Going to fill it.")
                me_filled = False
                emptyThisGridLabel(exitGrid,label)
                count = countLabelFill(r,c,v,label,True,v,guessLevel)
                return # Rather than try to re-run Single-Exit analysis, start full analysis again.
            if count == 0:           # If any non-border regions have count=0, they're isolated. Mark error
                if debugPrint:
                    print("SingleExit Error Found at",r,c,v,guessLevel)
                errorFound = True
                return
            checkAndUpdateMultiExitGlobals(r,c,v,count)
            label = label+1          # Prep to label the next region

#---------------------------------------------------------------------------
# makeAGuess
#   Using the last discovered Best Guess, assign one value.
#      Then recursively restart analyzeAllAdditions
#      Upon error, assign the opposite value and continue
#        the current loop.
def makeAGuess(guessLevel):
    global me_r
    global me_c
    global me_v
    global me_filled
    global errorFound
    global exitGrid

    guessLevel = guessLevel+1   # Increase the guess level
    emptyThisGrid(exitGrid)
    r = me_r                    # Use previously found "best guess" region
    c = me_c                    # Need to copy locally to preserve during recursion
    v = me_v
    # Use opposite color of current region first.  Might force a quick single-Exit assignment
    new_val = 23-v              # 23-v changes white to choc, and vice-versa
    if debugPrint:
        print("GUESSING")
        printGrid()
        print("Making guess. Filling",r,c,new_val,guessLevel)
    me_filled = False           # Clear the Multi-Exit-Filled flag
    count = countLabelFill(r,c,v,50,True,new_val,guessLevel)
    analyzeAllAdditions(guessLevel)    # Restart analysis to test the guess
                                         # If it's right, we'll exit
                                         # if it's wrong, we'll return here
    if debugPrint:
        print("OOPS.")
        printGrid()
    emptyGuesses(guessLevel)     # Clear out all guesses
    errorFound = False           # Clear out error
    guessLevel = guessLevel-1    # Back to original guess level.
    emptyThisGrid(exitGrid)
    if debugPrint:
        print("Guessed Wrong. Assigning",r,c,v,guessLevel)
    me_filled = False
    count = countLabelFill(r,c,v,50,True,v,guessLevel)
    # Function now returns after setting the right color for this guessLevel

#---------------------------------------------------------------------------
# Do Analysis until no new squares can be placed. 
#   Exit with error if any errors found, to allow prior guess to be removed
def analyzeAllAdditions(guessLevel):
    if debugPrint:
        print("Starting All Loop")
    global newSquareAdded
    newSquareAdded = True  # Get the while loops started
    while True: # Run forever, until grid is full or error is found
        while(newSquareAdded):      # Loop for all checks
            while(newSquareAdded):  # Loop for Border and 2x2 checks
                newSquareAdded = False  # Will be set back to True in fillSquare()
                checkBorder(guessLevel)
                checkAll2x2(guessLevel)
                if errorFound:
                    return   # Simply by returning, a prior guess will be removed and replaced
            checkSingleExit(guessLevel)
            if errorFound: # A zero-exit (surrounded) region exists, not on the border
                return
    
        if gridFull(): # We reached the end!
            print("")
            printGrid()
            exit()     # Exit the program, since there's only one solution.
    
        # The grid isn't full, so we need to make a guess
		# If the guess is wrong, the last step of makeAGuess() is to
		#    fill the opposite color (which sets newSquareAdded to True)
        makeAGuess(guessLevel)

#------------------------------------------------------------------------
# Main program starts here.

textSize = sys.stdin.readline().rstrip('\n').rstrip(' ');
gridSize = int(textSize)

# Read in the maze
for i in range(gridSize):
    line = sys.stdin.readline()  # "." = white.  "#" = chocolate.  "?" = unknown
    for j in range(gridSize):
        square = line[j]
        if square == '.':    # white = 11
            mainGrid[i][j] = 11
        elif square == '#':  # chocolate = 12
            mainGrid[i][j] = 12
        else:
            mainGrid[i][j] = 0
# Debug Print the starting values
if debugPrint:
    print('')
    print ('Initial Grid:')
    printGrid()

# This call will analyze all options, then print the solution and exit.
analyzeAllAdditions(1)
