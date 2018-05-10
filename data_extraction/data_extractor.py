import csv
import pandas
import json


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

        column_index['input']['pre-tax amount'] = {'column_index': 0}
        column_index['input']['tax amount'] = {'column_index': 1}

        index = 2

        for i in range(len(unique_expense_desc)):
            column_index['input'][unique_expense_desc[i]] = {'column_index': i + index}

        index += len(unique_expense_desc)

        for i in range(len(unique_tax_name)):
            column_index['input'][unique_tax_name[i]] = {'column_index': i + index}

        for i in range(len(unique_categories)):
            column_index['output'][unique_categories[i]] = {'value': i}

        Parser.__save_column_index(column_index)

    @staticmethod
    def __save_column_index(json_file):
        with open('../data/column_index.txt', 'w') as outfile:
            json.dump(json_file, outfile)

Parser.parse_csv_data(Parser.training_data_file)
