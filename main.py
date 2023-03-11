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

def determine_dataset(selection):
    if(selection == 1):
        df = l.small_dataset_as_df()
    if(selection == 2):
        df = l.large_dataset_as_df()
    if(selection == 3):
        df = l.custom_small_dataset_as_df()
    if(selection == 4):
        df = l.custom_large_dataset_as_df()
    return df

def main():
    s = SearchAlgo()
    search_algo_choice = retrieve_search_algo_choice()
    selection = full_algo()
    normalized = int(input("\nEnter 0 for original data\nEnter 1 for normalized data: "))
    df = None
    df = determine_dataset(selection)
    if(normalized):
        df = l.normalize_dataset(df)

    if(search_algo_choice == 1):
        s.feature_selection(len(df.columns)-1,df)
    else:
        s.feature_selection(len(df.columns)-1,df,False)
if __name__ == "__main__":
    main()