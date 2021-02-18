from .file import QDasFile
import pandas as pd


def read_qdas_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return QDasFile(lines)


def create_attribute_dataframe(attribute, grouped=False) -> pd.DataFrame:
    df = pd.DataFrame([m.as_dict() for m in attribute.get_measurements()])
    df.columns = ["datetime", "value"]

    if grouped:
        df = df.groupby("datetime").aggregate("mean").reset_index()
        df["datetime"] = pd.to_datetime(df["datetime"])
        df = df.set_index("datetime")

    return df


def create_column_dataframe(qdas_data, part_index=0) -> pd.DataFrame:
    qdas_df = pd.DataFrame()

    for i, attribute in enumerate(qdas_data.parts[part_index].get_attributes()):
        name = attribute.get_data("K2002")

        if name != "":
            df = create_attribute_dataframe(attribute, True)
            df.columns = [name]

            qdas_df = pd.concat([qdas_df, df], axis=1)

    qdas_df = qdas_df.sort_index()
    return qdas_df
