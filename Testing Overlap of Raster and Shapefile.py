import geopandas as gpd
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt

# Load the shapefile and select Ethiopia
gdf = gpd.read_file('Data/World_Countries/World_Countries_Generalized.shp')
ethiopia = gdf[gdf['COUNTRY'] == 'Ethiopia']

# Load the GeoTIFF file
with rasterio.open('Data/DMSP_Data/F18_20130101_20130131.cloud2.light1.marginal0.glare2.line_screened.avg_vis.tif') as src:
    img = src.read()

    # Get the extent of the raster
    left, bottom, right, top = src.bounds

# Create a new figure and axes
fig, ax = plt.subplots()

# Plot the raster on the axes
show(img, extent=[left, right, bottom, top], ax=ax)

# Plot the shapefile on the same axes
ethiopia.plot(ax=ax, facecolor='none', edgecolor='red')

# Display the plot
plt.show()
