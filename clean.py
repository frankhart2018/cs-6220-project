import pandas as pd
import json
import argparse
from typing import Dict, List

from tasks.clean_fill.clean.remove_unnamed import RemoveUnnamed
from tasks.clean_fill.clean.get_release_year import GetReleaseYear
from tasks.clean_fill.clean.running_time_mins import RunningTimeMins
from tasks.clean_fill.fill.release_date import ReleaseDate


def main():
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Clean and fill data"
    )
    parser.add_argument("--input", type=str, help="Input file", required=True)
    parser.add_argument(
        "--clean", action="store_true", help="Clean data", default=False
    )
    parser.add_argument(
        "--fill", action="store_true", help="Fill missing data", default=False
    )

    args: argparse.Namespace = parser.parse_args()

    df: pd.DataFrame = pd.read_csv(args.input)

    with open("config.json", "r") as f:
        config: Dict[str, List[str]] = json.load(f)

    processes: str = ""

    if args.fill:
        processes += "_filled"

        # Fill
        print("Filling missing data...")
        for filler in config["fillers"]:
            class_name = filler.replace("_", " ").title().replace(" ", "")
            print(f"Running {class_name} filler!")

            try:
                obj = eval(class_name)()
                df = obj.fill(df=df)
            except NameError as _:
                print(f"{class_name} filler not found!")

    if args.clean:
        processes += "_cleaned"

        # Clean
        print("Cleaning....")
        for cleaner in config["cleaners"]:
            class_name = cleaner.replace("_", " ").title().replace(" ", "")
            print(f"Running {class_name} cleaner!")

            try:
                obj = eval(class_name)()
                df = obj.clean(df)
            except NameError as _:
                print(f"{class_name} cleaner not found!")

    input_file_name = ".".join(args.input.split(".")[:-1])
    output_file_name = f"{input_file_name}{processes}_processed.csv"

    df.to_csv(output_file_name, index=False)


if __name__ == "__main__":
    main()
