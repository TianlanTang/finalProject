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
    target_data = country_data.get_country_data_by_name(target_name)
    
    # ten chances to guess the country name
    chances = 10

    # print the categories
    infos = ' '.join(categories) + '\n'
    
    while chances:
        # get country name
        current_name = input("Enter the country name: ")
        
        # get country data
        current_data = country_data.get_country_data_by_name(current_name)
        
        if not current_data:
            print("Country not found.")
            continue

        # get stats
        for i, category in enumerate(categories):
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
                infos += compare_stat + ' '


            except ValueError:
        
                # compare string
                compare_str = compare_string(cur_stat, target_stat)
                infos += compare_str + ' '

        # switch to next line
        print(infos)
        infos += '\n'

        # check if the country name is correct
        if current_name == target_name:
            print("Correct!")
            break

        chances -= 1


if __name__ == "__main__":
    main()


# TODO: 1. 吧main函数放到一个单独的文件中
# TODO: 2. 格式化输出为表格
# TODO: 3. 增加难易度模式 开始如果选择简单 就只从人口>一定数量的国家中选择