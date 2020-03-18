# load_every_json_file.py
""" Trys to load every JSON file and extract data to create a new master publication index. """

import shared
import os
import json

def open_json_file(root, name):    
    data = None
    filename = os.path.join(root, name)
    try:
        with open(filename, encoding='utf-8') as json_file:
            data = json.load(json_file)
    except Exception as exp:
        print(exp)

    return data

def extract_data(root, name, raw):
    filename = os.path.join(root, name)
    paper_id = raw['paper_id']
    metadata = raw['metadata']
    title = metadata['title']
    abstracts = raw['abstract']
    
    has_abstract = False
    has_full_text = False

    #if len(abstracts)>1:
    #    print('more than one abstract for {}'.format(filename))

    #if len(abstracts)==0:
    #    print('no abstract for {}'.format(filename))

    abstract_sections = []

    for abstract in abstracts:
        abstract_sections.append(abstract['text'])
        cite_spans = abstract['cite_spans']
        ref_span = abstract['ref_spans']
        section = abstract['section']

    if len(abstract_sections)>0:
        has_abstract = True
    #print("# of abstract sections {}".format(len(abstract_sections)))

    body_text = raw['abstract']
    body_text_sections = []

    for body_text_section in body_text:
        body_text_sections.append(body_text_section['text'])

    if len(body_text_sections)>0:
        has_full_text = True
    #print("# of body text sections {}".format(len(body_text_sections)))

    if not has_abstract and not has_full_text:
        print("{} has no abstract and has no full text".format(name))
    elif has_abstract and not has_full_text:
        print("{} has an abstract and has no full text".format(name))
    elif not has_abstract and has_full_text:
        print("{} has no abstract and has full text".format(name))
    elif has_abstract and has_full_text:
        print("{} has an abstract and has full text".format(name))

    #print(paper_id)
    #print(title)


def main():
    data_folder = os.path.abspath("../data/2020-03-13")
    for root, dirs, files in os.walk(data_folder, topdown=False):
        for name in files:
            if name[-4:]=="json":
                #print(os.path.join(root, name))
                raw = open_json_file(root, name)
                data = extract_data(root, name, raw)

        #for name in dirs:
        #    print(os.path.join(root, name))


if __name__ == "__main__":
    # execute only if run as a script
    main()