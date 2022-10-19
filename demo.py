# import logging
from distutils.command.config import config
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuartion
from housing.component.data_transformation import DataTransformation
from housing.util.util import read_yaml_file

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # data_transformation_config = Configuartion().get_data_transformation_config()
        # print(data_transformation_config)
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__=="__main__":
    main()