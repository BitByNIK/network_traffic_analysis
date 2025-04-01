import os
import glob
import pandas as pd


def read_csv_files_in_directory(data_directory_path: str, cache_directory_path: str, cached_file_name: str) -> pd.DataFrame:
    os.makedirs(cache_directory_path, exist_ok=True)

    cached_file_path = os.path.join(cache_directory_path, cached_file_name)
    if os.path.exists(cached_file_path):
        return pd.read_pickle(cached_file_path)

    csv_files = glob.glob(f"{data_directory_path}/*.csv")

    df_list = [pd.read_csv(csv_file) for csv_file in csv_files]
    df = pd.concat(df_list, ignore_index=True)

    df.to_pickle(cached_file_path)

    return df


def display_top_items(msg: str, data: pd.Series) -> None:
    print(f"\n{msg}:")
    for item, count in data.items():
        print(f"{item}: {count}")
