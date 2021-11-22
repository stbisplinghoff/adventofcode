# Solution to Advent of Code 2020 day 24

# Read data
with open("input.txt") as inFile:
    tiles = inFile.read().split("\n")

# Hexagonal coordinate system
# e: 2,0   se: 1,1    sw: -1,1     w: -2,0      nw: -1,-1   ne: 1,-1
moveMap = [(2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1), (1, -1)]
# Set up dictionary with identified tiles, coordinate as key, True=Black, False=White
identifiedTiles = {}
for tile in tiles:
    # Recode directions as ordered above to get single character instructions
    recodedTilePath = tile \
        .replace("se", "1").replace("sw", "2").replace("nw", "4") \
        .replace("ne", "5").replace("e", "0").replace("w", "3")
    currentLocation = (0, 0)
    # Travel the path by adjusting coordinates with every step
    for move in [int(strMove) for strMove in list(recodedTilePath)]:
        currentLocation = currentLocation[0] + moveMap[move][0], currentLocation[1] + moveMap[move][1]
    # Not yet recorded tiles are white, set them initially to black
    if currentLocation not in identifiedTiles:
        identifiedTiles[currentLocation] = True
    # Flip known tiles
    else:
        identifiedTiles[currentLocation] = not identifiedTiles[currentLocation]
# Sum up all known tiles that are actually black (=True)
print("Black tiles: ", sum(identifiedTiles.values()))

for days in range(100):
    newValues = {}
    whiteCheckCandidates = []
    for coordinate, blackColor in identifiedTiles.items():
        adjacentCoordinates = [(coordinate[0] + x, coordinate[1] + y) for x, y in moveMap]
        if blackColor:
            # Rule 1: Check black tiles for neighbouring (0 or >2) black tiles
            adjacentBlackColors = [identifiedTiles[testCoordinate]
                                   for testCoordinate in adjacentCoordinates if testCoordinate in identifiedTiles]
            if sum(adjacentBlackColors) == 0 or sum(adjacentBlackColors) > 2:
                newValues[coordinate] = False
            # Rule 2: Find white tiles that are adjacent to black tile to reduce search area
            for currentCoordinate in adjacentCoordinates:
                if currentCoordinate not in identifiedTiles or identifiedTiles[currentCoordinate] == False:
                    whiteCheckCandidates += (currentCoordinate,)
    # Rule 2 continued: Check every candidate for adjacent black tiles (similar to rule 1, different count condition)
    for coordinate in whiteCheckCandidates:
        adjacentCoordinates = [(coordinate[0] + x, coordinate[1] + y) for x, y in moveMap]
        adjacentBlackColors = [identifiedTiles[testCoordinate]
                               for testCoordinate in adjacentCoordinates if testCoordinate in identifiedTiles]
        # Flip this tile to white if it has exactly 2 adjacent black tiles
        if sum(adjacentBlackColors) == 2:
            newValues[coordinate] = True
    # Apply new values
    for coordinate, newColor in newValues.items():
        identifiedTiles[coordinate] = newColor
# Count black tiles
print("Black tiles: ", sum(identifiedTiles.values()))
