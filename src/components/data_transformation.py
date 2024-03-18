import sys
import os
from dataclasses import dataclass   # used for simplifying the class creation for data storage

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer   # for applying transformations to columns
from sklearn.impute import SimpleImputer        # for handling missing values
from sklearn.pipeline import Pipeline           # for creating data processing pipelines
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# imports from "custom modules"
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    """
    Stores configuration for data transformation
    """

    # path to save preprocessing object...
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        """
        This function is responsible for DEFINING data transformation
        """
        try:
            # defining numerical columnns
            numerical_columns = ['writing_score', 'reading_score']
            # defining categorical columns
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            # initializing pipeline for "numerical_columns"
            numerical_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )
            # initializing pipeline for "catgorical_columns"
            categorical_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )

            # Showing the status using logging
            logging.info(f"Numerical Columns: {numerical_columns}")
            logging.info(f"Categorical Columns: {categorical_columns}")

            # Apply pipelines created above to Columns using ColumnTransformer class
            preprocessor = ColumnTransformer(
                [
                    # apply "numerical_pipeline" created above to "numerical_columns"
                    ("numerical_pipeline", numerical_pipeline, numerical_columns),

                    # apply "categorical pipeline" created above to "categorical columns"
                    ("categorical_pipeline", categorical_pipeline, categorical_columns)
                ]
            )

            logging.info("Column Transformations applied !")

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        """
        This function is responsible for APPLYING Data Transformations
        [ Performing data transformation on our data(train/test) ]
        """
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Reading train and test data, completed")

            logging.info("Obtaining preprocessing object")
            preprocessing_obj = self.get_data_transformer_object()
            
            target_column_name = "math_score"
            numerical_columns = ["writting_score", "reading_score"]

            # creating X and y (that is independent and dependent features)
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe.")

            # performing fit_transform on train data (for training) and just transform on test data (because can't train)
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            # "np.c_" -> performs "Column Wise Concatenation"
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved Preprocessing Object.")

            save_object (
                file_path = self.data_transformation_config.preprocessor_obj_file_path, # "preprocessor.pkl" file will be passed over here
                obj = preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e, sys)