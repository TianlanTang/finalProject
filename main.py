from country_data import CountryData
from cal_stats import compare_stats, compare_string
import random

def main():
    
    # load data
    filename = "global_stats_2022.csv"
    country_data = CountryData(filename)
    categories = country_data.get_categories()

    # randomly select a country
    target_name = random.choice(country_data.get_country_names())
    print(f"Target Country: {target_name}")

    # for debugging
    target_name = "Martinique"

    target_data = country_data.get_country_data_by_name(target_name)
    
    # ten chances to guess the country name
    chances = 10

    # print the categories
    infos = [categories]
    
    while chances:
        # get country name
        current_name = input("Enter the country name: ")
        
        # get country data
        current_data = country_data.get_country_data_by_name(current_name)
        
        if not current_data:
            print("Country not found.")
            continue

        info = []
        # get stats
        for i in range(len(categories)):
            # get stats
            cur_stat = current_data[i]
            target_stat = target_data[i]

            if cur_stat == None:
                cur_stat = 'N/A'
            
            try:
                # is a number 
                cur_stat = float(cur_stat)
                target_stat = float(target_stat)
                # compare stats
                compare_stat = compare_stats(cur_stat, target_stat, country_data.get_standard_deviation()[i])
                info.append(compare_stat)


            except ValueError:
        
                # compare string
                compare_str = compare_string(cur_stat, target_stat)
                info.append(compare_str)

        infos.append(info[:])
        print('\n'.join([('|'.join(line)) for line in infos]))

        # check if the country name is correct
        if current_name == target_name:
            print("Correct!")
            break

        chances -= 1


if __name__ == "__main__":
    main()


# TODO: 1. 增加难易度模式 开始如果选择简单 就只从人口>一定数量的国家中选择
# TODO: 2. 用字典树进行近似提示以及前缀提示
# TODO: 3. 增加计时器, 统计时间