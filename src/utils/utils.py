import os
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
