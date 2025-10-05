# Data tools

Minimal, reusable utilities for data cleaning and quick transformations.

This repo starts with a tiny, **generic splitter** that divides a CSV into one file per
**mutually exclusive** column (e.g., `["sex", "age"]`). It validates that no row
has more than one of those columns filled, then saves a CSV per category.

## Features
- ✅ Straightforward function with logging
- ✅ Generic list of columns (`["sex", "age"]`, or any set you want)
- ✅ Sanity checks and clear output
- ✅ Example script and demo notebook

## Install
```bash
# (Optionally) create and activate a venv first
# python -m venv .venv && source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate                              # Windows

pip install -r requirements.txt
```

## Usage
**From Python:**
```python
from src.split_by_columns import split_dataset_by_columns

split_dataset_by_columns("data/sample/Northern_Ireland_Online_Crime.csv", ["sex", "age"])
```

**From the included script:**
```bash
python split_example.py
```

### What it outputs
For input `data.csv` and columns `["sex", "age"]`, you'll get:
- `data_by_sex.csv`
- `data_by_age.csv`

Each contains only the rows for that column (e.g., rows where `sex` is set)
and drops the other specified category columns.

## Project layout
```
Data-tools/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ LICENSE
├─ src/
│  └─ split_by_columns.py
├─ split_example.py
└─ notebooks/
   └─ 01_split_by_columns.ipynb
```

## Contributing
PRs welcome! Keep utilities **minimal and well-logged**.
