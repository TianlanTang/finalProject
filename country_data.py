import csv

class CountryData:
    def __init__(self, filename: str):
        self.filename = filename
        self.country_names, self.data, self.categories = self._load_data()
        self.avgs = self._calculate_averages()
        self.standard_deviation = self._calculate_standard_deviation()

    def _load_data(self) -> tuple[list[str], dict[str, list[float|str]], list[str]]:
        with open(self.filename, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            categories = next(reader)

            # using country name as key
            data = {data[1]: data for data in reader}
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
    
    def get_country_names(self) -> list[str]:
        return self.country_names
    
    def get_categories(self) -> list[str]:
        return self.categories
    
    def get_standard_deviation(self) -> list[float]:
        return self.standard_deviation
    
    def get_country_data_by_name(self, name: str) -> list[float|str]:
        return self.data.get(name, None)

    
if __name__ == "__main__":
    filename = "global_stats_2022.csv"
    country_data = CountryData(filename)
    print("Categories:", country_data.categories)
    print("Averages:", country_data.avgs)
    print("Standard Deviations:", country_data.standard_deviation)
    print("data:", country_data.get_data()["United States"])
    print("countries:", country_data.country_names[:10])
