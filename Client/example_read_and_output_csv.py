import csv
import os


def read_and_save_csv(input_file_path, output_file_path):
    if not os.path.exists(input_file_path):
        print(f"File '{input_file_path}' does not exist.")
        return

    data = []
    with open(input_file_path, mode="r") as input_file:
        csv_reader = csv.reader(input_file)
        header = next(csv_reader)
        data.append(header)
        for row in csv_reader:
            data.append(row)

    with open(output_file_path, mode="w", newline="") as output_file:
        csv_writer = csv.writer(output_file)
        for row in data:
            csv_writer.writerow(row)

    print(f"Data has been successfully saved to '{output_file_path}'")


if __name__ == "__main__":
    # Relative path to the input CSV file
    input_relative_path = os.path.join("../", "Data", "sample_data.csv")
    # Relative path to the output CSV file
    output_relative_path = os.path.join("../", "Output", "new_sample_data.csv")

    read_and_save_csv(input_relative_path, output_relative_path)
