from pydantic import BaseModel, Field, field_validator
import re
import pandas as pd
from utils.string_validation_util import validate_string_spaces, Validate_string_line_space_char

df = pd.read_csv("data/cfa-data.csv", sep="\t")


class CFADataModel(BaseModel):
  topic: str
  year: int = Field(default = None)
  level: int
  introductionSummary: str = Field(default = None)
  learningOutcomes: str = Field(default = None)
  summary: str = Field(default = None)
  summaryPageLink: str = Field(pattern=r'^https:\/\/www\.cfainstitute\.org\/.*')
  pdfFileLink: str = Field(default = None, pattern=r'^https://www\.cfainstitute\.org/-/media/documents/protected/.*\.pdf$')

  @field_validator("topic")
  @classmethod
  def topic_validator(cls, v):
    if v:
      if not validate_string_spaces(v):
        raise ValueError('Unwanted spaces in the string')
      return v.title()

  @field_validator("year")
  @classmethod
  def year_validator(cls, v):
    if v:
      reg_pattern=r'^20\d{2}$'
      if not re.match(reg_pattern, str(v)):
        raise ValueError('Year not in range')
      return v
    
  @field_validator("level")
  @classmethod
  def level_validator(cls, v):
    if v:
      reg_pattern=r'\d{1,2}'
      if not re.match(reg_pattern, str(v)):
        raise ValueError('Level not in range')
      return v

  @field_validator("introductionSummary", "learningOutcomes", "summary", mode="before")
  @classmethod
  def introduction_validator(cls, v):
    if v:
      if not validate_string_spaces(v):
        raise ValueError('Unwanted spaces in the string')
      if not Validate_string_line_space_char(v):
        raise 
      return v

