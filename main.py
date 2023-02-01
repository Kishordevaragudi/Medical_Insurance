from Insurance.logger import log
from Insurance.exception import InsuranceException
import os,sys

def test_logger_and_expection():
    try:
        log.info("Starting the test_logger_and_expection")
        result=3/0
        print(result)
        log.info("Ending point of test_logger_and_expection")
    except Exception as e:
        log.debug(str(e))
        raise InsuranceException(e, sys)

if __name__ == "__main__":
    try:
        test_logger_and_expection()
    except Exception as e:
        print(e)