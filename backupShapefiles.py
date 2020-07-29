# Importing the arcpy package
import arcpy
# Importing the datetime package
import datetime

# Setting up your workspace. Python will read from the folder you specify here
arcpy.env.workspace = 'C:/input/'
# Enable overwriting arcpy output results
# If this option is not set to True, you cannot run the geoprocessing more than once
arcpy.env.overwriteOutput = True
# Specify the output folder
outputFolder = 'C:/output/'

# Define an object named shapefiles.
# This object is basically a list of shapefiles under the workspace.
# If you select the workspace as GDB, the object will be a list of feature classes.
shapefiles = arcpy.ListFeatureClasses()

# Loop through the list object
for sf in shapefiles:
    # Create a copy of the file and attach to the new name the current date.
    # Then save the output in the outputFolder path you selected
    arcpy.Copy_management(sf, outputFolder + sf[0:-4] + '_' + str(datetime.date.today()) + '.shp')

# These are confirmation messages that everything went well
print('Done backing up for ' + str(datetime.date.today()))
print('Origin folder -> ' + arcpy.env.workspace)
print('Destination folder -> ' + outputFolder)
