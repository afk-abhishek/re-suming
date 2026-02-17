from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TFIDFMatcher:

    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")

    def match(self, resumes, job_desc):

        docs = resumes + [job_desc]

        tfidf = self.vectorizer.fit_transform(docs)

        resume_vecs = tfidf[:-1]
        jd_vec = tfidf[-1]

        scores = cosine_similarity(resume_vecs, jd_vec)

        return scores.flatten()
