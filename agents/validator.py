from utils.loader import load_spec, load_data


def create_prompt(spec_path):

    spec = load_spec(spec_path)

    prompt = spec["prompt"]

    data_path = spec["data_source"]["path"]

    file_data = load_data(data_path)

    system_prompt = f"""
You are a Data Quality AI agent.

Task:
{spec["task"]}

User Request:
{prompt}

Input Dataset:
{file_data}

Please analyze the dataset and provide:
1. Columns with NULL values
2. Duplicate rows
3. Any data quality issues
"""

    return system_prompt