# Import necessary libraries
import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import argparse

# Function to identify geolocation variables in the NetCDF file
def find_geolocation_vars(dataset):
    # Possible names for 2D latitude and longitude variables
    lat_names = ['nav_lat', 'lat', 'latitude']
    lon_names = ['nav_lon', 'lon', 'longitude']

    # Search for latitude and longitude variables in the dataset
    lat_var = lon_var = None
    for var_name in dataset.variables:
        if var_name.lower() in lat_names:
            lat_var = dataset.variables[var_name][:]
        elif var_name.lower() in lon_names:
            lon_var = dataset.variables[var_name][:]
    
    if lat_var is None or lon_var is None:
        raise ValueError("2D Latitude and/or Longitude variables not found in the dataset.")
    
    return lat_var, lon_var

# Function to read and plot data from a NetCDF file
def plot_from_netcdf(file_path, var_name):
    # Open the NetCDF file
    dataset = nc.Dataset(file_path, mode='r')
    
    # Print the metadata of the file
    print(f"Metadata for {file_path}:")
    print(dataset)

    # Check and retrieve 2D latitude and longitude variables
    lat, lon = find_geolocation_vars(dataset)

    # Read the variable data
    if var_name not in dataset.variables:
        raise ValueError(f"Variable '{var_name}' not found in the dataset.")
    
    var_data = dataset.variables[var_name][:]
    var_units = dataset.variables[var_name].units if 'units' in dataset.variables[var_name].ncattrs() else 'Unknown'

    # Close the dataset
    dataset.close()

    # Plot the data (assuming 2D data or slicing 3D/4D data for plotting)
    plt.figure(figsize=(10,6))
    if var_data.ndim == 2:  # 2D variable
        plot_data = var_data
    elif var_data.ndim >= 3:  # 3D/4D variable (e.g., with time dimension)
        plot_data = var_data[0, :, :]  # Plot first time step (if time exists)
    else:
        raise ValueError(f"Unsupported number of dimensions for variable '{var_name}'.")

    # Create a smooth plot with a colorful colormap
    plt.contourf(lon, lat, plot_data, cmap='viridis', levels=100)  # 'viridis' for a colorful and smooth scale, 100 levels for smoother transition
    plt.colorbar(label=f'{var_name} ({var_units})')
    
    # Customize the plot
    plt.title(f'{var_name} at Time Step 0' if var_data.ndim >= 3 else f'{var_name}')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    # Ensure correct tick labels
    plt.grid(True)  # Add grid for better readability
    plt.show()

# Main function to parse command-line arguments and call the plot function
def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description='Plot a variable from a NetCDF file.')
    parser.add_argument('file_path', type=str, help='Path to the NetCDF file')
    parser.add_argument('variable_name', type=str, help='Name of the variable to plot')
    
    # Parse the arguments
    args = parser.parse_args()

    # Call the function to plot the NetCDF data
    plot_from_netcdf(args.file_path, args.variable_name)

# Entry point for the script
if __name__ == '__main__':
    main()

