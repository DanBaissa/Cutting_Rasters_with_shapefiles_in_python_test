import geopandas as gpd
import rasterio
from rasterio.plot import show
from rasterio.mask import mask
import matplotlib.pyplot as plt

# Load the shapefile and select Ethiopia
gdf = gpd.read_file('Data/World_Countries/World_Countries_Generalized.shp')
ethiopia = gdf[gdf['COUNTRY'] == 'Ethiopia']

# Load the GeoTIFF file
with rasterio.open('Data/DMSP_Data/F18_20130101_20130131.cloud2.light1.marginal0.glare2.line_screened.avg_vis.tif') as src:
    # Convert the Ethiopia polygon to the same CRS as the raster
    ethiopia = ethiopia.to_crs(src.crs)

    # Cut the raster with the Ethiopia polygon
    out_image, out_transform = mask(src, ethiopia.geometry, crop=True)
    out_meta = src.meta

# Update the metadata to reflect the new raster (e.g., new dimensions, transform)
out_meta.update({
    "driver": "GTiff",
    "height": out_image.shape[1],
    "width": out_image.shape[2],
    "transform": out_transform,
})

# Create a new figure and axes
fig, ax = plt.subplots()

# Plot the cut raster on the axes
show(out_image, transform=out_transform, ax=ax)

# Display the plot
plt.show()
