# word_counter.py
""" generate word counts for all abstracts """

import shared

def main():
    filename = "../data/2020-03-13/all_sources_metadata_2020-03-13.csv"
    columns, rows = shared.read_csv(filename)
    print("There are {} columns.".format(len(columns)))
    print("There are {} rows.".format(len(rows)))

    for row_number, row in enumerate(rows):
        if len(row) == 14:
            (sha, source_x, title, doi, pmcid, pubmed_id, license, abstract, publish_time, authors, journal, microsoft_id, who_number_covidence, has_full_text) = row
            print("{} source_x={} title={} doi={} pmcid={} pubmed_id={}".format(row_number, source_x, title, doi, pmcid, pubmed_id, len(abstract)))
        else: 
            print("row {} is not 14 columns in length".format(row_number))
        
        #print("{1} {2}".format(row_number, sha))

        # The all_sources_metadata_2020-03-13.csv is incomplete

if __name__ == "__main__":
    # execute only if run as a script
    main()