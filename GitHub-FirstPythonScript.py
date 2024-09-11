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

selcRegion = arcpy.management.SelectLayerByAttribute('ks_ecoregions', 'NEW_SELECTION', "US_L3NAME = 'Flint Hills'")
Buffer = arcpy.analysis.Buffer(selcRegion,'Buffer', '10 Kilometers')
arcpy.analysis.Clip(selcRegion, Buffer,'clippedRivers')
arcpy.management.CalculateGeometryAttributes('clippedRivers' , [['riverlenght', 'LENGTH']], 'MILES_US')
arcpy.da.SearchCursor('fileStats', 'SUM_riverlenght') 

