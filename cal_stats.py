PURPLECOLOR = "\033[45;30m"
ORANGECOLOR = "\033[43;30m"
YELLOWCOLOR = "\033[103;30m" 
GREENCOLOR = "\033[42;30m"

def cal_difference_by_standard_deviation(current: float, target: float, std_dev: float) -> float:
    """
    Calculate the difference between the current and target values in terms of standard deviations.
    
    Args:
        current (float): The current value.
        target (float): The target value.
        std_dev (float): The standard deviation of the dataset.
    
    Returns:
        float: The difference in terms of standard deviations.
    """
    if std_dev == 0:
        return 0
    return (current - target) / std_dev

def compare_stats(current: float, target: float, std_dev: float) -> str:

    difference = cal_difference_by_standard_deviation(current, target, std_dev)  # Assuming std_dev is 1 for simplicity

    if difference > 3:
        return PURPLECOLOR + ' ' + str(round(current, 0)) + ' ' + '↓' * 3 + ' ' + "\033[0m"
    elif difference > 1 and difference <= 3:
        return ORANGECOLOR + ' ' + str(round(current, 0)) + ' ' + '↓' * 2 + ' ' + "\033[0m"
    elif difference > 0 and difference <= 1:
        return YELLOWCOLOR + ' '+ str(round(current, 0)) + ' ' + '↓' + ' ' + "\033[0m"
    elif difference < -3:
        return PURPLECOLOR + ' '+ str(round(current, 0)) + ' ' + '↑' * 3 + ' ' + "\033[0m"
    elif difference < -1 and difference >= -3:
        return ORANGECOLOR + ' '+ str(round(current, 0)) + ' ' + '↑' * 2 + ' ' + "\033[0m"
    elif difference < 0 and difference >= -1:
        return YELLOWCOLOR + ' '+ str(round(current, 0)) + ' ' + '↑' + ' ' + "\033[0m"
    else:
        return GREENCOLOR + ' '+ str(round(current, 0)) + ' ' + "\033[0m"
    
def compare_string(current: str, target: str) -> str:

    if current == target:
        return GREENCOLOR + ' ' + str(current) + ' ' + "\033[0m"
    elif current != target:
        return PURPLECOLOR + ' ' + str(current) + ' ' + "\033[0m"


    
if __name__ == "__main__":
    # test example
    current = 130
    target = 110
    std_dev = 10
    
    stats = compare_stats(current, target, std_dev)
    print(f"Stats: {stats}")

    current_str = "A"
    target_str = "B"

    result_str = compare_string(current_str, target_str)
    print(f"String comparison result: {result_str}")

