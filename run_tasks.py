import pandas as pd
import argparse
import json

from tasks.process.movie_desc_embeddings.movie_desc_embeddings_runner import MovieDescEmbeddingsRunner
from tasks.process.content_based_filtering.content_based_filtering_runner import ContentBasedFilteringRunner
from tasks.process.genre_popularity.genre_popularity_runner import GenrePopularityRunner


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tasks")
    parser.add_argument("-d", "--dataset", type=str, required=True, help="Dataset to use")

    args = parser.parse_args()

    with open("config.json", "r") as f:
        config = json.load(f)

    df = pd.read_csv(args.dataset)

    #################################################################
    # TASK 1 Config
    #################################################################
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

    #################################################################
    # TASK 2 Config
    #################################################################
    content_based_filtering_runner_config = config["tasks"]["content_based_filtering_runner"]

    # TfIdf config
    tfidf_config = content_based_filtering_runner_config["tfidf"]
    similarity_matrix_path_tfidf = tfidf_config["similarity_matrix_path_tfidf"]
    df_mapping_path_tfidf = tfidf_config["df_mapping_path_tfidf"]

    # Nn config
    nn_config = content_based_filtering_runner_config["nn"]
    similarity_matrix_path_nn = nn_config["similarity_matrix_path_nn"]
    df_mapping_path_nn = nn_config["df_mapping_path_nn"]

    #################################################################
    # TASK 2 Config
    #################################################################
    genre_popularity_runner_config = config["tasks"]["genre_popularity_runner"]
    grouped_genres_dict_path = genre_popularity_runner_config["grouped_genres_dict_path"]
    genre_count_path = genre_popularity_runner_config["genre_count_dict_path"]

    input_dict = {
        "df": df,
        "n_components": n_components,
        "init": init,
        "embeddings_path": embeddings_path,
        "tsne_x_path": tsne_x_path,
        "tsne_y_path": tsne_y_path,
        "pca_x_path": pca_x_path,
        "pca_y_path": pca_y_path,
        "similarity_matrix_path_tfidf": similarity_matrix_path_tfidf,
        "df_mapping_path_tfidf": df_mapping_path_tfidf,
        "similarity_matrix_path_nn": similarity_matrix_path_nn,
        "df_mapping_path_nn": df_mapping_path_nn,
        "grouped_genres_dict_path": grouped_genres_dict_path,
        "genre_count_dict_path": genre_count_path,
    }

    tasks = config["run_tasks"]

    for task in tasks:
        task_name = task.replace("_", " ").title().replace(" ", "")
        print(f"Running {task_name}")
        subtasks = config["run_tasks"][task]
        runner = eval(task_name)(subtasks=subtasks)
        runner.run(**input_dict)
