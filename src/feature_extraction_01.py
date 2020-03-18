# feature_extraction_01.py

import shared

def main():
    filename = "../data/2020-03-13/all_sources_metadata_2020-03-13.csv"
    columns, rows = shared.read_csv(filename)
    print("There are {} columns.".format(len(columns)))
    print("There are {} rows.".format(len(rows)))

if __name__ == "__main__":
    # execute only if run as a script
    main()