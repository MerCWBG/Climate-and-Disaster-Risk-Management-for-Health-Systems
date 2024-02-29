import geopandas as gpd


class population:
    def __init__(self, id, polygon, population_qty):
        self.id = id
        self.polygon = polygon
        self.population_qty = population_qty


class PopulationData:
    @staticmethod
    def read_shapefile(shapefile_path):
        """
        Lee un archivo shapefile que contiene información sobre la población y devuelve un GeoDataFrame.
        Args:
            shapefile_path (str): La ruta al archivo shapefile.
        Returns:
            GeoDataFrame: Un GeoDataFrame que contiene los datos de población.
        """
        gdf = gpd.read_file(shapefile_path)
        return gdf

    @staticmethod
    def create_population_objects(gdf):
        """
        Crea objetos Population a partir de un GeoDataFrame.
        Args:
            gdf (GeoDataFrame): El GeoDataFrame que contiene los datos de población.
        Returns:
            list: Una lista de objetos Population.
        """
        populations = []
        for index, row in gdf.iterrows():
            population = Population(row["ID"], row["geometry"], row["Population"])
            populations.append(population)
        return populations
