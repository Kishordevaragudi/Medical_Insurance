from Insurance.logger import log
from Insurance.exception import InsuranceException
import os,sys
from Insurance.utils import get_collection_as_dataframe

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
     get_collection_as_dataframe(database_name = "INSURANCE",collection_name ="INSURANCE_PROJECT")
        
    except Exception as e:
        print(e)