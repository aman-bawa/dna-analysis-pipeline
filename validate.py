import csv
import re
import logging
import argparse

logging.basicConfig(
    filename="C:/Users/AMAN/PycharmProjects/dna_analysis_pipeline/dna_pipeline/logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s %(message)s",
    filemode="w",
)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to input file")
    parser.add_argument("--output", required=True, help="path to output file")
    args = parser.parse_args()
    logging.info(f"parsing args: {args}")
    return args.input, args.output


def open_input_file(input_file, writer):
    with open(input_file, mode="r") as file:
        logging.info(f"Reading file {input_file}")
        reader = csv.DictReader(file)
        data = list(reader)
        pattern = re.compile("^[ACGT]+$")
        reason = []
        success = 0
        failed = 0
        total_genes = len(data)
        for row in data:
            if len(row["Sequence"]) < 5 and not pattern.fullmatch(row["Sequence"]):
                failed += 1
                print(f"{row['Gene']}\t{row['Sequence']} is NOT a valid sequence")
                reason.append(row["Gene"])
                logging.info(
                    f"Rejected {row['Gene']}\n Reason:  NOT a valid sequence and short sequence"
                )
            elif len(row["Sequence"]) < 5:
                failed += 1
                print(f"{row['Gene']}\t{row['Sequence']} is less than 5 nucleotides")
                reason.append(row["Gene"])
                logging.info(
                    f"Rejected {row['Gene']}\n Reason: Sequence less than 5 nucleotides"
                )
            elif not pattern.fullmatch(row["Sequence"]):
                failed += 1
                print(f"{row['Gene']}\t{row['Sequence']} is NOT a valid sequence")
                reason.append(row["Gene"])
                logging.info(f"Rejected {row['Gene']}\n Reason:  NOT a valid sequence")

            else:
                success += 1
                writer.writerow({"Gene": row["Gene"], "Sequence": row["Sequence"]})
        return success, failed, total_genes, reason


def write_in_output_file(output_file, input_file):
    with open(output_file, mode="w", newline="") as f:
        logging.info(f"writing to {output_file}")
        fieldnames = ["Gene", "Sequence"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        success, failed, total_genes, reason = open_input_file(input_file, writer)
        logging.info(f" done writing to {output_file}")

    return success, failed, total_genes, reason


def main():
    logging.info(f"Running main")
    input_file, output_file = parse_args()
    try:
        success, failed, total_genes, reason = write_in_output_file(
            output_file, input_file
        )

        print("==================summary=============")
        print(f"total genes: {total_genes}")
        print(f"success in validated genes {success}")
        print(f"failed in validated genes {failed}")
        print(f"failed in validated genes {reason}")
        print("                   DONE                       ")

        logging.info(f"DONE")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
