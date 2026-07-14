import argparse
import csv
import logging


logging.basicConfig(
    filename="C:/Users/AMAN/PycharmProjects/dna_analysis_pipeline/dna_pipeline/logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    filemode="a",
)


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path of input file", required=True)
    parser.add_argument("--output", help="path of output file", required=True)
    args = parser.parse_args()
    logging.info(f"parsing args: {args}")
    return args.input, args.output


def read_input_file(input_file):
    logging.info(f"reading input file: {input_file}")
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


def writ_output_file(output_file, data):
    logging.info(f"writing output file: {output_file}")
    with open(output_file, "w", newline="") as f:
        fieldnames = ["Gene", "length", "GC_content"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        logging.info(f"calculating statistics ")
        for row in data:
            length = len(row["Sequence"])
            G_content = row["Sequence"].count("G")
            C_content = row["Sequence"].count("C")
            GC_content = float(((G_content + C_content) / length) * 100)
            writer.writerow(
                {"Gene": row["Gene"], "length": length, "GC_content": GC_content}
            )


def main():
    logging.info(f"Starting main")
    input_file, output_file = parseArgs()
    try:
        data = read_input_file(input_file)
        writ_output_file(output_file, data)
        logging.info(f"Finished main")

    except Exception as e:
        logging.exception("exception occurred")


if __name__ == "__main__":
    main()
