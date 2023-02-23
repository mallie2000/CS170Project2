from node import SearchAlgo
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

def main():
    s = SearchAlgo()
    number_of_features = retrieve_num_of_features()
    search_algo = retrieve_search_algo_choice()
    if(search_algo == 1):
        s.forwardSelection(number_of_features)
    if(search_algo == 2):
        s.backwards_elimination(number_of_features)

if __name__ == "__main__":
    main()