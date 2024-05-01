import polars as rs

reader = rs.read_csv_batched(
    "dataset_TIST2015/dataset_TIST2015_POIs.txt", low_memory=True
)

batches = reader.next_batches(100)
seen_groups = set()


while batches:

    print(batches)

    batches = reader.next_batches(100)
