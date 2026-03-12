import yaml

def load_spec(path):
    with open(path, "r") as f:
        spec = yaml.safe_load(f)
    return spec


def load_data(path):
    with open(path, "r") as f:
        file_data = f.read()
    return file_data