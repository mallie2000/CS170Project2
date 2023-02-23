import random as r
from copy import deepcopy

def remove_values_from_list(original_list,values_to_remove):
    for value in values_to_remove:
        if(value in original_list):
            original_list.remove(value)
    return original_list

def create_new_node_with_different_feature_set(original_feature_set:list, new_feature_number:int):
    modified_list_of_features = deepcopy(original_feature_set)
    modified_list_of_features.remove(new_feature_number)
    possible_node = Node(modified_list_of_features)
    return possible_node

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


    def exploreBestFeatures(self,list_of_features,initialFeatures = None):
        nodes_to_explore = []
        for feature_num in list_of_features:
            if(initialFeatures == None):
                new_node = Node([feature_num])
            else:
                new_node = Node([feature_num]+initialFeatures)
            print(f"Using feature(s) {new_node.feature_set} accuracy is {new_node.score}%")
            nodes_to_explore.append(new_node)
        nodes_to_explore.sort(key = lambda x: x.score)
        print()
        best_feature = nodes_to_explore.pop()
        print(f"Feature set {best_feature.feature_set} was best, accuracy is {best_feature.score}%")
        if(best_feature.score > self.highest_accuracy):
            self.highest_accuracy = best_feature.score
            self.feature_set_with_highest_accuracy = best_feature.feature_set
        return best_feature

    def forwardSelection(self,number_of_features):
        startingNode = Node()
        print(f"Using no features and 'random' evaluations, I get an accuracy of {startingNode.score}%\n")
        self.highest_accuracy = startingNode.score
        print("Beginning search\n")
        feature_list  = [x for x in range(1,number_of_features+1)]
        best_node_feature_set = None
        while(len(feature_list) != 0):
            best_node_feature_set = self.exploreBestFeatures(feature_list,best_node_feature_set).feature_set
            feature_list = self.remove_values_from_list(feature_list,best_node_feature_set)
        print(f"\nFinished Search!! The best feature subset is {self.feature_set_with_highest_accuracy}, which has an accuracy of {self.highest_accuracy}%") 
    
    def backwards_elimination(self,number_of_features):
        starting_list_of_features = [x for x in range(1,number_of_features+1)]
        starting_node = Node(starting_list_of_features)
        print(f"Using all features and 'random' evaluations, I get an accuracy of {starting_node.score}%\n")
        self.highest_accuracy = starting_node.score
        self.feature_set_with_highest_accuracy = starting_list_of_features
        print("Beginning search\n")


        while(len(starting_list_of_features) != 0):
            list_of_possible_nodes = []
            for feature_num in starting_list_of_features:
                possible_node = create_new_node_with_different_feature_set(starting_list_of_features,feature_num)
                print(f"Using feature(s) {possible_node.feature_set} accuracy is {possible_node.score}%")
                list_of_possible_nodes.append(possible_node)
            list_of_possible_nodes.sort(key = lambda x: x.score)
            best_possible_node = list_of_possible_nodes.pop()

            if(best_possible_node.score > self.highest_accuracy):
                self.highest_accuracy = best_possible_node.score
                self.feature_set_with_highest_accuracy  = best_possible_node.feature_set
            print(f"Feature set {best_possible_node.feature_set} was best, accuracy is {best_possible_node.score}%\n")
            starting_list_of_features = best_possible_node.feature_set
        print(f"\nFinished Search!! The best feature subset is {self.feature_set_with_highest_accuracy}, which has an accuracy of {self.highest_accuracy}%")
        






        
