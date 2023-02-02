from Insurance.logger import log
from Insurance.exception import InsuranceException
import os,sys
from Insurance.utils import get_collection_as_dataframe
from Insurance.entity.config_entity import DataIngestionConfig
from Insurance.entity import config_entity
from Insurance.components.data_ingestion import DataIngestion
from Insurance.components.data_validation import DataValidation
from Insurance.components.data_transformation import DataTransformation




if __name__ == "__main__":
    try:

        traning_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(traning_pipeline_config = traning_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config = data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        # Data Validation 
        data_validation_config = config_entity.DataValidationConfig(traning_pipeline_config = traning_pipeline_config)
        data_validation = DataValidation(data_validation_config = data_validation_config,
                                         data_ingestion_artifact = data_ingestion_artifact)

        data_validation_artifact = data_validation.initaite_data_validation()

        # Data Transformation
        data_transformation_config = config_entity.DataTransformationConfig(traning_pipeline_config = traning_pipeline_config)
        data_transformation = DataTransformation(data_transformation_config = data_transformation_config, 
        data_ingestion_artifact= data_ingestion_artifact)
        data_transformation_artifact = data_transformation.initaite_data_transformation()
        
    except Exception as e:
        print(e)