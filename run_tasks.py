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

    # Task 1 config
    movie_desc_embeddings_runner_config = config["tasks"]["movie_desc_embeddings_runner"]
    tsne_config = movie_desc_embeddings_runner_config["tsne"]
    pca_config = movie_desc_embeddings_runner_config["pca"]
    n_components = movie_desc_embeddings_runner_config["n_components"]
    embeddings_path = movie_desc_embeddings_runner_config["embeddings_path"]

    # T-SNE config
    init = tsne_config["init"]
    tsne_x_path = tsne_config["tsne_x_path"]
    tsne_y_path = tsne_config["tsne_y_path"]

    # PCA config
    pca_x_path = pca_config["pca_x_path"]
    pca_y_path = pca_config["pca_y_path"]

    input_dict = {
        "df": df,
        "n_components": n_components,
        "init": init,
        "embeddings_path": embeddings_path,
        "tsne_x_path": tsne_x_path,
        "tsne_y_path": tsne_y_path,
        "pca_x_path": pca_x_path,
        "pca_y_path": pca_y_path,
    }

    tasks = config["run_tasks"]

    for task in tasks:
        task_name = task.replace("_", " ").title().replace(" ", "")
        subtasks = config["run_tasks"][task]
        runner = eval(task_name)(subtasks=subtasks)
        runner.run(**input_dict)
