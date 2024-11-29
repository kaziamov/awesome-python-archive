import os


def fixtures_path(path: str):
    return os.path.join(os.path.dirname(__file__), 'fixtures/', path)
