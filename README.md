# QUAD TREE

Uniteractive script for sorting points provided in *.geoJSON file.

1. load geo.JSON filen with named import.geojson
Run split.py

Split.py is working togehter with quadtree.py. - split.py imports functions from quadtree.py
  It is necessary to have thos two files in one folder.

Script is by deaful working with quad tree algortitm and runs until is less than 50 point is each quad.
Each quad is defined by new crerated ID

In the end its creates new GeoJson file called output.geojson with new coordinates and new IDs included.

