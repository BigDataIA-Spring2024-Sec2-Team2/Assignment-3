from unittest import TestCase
from parameterized import parameterized

from models.cfa_data_model import CFADataModel

# dummy data
data = {
      'topic' : "test topic 1",
      'year' : "2021",
      'level' : "2",
      'introductionSummary' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
      'learningOutcomes' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
      'summary' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
      'summaryPageLink' : "https://www.cfainstitute.org/membership/professional-development/refresher-readings/test-reading-path-1",
      'pdfFileLink' : "https://www.cfainstitute.org/-/media/documents/protected/refresher-reading/2024/level2/level2a/RR_2024_L2V1R5-1.pdf",
    }

data_no_topic = {key: value for key, value in data.items() if key != "topic"}
data_no_year = {key: value for key, value in data.items() if key != "year"}
data_no_level = {key: value for key, value in data.items() if key != "level"}
data_no_intro = {key: value for key, value in data.items() if key != "introductionSummary"}
data_no_outcome = {key: value for key, value in data.items() if key != "learningOutcomes"}
data_no_summary = {key: value for key, value in data.items() if key != "summary"}
data_no_summarylink = {key: value for key, value in data.items() if key != "summaryPageLink"}
data_no_pdfFileLink = {key: value for key, value in data.items() if key != "pdfFileLink"}

class CFADataModelTestClass(TestCase):
  def setUp(self):
    ''' initialize data '''
    # all values populated
    self.data = data.copy()

  @parameterized.expand([
    (data,),
    (data_no_year,),
    (data_no_intro,),
    (data_no_outcome,),
    (data_no_summary,),
    (data_no_pdfFileLink,),
  ])
  def test_model_creation_correct_data(self, data):
    ''' test model creation with correct data (some optional fields missing) '''
    validate_res = CFADataModel.model_validate(data)
    self.assertIsNotNone(validate_res)

  @parameterized.expand([
    (data_no_topic,),
    (data_no_level,),
    (data_no_summarylink,),
  ])
  def test_model_creation_incorrect_data(self, data):
    ''' test model creation with missing mandatory data '''
    with self.assertRaises(ValueError):
      CFADataModel.model_validate(data, strict=True)

  def test_model_creation_incorrect_level_data(self):
    ''' test model creation with incorrect level data '''
    self.data["level"] = "II"
    with self.assertRaises(ValueError) as err:
      CFADataModel.model_validate(self.data)
    self.assertIn("level", str(err.exception))