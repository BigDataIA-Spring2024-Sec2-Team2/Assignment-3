csv_to_model_map = {
    'NameOfTheTopic': 'topic',
    'Year': 'year',
    'Level': 'level',
    'IntroductionSummary': 'introductionSummary',
    'LearningOutcomes': 'learningOutcomes',
    'Summary': 'summary',
    'SummaryPageLink': 'summaryPageLink',
    'PDFFileLink': 'pdfFileLink'
}

model_to_csv_map = {
  'topic': 'NameOfTheTopic', 
  'year': 'Year', 
  'level': 'Level', 
  'introductionSummary': 'IntroductionSummary', 
  'learningOutcomes': 'LearningOutcomes', 
  'summary': 'Summary', 
  'summaryPageLink': 'SummaryPageLink', 
  'pdfFileLink': 'PDFFileLink'
}

def convertRomanToInt(s):
  map = {'I':1, 'II': 2, 'III':3}
  return map[s]