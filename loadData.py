import pandas as pd
import numpy as np

def small_dataset_as_df():
    col_names = [i for i in range(1,11)]
    col_names.insert(0,"Feature")
    df = pd.read_csv("small-test-dataset.txt",delim_whitespace=True,header = None, names=col_names)
    return df

def custom_small_dataset_as_df():
    col_names = [i for i in range(1,11)]
    col_names.insert(0,"Feature")
    
    df = pd.read_csv("CS170_Spring_2022_Small_data__2.txt",delim_whitespace=True,header = None, names=col_names)
    return df

def custom_large_dataset_as_df():
    col_names = [i for i in range(1,11)]
    col_names.insert(0,"Feature")
    
    df = pd.read_csv("CS170_Spring_2022_Large_data__02.txt",delim_whitespace=True,header = None, names=col_names)
    return df

def large_dataset_as_df():
    col_names = [i for i in range(1,41)]
    col_names.insert(0,"Feature")
    df = pd.read_csv("Large-test-dataset.txt",delim_whitespace=True,header = None, names=col_names)
    return df

def normalize_dataset(df):
    normalized_df = df.copy()
    for col in df.columns[1::]:
        normalized_df[col] = (normalized_df[col] - normalized_df[col].mean())/normalized_df[col].std()
    return normalized_df


def accuracyFunction(df,feature_set):
    if(len(feature_set) < 1):
        counts = df["Feature"].value_counts()
        class1 = counts[1.0]
        class2 = counts[2.0]
        accuracy = max(class1,class2)/len(df)
        return accuracy
    number_correctly_classfied = 0
    smaller_df_columns = ["Feature"] + feature_set
    smaller_df = df.filter(smaller_df_columns,axis = 1)

    for row_index in range(len(smaller_df)):
        row_of_values = smaller_df.iloc[[row_index]].values.tolist()[0]
        class_label_for_current_row = row_of_values[0]
        data_for_current_row = row_of_values[1:]

        nearest_neighbor_label = classifier(smaller_df, row_index, data_for_current_row)

        if class_label_for_current_row == nearest_neighbor_label:
            number_correctly_classfied += 1 # if predicted label is same as actual label, increment count
    accuracy = number_correctly_classfied / (len(smaller_df)) # calculate the accuracy
    return accuracy

def classifier(smaller_df, row_index, data_for_current_row):
    nearest_neighbor_location = np.inf
    distance = list()
    for sub_row_index in range(len(smaller_df)): # iterate through each row in data for finding the nearest neighbor
        if sub_row_index != row_index:
            v1 = np.array(data_for_current_row)
            v2 = np.array(smaller_df.iloc[[sub_row_index]].values.tolist()[0][1:])
            distance.append([sub_row_index,np.sqrt(np.sum((v1 - v2)**2))])  # calculate the Euclidean distance
        # print(f"{row_index} is closest with {nearest_neighbor_location}")

    distance.sort(key = lambda x: x[1])
    nearest_neighbor_location=distance[0][0]
    nearest_neighbor_label = smaller_df.iloc[nearest_neighbor_location]["Feature"]
    return nearest_neighbor_label



