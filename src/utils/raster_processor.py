import rasterio
import geopandas as gpd
from shapely.geometry import Polygon
from tqdm import tqdm


class RasterProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def pixel_to_map_coordinates(self, transform, col, row):
        x, y = transform * (col, row)
        return x, y

    def generate_polygons(self):
        """Genera polígonos a partir de un archivo raster."""
        polygons = []

        with rasterio.open(self.file_path) as src:
            data = src.read()
            # print(f"Número de bandas: {src.count}")
            # print(f"Tamaño de la matriz: {data.shape}")
            transform = src.transform

            for i in range(src.count):
                band_data = data[i, :, :]

                for row in tqdm(range(band_data.shape[0])):
                    for col in range(band_data.shape[1]):
                        value = band_data[row, col]

                        if value > 0:
                            x1, y1 = self.pixel_to_map_coordinates(transform, col, row)
                            x2, y2 = self.pixel_to_map_coordinates(
                                transform, col + 1, row
                            )
                            x3, y3 = self.pixel_to_map_coordinates(
                                transform, col + 1, row + 1
                            )
                            x4, y4 = self.pixel_to_map_coordinates(
                                transform, col, row + 1
                            )

                            poly = Polygon([(x1, y1), (x2, y2), (x3, y3), (x4, y4)])

                            polygon_data = {
                                "band": i + 1,
                                "value": value,
                                "geometry": poly,
                            }
                            polygons.append(polygon_data)

        gdf = gpd.GeoDataFrame(polygons)
        return gdf

    def generate_points(self):
        """Generates points from a raster file."""
        points = []

        with rasterio.open(self.file_path) as src:
            data = src.read()
            transform = src.transform

            for i in range(src.count):
                band_data = data[i, :, :]

                for row in tqdm(range(band_data.shape[0])):
                    for col in range(band_data.shape[1]):
                        value = band_data[row, col]

                        if value > 0:
                            # Calculate the coordinates of the center of the pixel
                            # x, y = self.pixel_to_map_coordinates(transform, col + 0.5, row + 0.5)

                            x, y = self.pixel_to_map_coordinates(transform, col, row)

                            point_data = {"band": i + 1, "value": value, "x": x, "y": y}
                            points.append(point_data)

        gdf = gpd.GeoDataFrame(
            points,
            geometry=gpd.points_from_xy(
                [p["x"] for p in points], [p["y"] for p in points]
            ),
        )
        return gdf
