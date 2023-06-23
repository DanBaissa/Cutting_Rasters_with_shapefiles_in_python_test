import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import show


# Load the shapefile
gdf = gpd.read_file('Data/World_Countries/World_Countries_Generalized.shp')

# Print the column names of the shapefile
print(gdf.columns)

# Print the contents of the shapefile
print(gdf)

# Plot the shapefile
gdf.plot()
plt.show()


# Select Ethiopia from the COUNTRY column
ethiopia = gdf[gdf['COUNTRY'] == 'Ethiopia']

# Print the contents of the selected row
print(ethiopia)

# Plot the polygon of Ethiopia
ethiopia.plot()
plt.show()

# Load the GeoTIFF file
with rasterio.open('Data/DMSP_Data/F18_20130101_20130131.cloud2.light1.marginal0.glare2.line_screened.avg_vis.tif') as src:
    img = src.read()

    # Get the extent of the raster
    left, bottom, right, top = src.bounds
    print('Left:', left, 'Bottom:', bottom, 'Right:', right, 'Top:', top)

# Plot the GeoTIFF file
plt.figure(figsize=(10, 10))
show(img)
plt.show()