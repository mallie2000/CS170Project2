import random as r
class Node:
    def __init__(self,feature_set = None):
        if feature_set != None:
            self.feature_set = feature_set
        else:
            self.feature_set = []
        self.score = 0
        self.evaluation_function()

    def evaluation_function(self):
        self.score = round(r.uniform(0,100.00),2)

class SearchAlgo:
    def __init__(self):
        self.max_accuracy = 0
        self.best_feature_set = []

    def removeValuesFromFeatureList(self,original_list,values_to_remove):
        for value in values_to_remove:
            if(value in original_list):
                original_list.remove(value)
        return original_list

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
        if(best_feature.score > self.max_accuracy):
            self.max_accuracy = best_feature.score
            self.best_feature_set = best_feature.feature_set
        return best_feature

    def forwardSelection(self,number_of_features):
        startingNode = Node()
        print(f"Using no features and 'random' evaluations, I get an accuracy of {startingNode.score}%\n")
        self.max_accuracy = startingNode.score
        print("Beginning search\n")
        feature_list  = [x for x in range(1,number_of_features+1)]
        best_node_feature_set = None
        while(len(feature_list) != 0):
            best_node_feature_set = self.exploreBestFeatures(feature_list,best_node_feature_set).feature_set
            feature_list = self.removeValuesFromFeatureList(feature_list,best_node_feature_set)
        print(f"Finished Search!! The best feature subset is {self.best_feature_set}, which has an accuracy of {self.max_accuracy}%")





        
