# Data transformation : This component is responsible for transforming the data into a format that can be used by the machine learning model. This may include scaling, encoding, and feature engineering.
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object
@dataclass
class DataTransformationConfig:
    preproccessor_ob_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation'''
        try:
            numerical_columns = ['reading_score', 'writing_score']
            categorical_columns  = ['gender','race_ethnicity','parental_level_of_education','lunch','test_preparation_course']
            num_pipeline = Pipeline(
                steps =[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                steps = [
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder',OneHotEncoder()),
                    ('scaler',StandardScaler(with_mean=False))
                ]
            )
            logging.info("Categorical and numerical pipeline is created")
            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline',num_pipeline,numerical_columns),
                    ('cat_pipeline',cat_pipeline,categorical_columns)
                ]
            )
            return preprocessor
        except Exception as e: 
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")
            logging.info("Obtaining preproccessor object")
            preprocessor = self.get_data_transformer_object()
            target_column_name = 'math_score'
            numerical_columns = ['reading_score', 'writing_score']
            input_feature_train_df = train_df.drop(columns=[target_column_name])
            target_feature_train_df = train_df[target_column_name]
            input_feature_test_df = test_df.drop(columns=[target_column_name])
            target_feature_test_df = test_df[target_column_name]    
            logging.info("Applying preprocessor object on training and testing dataframe")
            input_feature_train_arr = preprocessor.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor.transform(input_feature_test_df)
            #np.c_ is used to combine multiple arrays column-wise to form a single dataset, especially useful in preprocessing and feature engineering
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            # return a,b and return (a,b) are different, in the first case we are returning two separate values and in the second case we are returning a tuple
            save_object(
                file_path = self.data_transformation_config.preproccessor_ob_file_path,
                obj = preprocessor
            )
            return train_arr, test_arr, self.data_transformation_config.preproccessor_ob_file_path
        except Exception as e: 
            raise CustomException(e,sys)