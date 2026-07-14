import argparse
import csv
import logging

logging.basicConfig(
    filename="C:/Users/AMAN/PycharmProjects/dna_analysis_pipeline/dna_pipeline/logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s %(message)s",
    filemode="a",
)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path of input file", required=True)
    parser.add_argument("--output", help="path of output file", required=True)
    args = parser.parse_args()
    logging.info(f"parsing arguments {args}")
    return args.input, args.output


def read_input_file(input_file):
    logging.info(f"reading input file {input_file}")
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


def statistics(data):
    total_gene = len(data)
    high_gc = float(data[0]["GC_content"])
    high_gc_gene = data[0]["Gene"]
    low_gc = float(data[0]["GC_content"])
    low_gc_gene = data[0]["Gene"]
    sum_gc = 0
    for row in data:
        logging.info(f"calculating statistics for {row['Gene']}")
        sum_gc += float(row["GC_content"])
        if float(row["GC_content"]) > high_gc:
            high_gc = float(row["GC_content"])
            high_gc_gene = row["Gene"]
        if float(row["GC_content"]) < low_gc:
            low_gc = float(row["GC_content"])
            low_gc_gene = row["Gene"]
    average_gc = sum_gc / total_gene
    return total_gene, high_gc, low_gc, average_gc, high_gc_gene, low_gc_gene


def generate_report(total_gene, high_gc, low_gc, average_gc, high_gc_gene, low_gc_gene):
    logging.info(f"writing report")
    return (
        f"================DNA REPORT====================\n"
        f"Total Gene: \n {total_gene}\n"
        f"highest GC : \n {high_gc_gene}\n {high_gc}\n"
        f"lowest GC : \n {low_gc_gene}\n {low_gc}\n"
        f"average GC : \n {average_gc}\n"
    )


def write_report(
    output_file, total_gene, high_gc, low_gc, average_gc, high_gc_gene, low_gc_gene
):
    logging.info(f"writing report")
    with open(output_file, "w") as f:
        rep = generate_report(
            total_gene, high_gc, low_gc, average_gc, high_gc_gene, low_gc_gene
        )
        f.write(rep)


def main():
    logging.info(f"opening main")
    try:
        input_file, output_file = parse_args()
        data = read_input_file(input_file)
        total_gene, high_gc, low_gc, average_gc, high_gc_gene, low_gc_gene = statistics(
            data
        )
        write_report(
            output_file,
            total_gene,
            high_gc,
            low_gc,
            average_gc,
            high_gc_gene,
            low_gc_gene,
        )
        logging.info("done")

    except Exception:
        logging.exception("Error occurred")


if __name__ == "__main__":
    main()
