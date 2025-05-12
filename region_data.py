import csv

class RegionData:
    def __init__(self, filename: str):
        self.filename = filename
        self.region_names, self.data, self.categories = self._load_data()
        self.avgs = self._calculate_averages()
        self.standard_deviation = self._calculate_standard_deviation()

    def _load_data(self) -> tuple[list[str], dict[str, list[float|str]], list[str]]:
        with open(self.filename, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            categories = next(reader)

            # using region name as key
            data = {data[0]: data for data in reader}
        return list(data.keys()), data, categories


    def _calculate_averages(self) -> list[float]:
        if not self.data:
            return []

        sums = [0] * len(self.categories)
        counts = len(self.data.keys()) 
        for row in self.data.values():
            for i in range(len(row)):
                try:
                    sums[i] += float(row[i])
                # row[i] is not a number, may be the continent name, just skip
                except ValueError:
                    continue
        avgs = [s / counts if counts > 0 else 0 for s in sums]
        return avgs
    
    def _calculate_standard_deviation(self) -> list[float]:
        if not self.data:
            return []

        std_devs = [0] * len(self.categories)
        counts = len(self.data.keys()) 
        for row in self.data.values():
            for i in range(len(row)):
                try:
                    std_devs[i] += (float(row[i]) - self.avgs[i]) ** 2
                except ValueError:
                    continue
        std_devs = [(s / counts) ** 0.5 if counts > 0 else 0 for s in std_devs]
        return std_devs

    def get_data(self) -> dict[str, list[float|str]]:
        return self.data
    
    def get_region_names(self) -> list[str]:
        return self.region_names
    
    def get_categories(self) -> list[str]:
        return self.categories
    
    def get_standard_deviation(self) -> list[float]:
        return self.standard_deviation
    
    def get_region_data_by_name(self, name: str) -> list[float|str]:
        return self.data.get(name, None)
    
    def get_countries_by_population(self, min_population: int = 0) -> list[str]:

        countries = []
        population_index = self.categories.index("population")
        
        for region_name, region_data in self.data.items():
            try:
                population = float(region_data[population_index])
                if population >= min_population:
                    countries.append(region_name)
            except (ValueError, TypeError, IndexError):
                # Skip countries with invalid population data
                continue
                
        return countries

    
if __name__ == "__main__":
    filename = "global_stats_2022.csv"
    region_data = RegionData(filename)
    print("Categories:", region_data.categories)
    print("Averages:", region_data.avgs)
    print("Standard Deviations:", region_data.standard_deviation)
    print("data:", region_data.get_data()["United States"])
    print("countries:", region_data.region_names[:10])
