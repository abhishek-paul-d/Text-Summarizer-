from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.data_ingeston_pipeline import DataIngestionPipeline

logger.info("Logging is implemented")

STAGE_NAME = "Data Ingestion Stage"

try: 
    logger.info(f"stage {STAGE_NAME} started")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    raise e