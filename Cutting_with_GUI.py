import os
import tkinter as tk
from tkinter import filedialog, ttk
import geopandas as gpd
import rasterio
from rasterio.mask import mask

# Load the shapefile and get the list of countries
gdf = gpd.read_file('Data/World_Countries/World_Countries_Generalized.shp')
countries = gdf['COUNTRY'].unique().tolist()

# Create the main window
window = tk.Tk()

# Create and pack the widgets
folder_label = tk.Label(window, text="DMSP datasets folder:")
folder_label.pack()

folder_var = tk.StringVar()
folder_entry = tk.Entry(window, textvariable=folder_var)
folder_entry.pack()

def browse_datasets_folder():
    folder_var.set(filedialog.askdirectory())

browse_button = tk.Button(window, text="Browse", command=browse_datasets_folder)
browse_button.pack()

output_label = tk.Label(window, text="Output folder:")
output_label.pack()

output_var = tk.StringVar()
output_entry = tk.Entry(window, textvariable=output_var)
output_entry.pack()

def browse_output_folder():
    output_var.set(filedialog.askdirectory())

output_button = tk.Button(window, text="Browse", command=browse_output_folder)
output_button.pack()

country_label = tk.Label(window, text="Country:")
country_label.pack()

country_var = tk.StringVar()
country_dropdown = ttk.Combobox(window, textvariable=country_var, values=countries)
country_dropdown.pack()

def crop_rasters():
    country_name = country_var.get()  # get the selected country name
    country = gdf[gdf['COUNTRY'] == country_name]
    datasets_folder = folder_var.get()
    output_folder = output_var.get()

    for file_name in os.listdir(datasets_folder):
        if file_name.endswith('.tif'):
            with rasterio.open(os.path.join(datasets_folder, file_name)) as src:
                country = country.to_crs(src.crs)
                out_image, out_transform = mask(src, country.geometry, crop=True)
                out_meta = src.meta
                out_meta.update({
                    "driver": "GTiff",
                    "height": out_image.shape[1],
                    "width": out_image.shape[2],
                    "transform": out_transform,
                })
                # Append the country name to the front of the output file name
                output_file_name = f"{country_name}_{file_name}"
                with rasterio.open(os.path.join(output_folder, output_file_name), 'w', **out_meta) as dest:
                    dest.write(out_image)


crop_button = tk.Button(window, text="Crop rasters", command=crop_rasters)
crop_button.pack()

# Start the main loop
window.mainloop()
