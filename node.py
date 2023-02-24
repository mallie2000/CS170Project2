import random as r
from copy import deepcopy

def remove_values_from_list(original_list,values_to_remove):
    for value in values_to_remove:
        if(value in original_list):
            original_list.remove(value)
    return original_list

def create_new_node_with_different_feature_set(original_feature_set:list, new_feature_number:int,addFlag = False):
    modified_list_of_features = deepcopy(original_feature_set)
    if(addFlag):
        modified_list_of_features.append(new_feature_number)
    else:
        modified_list_of_features.remove(new_feature_number)
    possible_node = Node(modified_list_of_features)
    return possible_node

def return_best_possible_feature_set_and_accuracy(list_of_potential_node):
    list_of_potential_node.sort(key = lambda x: x.score)
    best_possible_node = list_of_potential_node.pop()
    return best_possible_node

class Node:
    def __init__(self,feature_set = None):
        self.feature_set = []
        self.score = 0
        self.evaluation_function()
        if(feature_set is not None):
            self.feature_set = feature_set

    def evaluation_function(self):
        self.score = round(r.uniform(0,100.00),2)

class SearchAlgo:
    def __init__(self):
        self.highest_accuracy = 0
        self.feature_set_with_highest_accuracy = []


    def update_highest_accuracy_and_best_feature_set(self, best_node:Node):
        if(best_node.score > self.highest_accuracy):
            self.highest_accuracy = best_node.score
            self.feature_set_with_highest_accuracy  = best_node.feature_set

    
    def feature_selection(self,number_of_features,forward_selection_flag = True):
        starting_list_of_features = [x for x in range(1,number_of_features+1)]
        if(forward_selection_flag):
            starting_node = Node() #different
            current_feature_set = [] #different
        else:
            starting_node = Node(starting_list_of_features) #different
            current_feature_set = deepcopy(starting_list_of_features) #different
        print(f"Using all features and 'random' evaluations, I get an accuracy of {starting_node.score}%\n")
        self.highest_accuracy = starting_node.score
        self.feature_set_with_highest_accuracy = starting_node.feature_set
        print("Beginning search\n")

        while(len(starting_list_of_features) != 0):
            list_of_possible_nodes = []
            for feature_num in starting_list_of_features:
                if(forward_selection_flag):
                    possible_node = create_new_node_with_different_feature_set(current_feature_set,feature_num,addFlag=True)
                else:
                    possible_node = create_new_node_with_different_feature_set(current_feature_set,feature_num,addFlag=False)
                print(f"Using feature(s) {possible_node.feature_set} accuracy is {possible_node.score}%")
                list_of_possible_nodes.append(possible_node)
            best_possible_node = return_best_possible_feature_set_and_accuracy(list_of_possible_nodes)
            current_feature_set = best_possible_node.feature_set
            self.update_highest_accuracy_and_best_feature_set(best_possible_node)
            print(f"Feature set {best_possible_node.feature_set} was best, accuracy is {best_possible_node.score}%\n")
            if(forward_selection_flag):
                starting_list_of_features.remove(best_possible_node.feature_set[-1]) #different
            else:
                starting_list_of_features = current_feature_set #different
        print(f"\nFinished Search!! The best feature subset is {self.feature_set_with_highest_accuracy}, which has an accuracy of {self.highest_accuracy}%")
    

        







        
