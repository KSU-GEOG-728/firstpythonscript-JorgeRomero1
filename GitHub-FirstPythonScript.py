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
## selectRiver it stores the selected river "Kansas River"


selectRiver = arcpy.SelectLayerByAttribute_management('ks_major_rivers', 'NEW_SELECTION', "GNIS_NAME = 'Kansas River'")
selectCounties = arcpy.SelectLayerByLocation_management('Tiger2010_Census_County', 'INTERSECT', selectRiver, "", 'NEW_SELECTION')
arcpy.CopyFeatures_management(selectCounties, 'selectedCounties')
arcpy.management.CalculateGeometryAttributes('clippedRivers' , [['riverlenght', 'LENGTH']], 'MILES_US')