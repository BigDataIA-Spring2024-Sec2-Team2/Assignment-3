import pandas as pd
import numpy as np
from models.cfa_data_model import CFADataModel
from scripts.custom_logger import customLogger
from utils.data_cleaner_util import convertRomanToInt, csv_to_model_map, model_to_csv_map
import re
import os
import logging


logger = customLogger('web-scrapping-validation.log')
if "PYTEST_CURRENT_TEST" in os.environ:
  logger = logging  


def validate_function(model, max_attempts=3, **kwargs):
  ''' function to validate the raw data, and then try to fix the data if any validation is hit '''
  attempts = 0
  logger.info("Validating {} --------------".format(kwargs["topic"]))
  while attempts < max_attempts:
    try:
      m = model(**kwargs)
      logger.info("Succesfully validated {}".format(kwargs["topic"]))
      return m.model_dump()
    except Exception as e:
      for error in e.errors():
        field_name = error['loc'][0]
        msg = error["msg"]
        logger.info("Attempting to fix the error {}".format(field_name))
        if field_name == "topic":
          if "Test RR page" in msg:
            break
          kwargs["topic"] = kwargs["topic"].strip()
        elif field_name == "level":
          kwargs["level"] = convertRomanToInt(kwargs["level"])
        elif field_name in ["introductionSummary", "learningOutcomes", "summary"]:
          temp = kwargs[field_name].strip(" ")
          temp_list = [s.strip() for s in temp.split("\n")]
          temp = ' '.join(temp_list)
          temp = re.sub(r'\s+', ' ', temp)
          kwargs[field_name] = temp
        elif field_name == "pdfFileLink":
          kwargs["pdfFileLink"] = None
      attempts += 1
      logger.info("Retrying running model...")
  logger.error("could not fix csv entry for {}".format(kwargs['topic']))


def cleanDataWebScrape():
  ''' function to pass values to validator '''
  logger.info("------- Starting validating dataframe data -------")
  df = pd.read_csv("data/raw-data/cfa-data.csv", sep="\t")
  df = df.replace(np.nan, None)
  result_list = []
  for _, row in df.iterrows():
    topic_data = {}
    for column, field in csv_to_model_map.items():
      if column in row:
        topic_data[field] = row[column]
    res = validate_function(CFADataModel, max_attempts=2, **topic_data)
    if res:
      result_list.append(res)

  df_clean = pd.DataFrame(result_list)
  logger.info("------- Ending validating dataframe data -------")
  return df_clean


def convertDFtoCSV(df):
  ''' function to store DF locally '''
  logger.info("-------Starting Writing to CSV -------")
  csv_location = "data/clean-data/cfa-data-clean.csv"
  df.to_csv(csv_location, index=False,sep="\t")
  logger.info("------- Ending Writing to CSV -------")
  
if __name__ == '__main__': 
  df = cleanDataWebScrape()
  convertDFtoCSV(df)