"""
Cleans and dedupes data.
"""

def clean_column_names(df):
    """Changes pandas column names to be more pythonic """
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')\
                                .str.replace('(', '').str.replace(')', '')
    return df

def clean_neighborhood_names(df):
    """Removes whitespace in neighborhood names """
    df["neighborhood"] = df["neighborhood"].apply(str.rstrip)
    return df

def dedupe_rows(df):
    """Dedupes similar rows """
    df.drop_duplicates()
    return df

if __name__ == "__main__":
    combined_df = clean_column_names(combined_df)
    combined_df = clean_neighborhood_names(combined_df)
    combined_df = dedupe_rows(combined_df)
