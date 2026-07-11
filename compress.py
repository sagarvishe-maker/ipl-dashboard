import pandas as pd

df = pd.read_csv("ipl2008-25.csv", low_memory=False)

df.to_csv("ipl_data.csv.gz", index=False, compression="gzip")

print("Done")