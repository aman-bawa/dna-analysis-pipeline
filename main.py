import subprocess
import logging
logging.basicConfig(
    filename="C:/Users/AMAN/PycharmProjects/dna_analysis_pipeline/dna_pipeline/logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s %(message)s",
    filemode="w",
)

def main():
    try:
        logging.info("starting pipeline")
        logging.info("running validate.py")
        subprocess.run(["python","validate.py","--input","input/sequence.csv","--output","output/validated.csv"],check=True)
        logging.info("done with validate.py")
        logging.info("running analyze.py")
        subprocess.run(["python","analyze.py","--input","output/validated.csv","--output","output/analysis.csv"],check=True)
        logging.info("done  analyze.py")
        logging.info("running reports.py")
        subprocess.run(["python","reports.py","--input","output/analysis.csv","--output","output/final_report.txt"],check=True)
        logging.info("done with reports.py")
        logging.info("finished pipeline")

    except subprocess.CalledProcessError as e :
        logging.error(f"failed pipeline {e}")
        print("external program failed")

if __name__ == "__main__":
    main()