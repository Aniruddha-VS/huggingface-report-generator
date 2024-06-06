from huggingface_hub import HfApi
import pandas as pd

pd.set_option('display.max_columns', None)

def format_number(num):
    output = ""
    suffixes = ['', 'K', 'M', 'B', 'T']

    for suffix in suffixes:
        if num < 1000:
            output = f'{num:.2f} {suffix}'
            break
        num /= 1000

    return output

def generate_report():

    api = HfApi()

    most_downloaded_models = pd.DataFrame(list(api.list_models(sort='downloads', direction=-1, limit=10)))

    most_downloaded_models['downloads'] = most_downloaded_models['downloads'].apply(format_number)

    print('\n',most_downloaded_models[['id', 'downloads', 'pipeline_tag']].to_string(index=False), '\n')

if __name__ == "__main__":
    generate_report()
    exit(0)