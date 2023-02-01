from Insurance.logger import log
from Insurance.exception import InsuranceException
import os,sys
from Insurance.utils import get_collection_as_dataframe
from Insurance.entity.config_entity import DataIngestionConfig
from Insurance.entity import config_entity

#def test_logger_and_expection():
    #try:
       # log.info("Starting the test_logger_and_expection")
       # result=3/0
       # print(result)
       # log.info("Ending point of test_logger_and_expection")
    #except Exception as e:
    #    log.debug(str(e))
    #    raise InsuranceException(e, sys)

if __name__ == "__main__":
    try:
        #start_training_pipeline()
        #test_logger_and_expection()
     #get_collection_as_dataframe(database_name = "INSURANCE",collection_name ="INSURANCE_PROJECT")
        traning_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(traning_pipeline_config = traning_pipeline_config)
        print(data_ingestion_config.to_dict())
        
    except Exception as e:
        print(e)