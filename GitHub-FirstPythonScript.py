#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: GitHub-FirstPythonScript.py
    Author: Jorge Romero 
    Description:  Calculate total river miles with expanded ecoregion boundary
    Date created: 09/11/2024
    Python Version: 3.9.16
"""

# Import arcpy module and allow overwrites
import arcpy
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = "C:/Users/jorgeromero/Documents/firstpythonscript/GISProject/ExerciseData.gdb"

#Performe Geoprocessing 

## selectRegion contains FLint Hills region selected by attributes. 
selcRegion = arcpy.SelectLayerByAttribute_management('ks_ecoregions', 'NEW_SELECTION', "US_L3NAME = 'Flint Hills'")

## Buffer stores a buffer of 10 Km  from the selcRegion
arcpy.Buffer_analysis(selcRegion,'Buffer', '10 Kilometers')

## clippedRivers it stores and clip all the rivers that are within the buffer
arcpy.Clip_analysis('ks_major_rivers', 'Buffer', 'clippedRivers')

## Create a new column called "riverLength" that calculates the length of each river  in miles
arcpy.CalculateGeometryAttributes_management('clippedRivers' , [['riverLength', 'LENGTH']], 'MILES_US')

## Create an empty list to store the length of each river
riversLength = []

## Access to the attribute table of clippedRivers 
rows = arcpy.SearchCursor(clippedRivers)

## Iterate in each row of the attribute table to get the length of each river and append to the list 
for row in rows:
    length = row.getValue("riverLength")
    riversLength.append(length)

## Print the sum of the elements in the list riversLenght 
print(f'The total length of the clipped rivers is {sum(riversLength):.2f} Miles')

