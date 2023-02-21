# batch prediction
# traning prediction
from Insurance.pipeline.training_pipeline import start_training_pipeline
from Insurance.pipeline.batch_prediction import start_batch_prediction

#file_path = (r"/config/workspace/insurance.csv")

if __name__ =="__main__":
    try:
        #output =  start_batch_prediction(input_file_path=file_path)
        output =  start_training_pipeline()
        print(output)
    except Exception as e:
        print(e)
