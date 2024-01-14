# filehandler class to read/write transaction files
import csv

class FileHandler:
    def __init__(self, filename: str, headers: str = ['date', 'tr_name', 'debit', 'credit', 'card_number'], output_file: str = "data/processed_data.csv"):
        self.__file = filename
        self.__headers = headers
        self.__processed_data = None #contains processed data
        self.__output_file = output_file


    def read_csv(self) -> None:
        #read the file
        with open(self.__file, 'r') as file:
            csv_reader = csv.DictReader(file, fieldnames = self.__headers)
            self.__processed_data = list(csv_reader)

    def get_data(self) -> dict:
        #return processed data
        return self.__processed_data

    def write_csv(self, data: dict, header: list) -> None:
        #use dictwriter to write to output file
        with open(self.__output_file, 'w', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=header)

            # Write the header
            csv_writer.writeheader()

            # Write the data
            csv_writer.writerows(data)
