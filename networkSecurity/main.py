from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        logging.info("Starting data ingestion")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed successfully")
        print(data_ingestion_artifact)
    except Exception as e:
        raise CustomException(e,sys)