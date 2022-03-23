import os
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a streamlit application")
    parser.add_argument("-a", "--app", help="The name of the app to run", required=True)

    args = parser.parse_args()

    os.system(f"streamlit run {args.app}")