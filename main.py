import geopandas as gpd
import matplotlib.pyplot as plt

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