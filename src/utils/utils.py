import os
import re
import geopandas as gpd


class GeoDataFrameOperations:
    @staticmethod
    def filter_data(gdf, column, condition):
        """Filter GeoDataFrame based on a condition."""
        filtered_gdf = gdf[gdf[column] == condition]
        return filtered_gdf

    @staticmethod
    def drop_nan_geometry(gdf):
        """Drop rows with NaN geometry in a GeoDataFrame."""
        return gdf.dropna(subset=["geometry"])

    @staticmethod
    def calculate_damage(gdf, substantial_damage, complete_destruction):
        """Calculate damage based on 'value', 'substantial_damage', and 'complete_destruction'."""

        def calculate(row):
            value = row["value"]
            if complete_destruction is None and substantial_damage is None:
                return "exposed"
            elif complete_destruction is None and substantial_damage is not None:
                if value >= substantial_damage:
                    return "substantial damage"
                else:
                    return 0
            elif complete_destruction is not None and substantial_damage is not None:
                if value >= substantial_damage and value < complete_destruction:
                    return "substantial damage"
                elif value >= complete_destruction:
                    return "complete destruction"
                else:
                    return 0
            else:
                return 0

        gdf["damage"] = gdf.apply(calculate, axis=1)
        gdf = gdf[gdf["damage"] != 0]
        gdf = gdf.reset_index(drop=True)
        return gdf


class custom_preprocessing_infrastructure_return_file:

    @staticmethod
    def append_period_to_filelist(files, return_periods):
        # Combinar archivos con períodos de retorno
        combined_files = []
        for file_data in files:
            # Utilizar expresión regular para extraer el número del período de retorno del nombre del archivo
            match = re.search(r"(\d+)", file_data[0])
            if match:
                period_number = int(match.group())
                # Verificar si el número del período de retorno está en la lista de períodos de retorno
                if period_number in return_periods:
                    combined_files.append(file_data + (period_number,))
        return combined_files
