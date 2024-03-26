import os
import pandas as pd
import geopandas as gpd
from itertools import product
from src.utils.raster_processor import RasterProcessor


class NepalFunction:
    @staticmethod
    def nepal_health_care_type(df):
        df["TYPO_"] = "PHC"
        return df
