from node import SearchAlgo
import loadData as l
def retrieve_num_of_features():
    print("Welcome to Muzammil Allie's Feature Selection Algorithm")
    number_of_features = int(input("Please enter the total number of features: "))
    return number_of_features

def retrieve_search_algo_choice():
    search_algo_number = 0
    list_of_algorithms = ["Forward Selection","Backwards Elimination", "Muzammil's Special Search Algo"]
    while(search_algo_number not in range(1,len(list_of_algorithms)+1)):
        print("Type the number of the algorithm you wish to run")
        for index, algo in enumerate(list_of_algorithms):
            print(f"{index+1} {algo}")
        search_algo_number = int(input("Enter your choice here: "))
        print()
    return search_algo_number

def full_algo():
    print("Welcome to Muzammil Allie's classifier")
    print("Enter 1 for small data set")
    print("Enter 2 for large data set")
    print("Enter 3 for custom small data set")
    print("Enter 4 for custom large data set")
    selection = int(input("Enter selection here: "))
    return selection

def main():
    s = SearchAlgo()
    # selection = full_algo()
    # if(selection == 1):
    #     df = l.small_dataset_as_df()
    df = l.custom_large_dataset_as_df()
    dfN = l.normalize_dataset(df)
    s.feature_selection(len(dfN.columns)-1,dfN, False)

    # number_of_features = retrieve_num_of_features()
    # search_algo = retrieve_search_algo_choice()
    # if(search_algo == 1):
    #     s.feature_selection(number_of_features)
    # if(search_algo == 2):
    #     # s.backwards_elimination(number_of_features)
    #     s.feature_selection(number_of_features,False)

if __name__ == "__main__":
    main()