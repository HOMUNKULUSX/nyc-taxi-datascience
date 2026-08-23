import pandas as pd



df = pd.read_csv("data/taxi.csv")


pd.set_option(
    "display.max_columns",
    None
)

with open(
    "report/checkig_data_report.TXT",
    "w",
    encoding="utf-8"
) as file:
    
    file.write(
        "DATA UNDRESTANDING REPORT \n"
    )
    file.write("=" * 50 + "\n\n")

    file.write(
        "Data Shape:\n"
    )
    file.write(str(df.shape))
    file.write("\n\n")

    file.write(
        "Columns Name:\n"
    )
    file.write(str(df.columns.tolist()))
    file.write("\n\n")

    file.write(
        "Data Type:\n"
    )
    file.write(str(df.dtypes))
    file.write("\n\n")

    file.write(
        "Unique Values:\n"
    )
    file.write(str(df.nunique()))
    file.write("\n\n")

    file.write(
        "NULL Values:\n"
    )
    file.write(str(df.isnull().sum()))
    file.write("\n\n")

    file.write(
        "Duplicate Rows:\n"
    )
    file.write(str(df.duplicated().sum()))
    file.write("\n\n")

    file.write(
        "Desciptive Statistics:\n"
    )
    file.write(str(df.describe()))


