import ast
from simplpy.dict_.dict_func import dict_sort
import pickle

from tasks.process.task_runner import TaskRunner


class ComputeGenreOccurenceDict(TaskRunner):
    def __dump_to_pickle(self, obj, path):
        with open(path, 'wb') as f:
            pickle.dump(obj, f)

    def run(self, **kwargs):
        required_args = ["df", "grouped_genres_dict_path", "genre_count_dict_path"]
        self._required_args_checker(kwargs, required_args)

        df = kwargs["df"]
        df['Genre'] = df['Genre'].apply(lambda x: ast.literal_eval(x))

        genres = []

        for _, row in df.iterrows():
            genres.extend(row['Genre'])

        unique_genres = list(set(genres))

        grouped_genres = {}
        genre_count = {genre: 0 for genre in unique_genres}

        for pivot_genre in unique_genres:
            grouped_genre_for_pivot = {genre: 0 for genre in unique_genres if genre != pivot_genre}
            for _, row in df.iterrows():
                row_genres = row['Genre']
                if pivot_genre in row_genres:
                    genre_count[pivot_genre] += 1
                    for row_genre in row_genres:
                        if row_genre != pivot_genre:
                            grouped_genre_for_pivot[row_genre] += 1

            grouped_genres[pivot_genre] = dict_sort(grouped_genre_for_pivot, by="value", topk=5)

        self.__dump_to_pickle(grouped_genres, kwargs["grouped_genres_dict_path"])
        self.__dump_to_pickle(genre_count, kwargs["genre_count_dict_path"])
