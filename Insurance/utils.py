import pandas as pd 
import numpy as np
import os
import sys
from Insurance.exception import InsuranceException
from Insurance.config import mongo_client
from Insurance.logger import log
import yaml
import dill


def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    try:
        log.info(f"Reading data from database:{database_name} and collection:{collection_name}")
        df = pd.DataFrame(mongo_client[database_name][collection_name].find())
        log.info(f"Find columns:{df.columns}")
        if "_id" in df.columns:
            log.info(f"Dropping columns:_id")
            df = df.drop("_id",axis=1)
        log.info(f"Rows and columns in df:{df.shape}")
        return df    
    except Exception as e:
        raise InsuranceException(e, sys)