import statistics


def display_main_menu():

    print("Enter some numbers separated by commas (e.g 5, 67, 32)")


def get_user_input():

    numbers_string = input()
    string_list = numbers_string.split(",")
    numbers_float = [float(x) for x in string_list]
    return numbers_float


def calc_average(numbers_list):

    avg = sum(numbers_list)/len(numbers_list)
    return avg


def find_min_max(numbers_list):

    max_temp = max(numbers_list)
    min_temp = min(numbers_list)
    max_min_list = [min_temp, max_temp]
    return max_min_list


def sort_temperature(numbers_list):

    numbers_list.sort(key=float)
    return numbers_list


def calcu_median_temperature(numbers_list):

    median_list = statistics.median(numbers_list)
    return median_list


def main():

    display_main_menu()
    numbers_list = get_user_input()
    avg_temp = calc_average(numbers_list)
    print("The average temperature is ", avg_temp)
    minmax = find_min_max(numbers_list)
    print("The minimum and maximum temperature is ", minmax)
    sort_temperature(numbers_list)
    median_temp = calcu_median_temperature(numbers_list)
    print("The median temperature is ", median_temp)


if __name__ == "__main__":
    main()
