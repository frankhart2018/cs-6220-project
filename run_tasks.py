import pandas as pd
import argparse
import json

from tasks.process.movie_desc_embeddings.movie_desc_embeddings_runner import MovieDescEmbeddingsRunner


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tasks")
    parser.add_argument("-d", "--dataset", type=str, required=True, help="Dataset to use")

    args = parser.parse_args()

    with open("config.json", "r") as f:
        config = json.load(f)

    df = pd.read_csv(args.dataset)

    tsne_config = config["movie_desc_embeddings_runner"]["tsne"]
    n_components = tsne_config["n_components"]
    init = tsne_config["init"]
    embeddings_path = tsne_config["embeddings_path"]
    tsne_x_path = tsne_config["tsne_x_path"]
    tsne_y_path = tsne_config["tsne_y_path"]

    input_dict = {
        "df": df,
        "n_components": n_components,
        "init": init,
        "embeddings_path": embeddings_path,
        "tsne_x_path": tsne_x_path,
        "tsne_y_path": tsne_y_path
    }

    tasks = ["MovieDescEmbeddingsRunner"]

    for task in tasks:
        runner = eval(task)()
        runner.run(**input_dict)
