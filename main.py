from parser.file_parser import load_resumes, load_job
from sklearn_model.TFIDF_matcher import TFIDFMatcher


resumes = load_resumes("data/resumes")
job_desc = load_job("data/jobs")

matcher = TFIDFMatcher()

scores = matcher.match(resumes, job_desc)

for i, s in enumerate(scores):
    print(f"Resume {i+1} Score: {round(s*100,2)}%")
