from .file import DfqFile
import pandas as pd


def read_dfq_file(filename):
    """
    Reads a *.DFQ file from file system and parses the file contents.

    Parameters
    ----------
    filename
        The filename including the path to read.

    Returns
    -------
    DfqFile
        A new DfqFile object which holds all data of the file
        in data strucutres which can be accessed.
    """
    with open(filename, "rb") as f:
        lines = f.read().decode("iso8859-1", errors="replace").splitlines()

    return DfqFile(lines)


def create_characteristic_dataframe(characteristic, unique=False) -> pd.DataFrame:
    """
    Converts a characteristic inlcuding measured values into a pandas DataFrame.

    Parameters
    ----------
    characteristic
        The corresponding Characteristic to be converted.
    unique : bool, default False
        If grouped is set to True, all duplicates of the measured values by
        the index of the measure datetime will be grouped and the mean value
        will be calculated.

    Returns
    -------
    DataFrame
        New DataFrame with the measured values of the Characteristic.
    """
    df = pd.DataFrame(columns=["datetime", "value"])

    if len(characteristic.get_measurements()) > 0:
        df = pd.DataFrame(
            [m.as_value_dictionary() for m in characteristic.get_measurements()]
        )
        df.columns = ["datetime", "value"]
        df["datetime"] = pd.to_datetime(df["datetime"])
        if unique:
            df = df.groupby("datetime").aggregate("mean").reset_index()

    if unique:
        df = df.set_index("datetime")

    return df


def create_column_dataframe(
    file_data: DfqFile, part_index=0, group_by_date=True
) -> pd.DataFrame:
    """
    Converts a full part of the DFQ-File into a pandas DataFrame with
    all Characteristics as columns and measured values as rows. To
    name the columns, the attribute K2002 is used.

    Parameters
    ----------
    file_data : Part
        The full aqdef reader object with all data.
    part_index : int, default 0
        If the data containts more than one part, the part to be
        used for the conversion can be specified. If only one part
        is available, the default index 0 is fine.
    group_by_date : bool, default True
        If group_by_date is set to True, all duplicates of the measured values by
        the index of the measure datetime will be grouped and the mean value
        will be calculated. Set to False if the measuers do not have
        any timestamp (datetime) as otherwise only one result will
        be returned.


    Returns
    -------
    DataFrame
        New DataFrame with the measured values of all Characteristic.
    """
    all_characteristics_df = pd.DataFrame()

    for i, characteristic in enumerate(
        file_data.get_part(part_index).get_characteristics()
    ):
        name = characteristic.get_data("K2002")

        if name != "":
            new_characteristic_df = create_characteristic_dataframe(
                characteristic, group_by_date
            )

            if not group_by_date:
                new_characteristic_df = new_characteristic_df["value"]
                new_characteristic_df.rename(name, inplace=True)

            new_characteristic_df.columns = [name]

            all_characteristics_df = pd.concat(
                [all_characteristics_df, new_characteristic_df], axis=1
            )

    all_characteristics_df = all_characteristics_df.sort_index()
    return all_characteristics_df
