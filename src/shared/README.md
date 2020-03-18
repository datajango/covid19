# shared code 

## index_reader.py

Loads the file all_sources_metadata_2020-03-13.csv into a in-memory data structure.

The file all_sources_metadata_2020-03-13.csv is located at path : 
CORD-19-research-challenge\2020-03-13\all_sources_metadata_2020-03-13.csv

1. Metadata for papers from these sources are combined: CZI, PMC, BioRxiv/MedRxiv. (total records 29500)
    - CZI 1236 records
    - PMC 27337
    - bioRxiv 566
    - medRxiv 361
1. 17K of the paper records have PDFs and the hash of the PDFs are in 'sha'
1. For PMC sourced papers, one paper's metadata can be associated with one or more PDFs/shas under that paper - a PDF/sha correponding to the main article, and possibly additional PDF/shas corresponding to supporting materials for the article.
1. 13K of the PDFs were processed with fulltext ('has_full_text'=True)
1. Various 'keys' are populated with the metadata:
    - 'pmcid': populated for all PMC paper records (27337 non null)
    - 'doi': populated for all BioRxiv/MedRxiv paper records and most of the other records (26357 non null)
    - 'WHO #Covidence': populated for all CZI records and none of the other records (1236 non null)
    - 'pubmed_id': populated for some of the records
    - 'Microsoft Academic Paper ID': populated for some of the records

The columns are: 

1. sha :  hash of the file
1. source_x
1. title
1. doi : populated for all BioRxiv/MedRxiv paper records and most of the other records (26357 non null)
1. pmcid :  populated for all PMC paper records (27337 non null)
1. pubmed_id
1. license
1. abstract
1. publish_time
1. authors
1. journal
1. Microsoft Academic Paper ID : populated for some of the records
1. WHO #Covidence : populated for all CZI records and none of the other records (1236 non null)
1. has_full_text

