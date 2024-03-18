import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


# if we're just defining variables, then use "dataclass" else use the traditional way of initializing "__init__" method inside class.

@dataclass
class DataIngestionConfig:

    # data_ingestion.py component will save all the files/output in artifacts folder path.
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
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

            logging.info("Train Test Split Initiated")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test set data
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