import os   # for interacting with os (for ex. creating directories)
import sys  # for accessing system-specific parameters (used for error handling)

import pandas as pd
from sklearn.model_selection import train_test_split

# imports from "custom modules"
from src.exception import CustomException   # a CustomException class for handling errors.
from src.logger import logging              # a logging system for recording events.
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer

from dataclasses import dataclass   # simplifying class creation for data storage


# if we're just defining variables, then use "dataclass" else use the traditional way of initializing "__init__" method inside class.

@dataclass
class DataIngestionConfig:
    """
    Stores file path for data storage.

    Attributes:
        - train_data_path: Path for saving training data.
        - test_data_path: Path for saving test data.
        - raw_data_path: Path for saving raw(unprocessed or unsplitted) data.
    """

    # "data_ingestion.py" component will save all the files/output in artifacts folder path.
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    """
    Handles Data Ingestion Process
    """

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Read data from csv: Here we can read from csv / mongodB anywhere
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the Dataset as DataFrame')

            # Creating directory structure that leads to train_data_path
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
        
            # Save entire DataFrame(df) to "raw_data_path" using "to_csv"
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Now will perform train-test-split
            logging.info("Initiating Train and Test Split")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Similar to raw_data, Save train and test data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))