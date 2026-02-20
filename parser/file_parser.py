import os


def parse_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().lower()


def load_resumes(folder):
    resumes = []

    for f in os.listdir(folder):
        if f.endswith(".txt"):
            path = os.path.join(folder, f)
            resumes.append(parse_txt(path))

    return resumes


def load_job(folder):
    files = os.listdir(folder)

    if not files:
        raise Exception("No job file found")

    path = os.path.join(folder, files[0])

    return parse_txt(path)
