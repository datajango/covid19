# index_reader.py
# load all_sources_metadata_2020-03-13.csv

import csv

def read_header(filename):
    columns = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        columns = next(csv_reader)  # gets the first line

    return columns

def read_csv(filename):
    columns = []
    rows = []
    
    with open(filename, "r", encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        columns = next(csv_reader)  # gets the first line
        for row in csv_reader:
            rows.append(row)

    return columns, rows

def main():
    filename = "../data/2020-03-13/all_sources_metadata_2020-03-13.csv"
    #columns = read_header(filename)
    #for position, column in enumerate(columns):
    #    print("{0} {1}".format(position+1, column))

    columns, rows = read_csv(filename)

    print("There are {} columns.".format(len(columns)))
    print("There are {} rows.".format(len(rows)))

if __name__ == "__main__":
    # execute only if run as a script
    main()