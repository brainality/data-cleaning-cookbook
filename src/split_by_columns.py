import pandas as pd
import logging

def split_dataset_by_columns(csv_path, columns):
    \"\"\"
    Minimal: split a CSV into multiple files based on which of the given columns is filled.
    Example: split_dataset_by_columns(\"data.csv\", [\"sex\", \"age\"])
    - Checks that no row has more than one of these columns filled.
    - For each column, keeps rows where that column is filled and drops the others.
    - Saves one CSV per column: <name>_by_<col>.csv
    \"\"\"
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    logging.info(\"Loading dataset...\")
    df = pd.read_csv(csv_path)
    total_rows = len(df)
    logging.info(f\"Total rows in original dataset: {total_rows}\")

    # 1) Validate: no row has more than one of the specified columns filled
    filled_counts = df[columns].notna().sum(axis=1)
    invalid = df[filled_counts > 1]
    if not invalid.empty:
        logging.warning(f\"⚠️ {len(invalid)} rows have multiple category columns filled.\")
    else:
        logging.info(\"No rows with multiple category columns filled. ✅\")

    # 2) Split + save
    total_split_rows = 0
    for col in columns:
        mask = df[col].notna()
        # keep current category column + all non-category columns
        keep = [c for c in df.columns if c not in columns] + [col]
        subset = df.loc[mask, keep]
        total_split_rows += len(subset)

        out_path = csv_path.replace('.csv', f'_by_{col}.csv')
        subset.to_csv(out_path, index=False)
        logging.info(f\"Saved '{col}' subset → {out_path} ({len(subset)} rows)\")

    # 3) Sanity check
    logging.info(f\"Total rows after split: {total_split_rows}\")
    if total_split_rows == total_rows:
        logging.info(\"✅ Row counts match — split successful.\")
    else:
        logging.warning(\"⚠️ Row count mismatch — check for missing/invalid rows.\")
