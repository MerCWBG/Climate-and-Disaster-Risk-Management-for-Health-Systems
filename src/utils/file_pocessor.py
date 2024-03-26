import os
import pandas as pd
import geopandas as gpd
from itertools import product
from src.utils.raster_processor import RasterProcessor


class FileProcessor:
    @staticmethod
    def read_tif(file_path, type="point"):
        processor = RasterProcessor(file_path)
        if type == "point":
            data = processor.generate_points()
        if type == "polygon":
            data = processor.generate_polygons()
        data.crs = "EPSG:4326"
        return data

    @staticmethod
    def read_csv(file_path):
        return pd.read_csv(file_path)

    @staticmethod
    def read_shapefile(file_path):
        return gpd.read_file(file_path)

    @staticmethod
    def read_geopackage(file_path):
        """Reads a GeoPackage file and returns a GeoDataFrame."""
        gdf = gpd.read_file(file_path)
        gdf.crs = "EPSG:4326"
        return gdf

    @staticmethod
    def save_to_excel(data_frame, output_path):
        data_frame.to_excel(output_path, index=False)

    @staticmethod
    def save_to_geopackage(geo_data_frame, output_path, output_name, layer_name=None):
        output_path = f"{output_path}{output_name}"
        geo_data_frame.to_file(output_path, layer=layer_name, driver="GPKG")


class FileLister:

    @staticmethod
    def drop_extension(filename):
        """
        Drop the file extension from a filename.

        Parameters:
            filename (str): The filename including the extension.

        Returns:
            str: The filename without the extension.
        """
        # Find the position of the last dot in the filename
        dot_position = filename.rfind(".")

        # If a dot is found, return the substring before it, otherwise return the original filename
        if dot_position != -1:
            return filename[:dot_position]
        else:
            return filename

    @staticmethod
    def list_files(directory):
        files_list = []
        try:
            # List all files in the directory
            files = os.listdir(directory)
            # Iterate over the files and add their names and paths to the list
            for file in files:
                file_path = os.path.join(directory, file)
                if os.path.isfile(file_path):
                    files_list.append((FileLister.drop_extension(file), file_path))
            return files_list
        except Exception as e:
            raise Exception(f"Error listing files in directory: {e}")

    @staticmethod
    def generate_combinations(list_of_lists):
        """
        Generates all combinations of elements from the inner lists.

        Args:
        list_of_lists (list): A list of lists.

        Returns:
        list: A list containing all combinations of elements.
        """
        return list(product(*list_of_lists))

    @staticmethod
    def get_name_multiple_dir(list_of_paths):
        temp_resp = []
        for path in list_of_paths:
            files = FileLister.list_files(path)
            temp_resp.append(files)
        resp = FileLister.generate_combinations(temp_resp)

        return resp
