from region_data import RegionData
from cal_stats import compare_stats, compare_string
from trie_tree import TrieTree
import random
import time

def main():

    # load data
    filename = "global_stats_2022.csv"
    region_data = RegionData(filename)
    categories = region_data.get_categories()
    
    # Select difficulty level
    print("Select difficulty level:")
    print("1 - Easy")
    print("2 - Hard")
    print("3 - Challenge")
    
    while True:
        try:
            difficulty = int(input("Choose a difficulty (1-3): "))
            if 1 <= difficulty <= 3:
                break
            else:
                print(f"{difficulty} not valid, please choose betwween 1 and 3.")
        except ValueError:
            print("Please enter a number between 1 and 3.")
    
    # choose countries based on difficulty
    if difficulty == 1:
        # easy: population > 30,000,000
        eligible_countries = region_data.get_countries_by_population(30000000)
    elif difficulty == 2:
        # Hard: population > 10,000,000
        eligible_countries = region_data.get_countries_by_population(10000000)
    else:
        # Challenge: all countries
        eligible_countries = region_data.get_region_names()

     # initialize the trie tree with region names
    region_trie = TrieTree(eligible_countries)
    
    # Randomly select a target region
    if eligible_countries:
        target_name = random.choice(eligible_countries)
        print(f"Guess a country or region with a population of at least {30 if difficulty == 1 else 10 if difficulty == 2 else 0} million.")
    else:
        raise ValueError("No eligible countries found based on the selected difficulty level.")
    
    # get target region data
    target_data = region_data.get_region_data_by_name(target_name)
    
    # ten chances to guess the region name
    chances = 10    # print the categories
    infos = [categories]
    
    # count the time.
    start_time = time.time()
    
    while chances:

        current_name = input("Enter the region name: ")

        # get region data
        current_data = region_data.get_region_data_by_name(current_name)

        if not current_data:
            print("Country or Region not found.")
            # pattern match
            similar_countries = region_trie.find_similar(current_name, max_distance=2)
  
            # prefix search
            prefix = current_name.strip()

            matching_countries = []
            # not search for empty string
            if len(prefix) > 0: 
                matching_countries = region_trie.starts_with(prefix)

            if similar_countries or matching_countries:
                print("Maybe you meant:")
            for i, region in enumerate(list(set(similar_countries + matching_countries))):  
                print(f"{i+1}. {region}")
            continue    

        # Name matching a region
        info = []
        # get stats
        for i in range(len(categories)):
            cur_stat = current_data[i]
            target_stat = target_data[i]

            if cur_stat == None:
                cur_stat = 'N/A'
            
            try:
                # is a number 
                cur_stat = float(cur_stat)
                target_stat = float(target_stat)
                # compare stats
                compare_stat = compare_stats(cur_stat, target_stat, region_data.get_standard_deviation()[i])
                info.append(compare_stat)

            except ValueError:
                # compare string
                compare_str = compare_string(cur_stat, target_stat)
                info.append(compare_str)

        infos.append(info[:])
        print('\n'.join([('|'.join(line)) for line in infos]))        

        # correct answer
        if current_name == target_name:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Correct! You guessed the region in {10 - chances} tries and it took you {elapsed_time:.0f} seconds.")
            return

        chances -= 1

    # show the right answer
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Wrong! The correct country or region is {target_name}.")
    print(f"Country or Region data: {('|').join(target_data)}")

if __name__ == "__main__":
    main()

