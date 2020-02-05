#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:33:45 2020

@author: tfield
"""

PROCESSING SCRIPT NAME: tfield_Evaluate_Raccoon_Life.py
INPUT FILE NAME:        2008Male00006.txt
OUTPUT FILE NAME:       tfield_Georges_life.txt

The processing script takes the input file, reads in the contents, and
separates it into three sections (header, data, and footer). The name of the
raccoon is taken from the footer. A dictionary is created for each list of
data, with the data stored as the most appropriate type (str, int, float).
Summary statistics are calculated and the distance the raccoon traveled is
added to the dictionary. Sumamary statistics, along with the Day, Time, X, Y,
Asleep, Behavior Mode, and Distance parameters are written to the output file
for all time points. 