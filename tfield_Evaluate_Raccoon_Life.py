#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:06:05 2020

@author: tfield
"""

import os
import math

# Open the file, read in the data, line by line, removing newline characters
fin = open("2008Male00006.txt", "r")
currentLine = fin.readline()
currentLine = currentLine.rstrip()
lines = [currentLine]
while len(currentLine) > 0:
    currentLine = fin.readline()
    currentLine = currentLine.rstrip()
    if len(currentLine) > 0:
        lines.append(currentLine)
        
# Close file once everything is read in
fin.close()

# Number of lines in the file, know the first line is header, last is result
numLines = len(lines)

# Split sections of files
header = lines[0]
data = lines[1:(numLines-2)]
footer = lines[numLines-1]

# Get name from first part of footer
name = footer.split(' ')
name = name[0]

# Separate using comma as delimiter
header = header.split(",")
splitData = []
for i in range(0,len(data)):
    splitLine = data[i].split(",")
    splitData.append(splitLine)

# Each list in the sortedData list is a single type of data. i.e. time
sortedData = []
for i in range(0,len(header)):
    currentData = []
    for j in range(0,len(splitData)):
        currentData.append(splitData[j][i])
    sortedData.append(currentData)

# Data type for each term in the header. 0 for string, 1 for int, 2 for float
dataTypes = [0,0,0,1,2,2,0,0,2,2,2,2,2,2,2]

# Change inputed data to correct datatype and return
def fixDataType(wrongDataType, newTypeFlag):
    rightDataType = []
    for i in range(0,len(wrongDataType)):
        if newTypeFlag == 1:
            rightDataType.append(int(wrongDataType[i]))
        elif newTypeFlag == 2:
            rightDataType.append(float(wrongDataType[i]))
        else:
            rightDataType.append(wrongDataType[i])
    return rightDataType

# Create a dictionary based on the information in the header
# use the lists in sortedData to fill the dictionary.
# Fix the data type of lists that should be int or float instead of string
raccoon = dict()
for i in range(0,len(header)):
    currentColumn = fixDataType(sortedData[i], dataTypes[i])
    raccoon[header[i]] = currentColumn

# Computes the sum of a numeric list
def computeSUM(inputData):
    total = 0;
    for i in range(0,len(inputData)):
        total = total + inputData[i]
    return total

# Computes the average value of a numeric list
def computeAVG(inputData):
    total = computeSUM(inputData)
    mean = total/len(inputData)
    return mean

# Computes the distance between consective pairs of points
def computeDIST(x, y):
    distances = [0]
    for i in range(1,len(x)):
        distances.append(math.sqrt((x[i]-x[i-1])**2 + (y[i]-y[i-1])**2))
    return distances   

# Adds the list (dist) to dictionary (dictName)
def defineDIST(dist, dictName):
    dictName['Distance'] = dist
    return dictName

# Compute summary statistics and update dictionary: incremental movement,
# add incrememtal movement to dictionary, average energy level, average X
# position, average Y position, total movement
movement = computeDIST(raccoon[' X'], raccoon[' Y'])
raccoon = defineDIST(movement, raccoon)
energyAVG = computeAVG(raccoon['Energy Level'])
xAVG = computeAVG(raccoon[' X'])
yAVG = computeAVG(raccoon[' Y'])
totalMovement = sum(raccoon['Distance'])

# Create output file
fout = open("tfield_Georges_life.txt", "w")

# Write header data to output file
fout.write(("Raccoon Name: {0:s}" + os.linesep).format(name))
fout.write(("Average location: {0:.2f}, {1:.2f}" + os.linesep).format(xAVG, yAVG))
fout.write(("Distance traveled: {0:.2f}" + os.linesep).format(totalMovement))
fout.write(("Average Energy Level: {0:.2f}" + os.linesep).format(energyAVG))
fout.write(("Raccoon end state: {0:s}" + os.linesep).format(footer))
fout.write(os.linesep)

# Used to determine which columns to output
keys = ["Day", "Time", ' X', ' Y', ' Asleep', 'Behavior Mode', 'Distance']

# Writes each of the keys to the output file, separated by a tab
def writeHeader(outputFile, columns):
    for i in range(0, len(columns)):
        outputFile.write(columns[i])
        outputFile.write('\t')
    outputFile.write(os.linesep)

# Writes the data for the given keys to the output file, separating values with
# tabs each time on a new line
def writeData(outputFile, columns, dictionary):
    dataLength = len(dictionary[columns[0]])
    for j in range(0, dataLength):
        for i in range(0, len(columns)):
            currentList = dictionary[columns[i]]
            currentVal = str(currentList[j])
            outputFile.write(currentVal)
            outputFile.write('\t')
        outputFile.write(os.linesep)

# Write the header and data to the output file
writeHeader(fout, keys)
writeData(fout, keys, raccoon)

fout.close()













    