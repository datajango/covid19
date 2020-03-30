# Covid 19 Kaggle Competition

## Starting Jypter Noptbook

1. Start Conda Env

    ```sh
    conda activate py37covid19 
    conda install jupyter
    jupyter-notebook
    ```


## Getting Started

1. Copy the Covid-19 Reseach data to the data folder as folder 2020-03-13

1. Create the Anaconda Env, see Conda Setup

1. Run a program that reads the metadata index of all papers.

    ```sh
    conda activate py37covid19 
    cd src
    python index_reader.py
    ```
    You should see the following output:
    ```
    There are 14 columns.
    There are 29500 rows.
    ```

1. Run a program that reads the actual JSON files of every publication.

    ```sh
    conda activate py37covid19 
    cd src
    python load_every_json_file.py
    ```
    You should see output for 29500 publication that reports on the abstract and the full text:
    ```
    deaac80fa1b6ee6b493932b297496c8751c9ef1b.json has an abstract and has full text
    dec1d801c2d5a971207df424ede4b1d65267b212.json has an abstract and has full text
    dec25863e871c025ecfd92611e727196ae88cb5b.json has an abstract and has full text
    deda9e69d8455166370e8bd96c2bdb630c4b97b0.json has an abstract and has full text
    dedf310e36616461c82de98d9b0ceae75c30e5cd.json has an abstract and has full text
    dedff395d93d8023667fc500d7c7c8451d581451.json has an abstract and has full text
    deeacb8558e3403c69cd8db9f4e8e5214fd85c46.json has an abstract and has full text
    deedf1e06ab3cae049c5326cab4e4a2771f54233.json has no abstract and has no full text
    def1cf77e1ef84f4373a342e23145be05ec5e226.json has an abstract and has full text
    def339c1e20c36c30ae665e0a4573ed30be45df7.json has an abstract and has full text
    df0310a74d62210e31be9fbe879085499825b14d.json has an abstract and has full text
    df1017e24101a51f6b5ca30ae2cb8376d8756a61.json has an abstract and has full text
    ```

## Data

- CORD-19-research-challenge

## Conda Setup

1. To update conda run

    ```sh
    conda update -n base -c defaults conda
    ```

1. List current Anaconda environmets.

    ```sh
    conda env list
    ```

1. Create a Anaconda Environment

    ```sh
    conda create --name py37covid19 python=3.7
    ```

1. Activate the Anaconda Environment

    ```sh
    conda activate py37covid19
    ```

1. Install PIP requirements into the "Covid-19 Research" Python 3.7 Anaconda Environment

    ```sh
    pip install -r requirements.txt
    ```

1. Create a requirements.txt to hold the pip package list

    ```sh
    conda list -e > requirements.txt
    ```


## Tasks

1. [What is known about transmission, incubation, and environmental stability? What do we know about natural history, transmission, and diagnostics for the virus? What have we learned about infection prevention and control?](./docs/Task01.md)
1. [What do we know about COVID-19 risk factors? What have we learned from epidemiological studies?](./docs/Task02.md)
1. [What do we know about virus genetics, origin, and evolution? What do we know about the virus origin and management measures at the human-animal interface?](./docs/Task03.md)
1. [At the time of writing, COVID-19 has spread to at least 114 countries. With viral flu, there are often geographic variations in how the disease will spread and if there are different variations of the virus in different areas. We’d like to explore what the literature and data say about this through this Task.](./docs/Task04.md)
1. [What do we know about the effectiveness of non-pharmaceutical interventions? What is known about equity and barriers to compliance for non-pharmaceutical interventions?](./docs/Task05.md)
1. [What do we know about vaccines and therapeutics? What has been published concerning research and development and evaluation efforts of vaccines and therapeutics?](./docs/Task06.md)
1. [What has been published concerning ethical considerations for research? What has been published concerning social sciences at the outbreak response?](./docs/Task07.md)
1. [What do we know about diagnostics and surveillance? What has been published concerning systematic, holistic approach to diagnostics (from the public health surveillance perspective to being able to predict clinical outcomes)?](./docs/Task08.md)
1. [What has been published about medical care? What has been published concerning surge capacity and nursing homes? What has been published concerning efforts to inform allocation of scarce resources? What do we know about personal protective equipment? What has been published concerning alternative methods to advise on disease management? What has been published concerning processes of care? What do we know about the clinical characterization and management of the virus?](./docs/Task09.md)
1. [What has been published about information sharing and inter-sectoral collaboration? What has been published about data standards and nomenclature? What has been published about governmental public health? What do we know about risk communication? What has been published about communicating with high-risk populations? What has been published to clarify community measures? What has been published about equity considerations and problems of inequity?](./docs/Task10.md)


## Topics of Language Technology

1. Spam Detection
1. Part of speech (POS) tagging
1. Named entity recongnition (NER)
1. Sentiment analysis
1. Coreference resolution
1. Word sense disambiguation (WSD)
1. Parsing
1. Machine translation (MT)
1. Information extraction (IE)
1. Question Answering
1. Paraphrase
1. Summarization
1. Dialog

## Question Answering

Answer Types and Query Formulation

### Answer Type Detection
- Decide the named entity type (person, place) of the answer
- Query Formulation
- Choose query keywords for the IR system
- Question Type classification
- Is this a definition question, a math question, a list question?
- Focus Detection
- Find the question words that are replaced by the answer
- Relation Extraction
- Find relations between entities in the question

### Features for Answer Type Detection
- Question words and phrases
- Part-of-speech tags
- Parse features (headwords)
- Named Entities
- Semantically related words


