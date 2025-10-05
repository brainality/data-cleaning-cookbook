import pandas as pd
import logging

def split_dataset_by_columns(csv_path,input_columns):
    """
    Split a dataset into multiple CSV files based on which of the given columns is filled.
    Example: split_dataset_by_columns("data.csv", ["sex", "age"])
    """
    df = pd.read_csv(csv_path)
    total_rows = len(df)
    logging.info(f"Total rows in original dataset: {total_rows}")

    filled_counts = df[input_columns].notna().sum(axis=1)
    invalid = df[filled_counts > 1]
    
    if not invalid.empty:
        logging.error(f"⛔️ file has {len(invalid)} rows with values filled! ")
        raise ValueError("Cannot split. Stopping execution... ")
    else:
        logging.info(f" ✅ No rows found with multiple category columns filled.")
        logging.info(f" 🔽 Moving to next step.")


    total_split_rows = 0
    
    for col in input_columns:
        logging.info(f"Processing column {col}")
        
        filter_rows = df[col].notna()
        drop_cols = [c for c in input_columns if c != col]
    
        subset = df[filter_rows].drop(columns = drop_cols)
        logging.info(f"Dropping cols {drop_cols}")
    
        total_split_rows += len(subset)
        logging.info(f"Dropped cols {len(subset)} {drop_cols}")
    
        out_path  = csv_path.replace('.csv',f"_by_{col}.csv")
        logging.info(f"Writing to {out_path}")
    
        subset.to_csv(out_path, index = False)
        logging.info(f"Saved {col} subset -> {out_path} {len(subset)} rows")
        logging.info(f"Total rows after split {total_split_rows}")

    if total_rows ==  total_split_rows:
        logging.info(f"✅ Row count matched - split successful")
    else:
        logging.info(f"✅ Row count did not match - check for invalid rows")
    