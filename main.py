from text_Summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from  text_Summarizer.logging import logger

STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>stage {STAGE_NAME} started<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>stage {STAGE_NAME} complete<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e 