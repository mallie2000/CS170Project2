import pandas as pd
import numpy as np

def small_dataset_as_df():
    col_names = [i for i in range(1,11)]
    col_names.insert(0,"Feature")
    df = pd.read_csv("small-test-dataset.txt",delim_whitespace=True,header = None, names=col_names)
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

def leave_one_out_cross_validation(data, current_set, feature_to_add):
    number_correctly_classfied = 0
    for i in range(data.shape[0]): # iterate through each row in data
        object_to_classify = data[i,1:] # extract feature values for the current row
        label_object_to_classify = data[i,0] # extract class label for the current row
        nearest_neighbor_distance = np.inf
        nearest_neighbor_location = np.inf
        for k in range(data.shape[0]): # iterate through each row in data for finding the nearest neighbor
            if k != i:
                distance = np.sqrt(np.sum((object_to_classify - data[k,1:])**2)) # calculate the Euclidean distance
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = data[nearest_neighbor_location,0] # extract class label for the nearest neighbor
        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classfied += 1 # if predicted label is same as actual label, increment count
    accuracy = number_correctly_classfied / data.shape[0] # calculate the accuracy
    return accuracy

def testCode(df,feature_set):
    number_correctly_classfied = 0
    smaller_df_columns = ["Feature"] + feature_set
    smaller_df = df.filter(smaller_df_columns,axis = 1)

    for row_index in range(len(smaller_df)):
        row_of_values = smaller_df.iloc[[row_index]].values.tolist()[0]
        class_label_for_current_row = row_of_values[0]
        data_for_current_row = row_of_values[1:]

        nearest_neighbor_distance = np.inf
        nearest_neighbor_location = np.inf

        for sub_row_index in range(len(smaller_df)): # iterate through each row in data for finding the nearest neighbor
            if sub_row_index != row_index:
                v1 = np.array(data_for_current_row)
                v2 = np.array(smaller_df.iloc[[sub_row_index]].values.tolist()[0][1:])
                distance = np.sqrt(np.sum((v1 - v2)**2)) # calculate the Euclidean distance
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = sub_row_index
                    nearest_neighbor_label = smaller_df.iloc[nearest_neighbor_location]["Feature"] # extract class label for the nearest neighbor
        if class_label_for_current_row == nearest_neighbor_label:
            number_correctly_classfied += 1 # if predicted label is same as actual label, increment count
    accuracy = number_correctly_classfied / (len(smaller_df)) # calculate the accuracy
    return accuracy

df = large_dataset_as_df()
# df = small_dataset_as_df()
print(testCode(df,[1,15,27]))


