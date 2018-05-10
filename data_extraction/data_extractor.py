import csv
import pandas
import json
import numpy


class Parser:
    training_data_file = "../data/training_data_example.csv"
    validation_data_file = "../data/validation_data_example.csv"
    employee_file = "../data/employee.csv"

    def __init__(self):
        pass

    @staticmethod
    def parse_csv_data(input_file):
        data_list = []  # list of lists
        header_list = []  # list containing just the header row
        with open(input_file, "r") as csv_file:
            parsed_data = csv.reader(csv_file, delimiter=",")
            i = 0
            for row in parsed_data:
                if i == 0:
                    header_list = row
                else:
                    data_list.append(row)
                i = i + 1
        return Parser.__pre_process_data(data_list, header_list)

    @staticmethod
    def __pre_process_data(data_list, header_list):
        """
        ['date', 'category', 'employee id', 'expense description', 'pre-tax amount', 'tax name', 'tax amount']
        :param data_list:
        :return:
        """
        table = pandas.DataFrame(data_list, columns=header_list)
        table.drop(['date', 'employee id'], axis=1, inplace=True)
        unique_categories = table['category'].unique()
        unique_expense_desc = table['expense description'].unique()
        unique_tax_name = table['tax name'].unique()

        column_index = {
            'input': {},
            'output': {}
        }

        column_index['input']['pre-tax amount'] = {
            'column_index': 0,
            'type': 'int'
        }

        column_index['input']['tax amount'] = {
            'column_index': 1,
            'type': 'int'
        }

        index = 2

        for i in range(len(unique_expense_desc)):
            column_index['input'][unique_expense_desc[i]] = {
                'column_index': i + index,
                'type': 'str'
            }

        index += len(unique_expense_desc)

        for i in range(len(unique_tax_name)):
            column_index['input'][unique_tax_name[i]] = {
                'column_index': i + index,
                'type': 'str'
            }

        for i in range(len(unique_categories)):
            column_index['output'][unique_categories[i]] = {'value': i}

        Parser.__save_column_index(column_index)
        return Parser.__post_process_data(data_list)

    @staticmethod
    def __post_process_data(data_list):
        json_data = Parser.__read_column_index()
        Y = [data[1] for data in data_list]
        data_list = [d[3:] for d in data_list]
        X = []

        for i in range(len(data_list)):
            x = numpy.zeros(len(json_data['input']))
            x[json_data['input']['pre-tax amount']['column_index']] = data_list[i][3]
            x[json_data['input']['tax amount']['column_index']] = data_list[i][3]

            for j in range(len(data_list[i])):
                try:
                    float(data_list[i][j])
                except ValueError:
                    x[json_data['input'][data_list[i][j]]['column_index']] = 1
            X.append(x)
        return X, Y

    @staticmethod
    def __save_column_index(json_file):
        with open('../data/column_index.json', 'w') as outfile:
            json.dump(json_file, outfile)

    @staticmethod
    def __read_column_index():
        with open('../data/column_index.json') as f:
            data = json.load(f)
        return data

