from sklearn_model.TFIDF_matcher import TFIDFMatcher


resumes = [
    "Python developer with ML and AWS experience",
    "Web developer skilled in React and Node",
    "Data scientist with PyTorch and NLP background"
]

job_desc = "Looking for ML engineer with Python and PyTorch"

matcher = TFIDFMatcher()

scores = matcher.match(resumes, job_desc)

for i, s in enumerate(scores):
    print(f"Resume {i+1} Score: {round(s*100,2)}%")
