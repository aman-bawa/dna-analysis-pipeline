# DNA Analysis Pipeline

## About

This is a small DNA analysis pipeline that I built while learning Python automation.
The main goal of this project was not only to analyze DNA sequences
but also to practice writing modular Python programs, using command-line arguments,
logging, CSV handling, and automating multiple scripts with `subprocess`.

The pipeline takes a CSV file containing gene names and DNA sequences
,validates the sequences, calculates some basic statistics,
and generates a final summary report.

---

## Project Structure

```
dna_pipeline/
│
├── main.py
├── validate.py
├── analyze.py
├── report.py
│
├── input/
│   └── sequence.csv
│
├── output/
│   ├── validated.csv
│   ├── analysis.csv
│   └── final_report.txt
│
└── logs/
    └── pipeline.log
```

---

## Pipeline Workflow

```
sequence.csv
      │
      ▼
validate.py
      │
      ▼
validated.csv
      │
      ▼
analyze.py
      │
      ▼
analysis.csv
      │
      ▼
report.py
      │
      ▼
final_report.txt
```

`main.py` runs all three scripts automatically using Python's `subprocess` module.

---

## Features

### 1. Validation

* Checks whether DNA sequences contain only A, C, G and T.
* Rejects sequences shorter than 5 nucleotides.
* Saves only valid sequences to `validated.csv`.
* Logs rejected sequences with the reason.

### 2. Analysis

For every valid sequence, the program calculates:

* Sequence length
* GC percentage

The results are stored in `analysis.csv`.

### 3. Report Generation

Generates a text report containing:

* Total number of genes
* Highest GC content
* Lowest GC content
* Average GC content

The report is saved as `final_report.txt`.

### 4. Logging

Every stage of the pipeline records its progress in `pipeline.log`.

---

## How to Run

Run the complete pipeline:

```bash
python main.py
```

Run individual scripts:

Validation

```bash
python validate.py --input input/sequence.csv --output output/validated.csv
```

Analysis

```bash
python analyze.py --input output/validated.csv --output output/analysis.csv
```

Report

```bash
python report.py --input output/analysis.csv --output output/final_report.txt
```

---

## Technologies Used

* Python
* argparse
* csv
* logging
* re (Regular Expressions)
* subprocess

---

## What I Learned

While building this project I practiced:

* Working with CSV files
* Using command-line arguments with `argparse`
* Writing modular programs using functions
* Using regular expressions for validation
* Logging program execution
* Automating multiple Python scripts using `subprocess`
* Structuring a project into multiple independent modules

This project helped me understand how small Python programs can be combined into a complete workflow, which is a common approach in bioinformatics pipelines.
