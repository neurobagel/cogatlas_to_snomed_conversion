import csv
import json

def read_tsv_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        column_names = next(reader)
        first_row = next(reader)
    return column_names, first_row

def read_json_keys(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data.keys()

def main():
    tsv_file_path = 'assessments.tsv'
    json_file_path = 'data_dictionary.json'

    tsv_column_names, first_row = read_tsv_data(tsv_file_path)
    json_keys = read_json_keys(json_file_path)

    missing_columns_with_values = [(col, first_row[i]) for i, col in enumerate(tsv_column_names) if col not in json_keys]

    for column, value in missing_columns_with_values:
        print(f'("{column}", "{value}")')

if __name__ == "__main__":
    main()