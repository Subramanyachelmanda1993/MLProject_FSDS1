# import logging
from distutils.command.config import config
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuartion
from housing.component.data_transformation import DataTransformation
from housing.util.util import read_yaml_file
import os

def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        # pipeline.run_pipeline()
        # data_transformation_config = Configuartion().get_data_transformation_config()
        # print(data_transformation_config)
        pipeline.start()
        logging.info("main function execution completed.")
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__=="__main__":
    main()