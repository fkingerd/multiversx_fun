from collections import Counter
import pandas as pd



metadata_list = [
    # your metadata list here
]

counts = Counter((a['trait_type'], a['value']) for m in metadata_list for a in m['attributes'])
df = pd.DataFrame(counts.items(), columns=['Trait Type', 'Value Count'])

# Sort the DataFrame by 'Trait Type' and 'Value Count' in ascending order
df = df.sort_values(['Trait Type', 'Value Count'], ascending=[True, True])

# Export the DataFrame to a CSV file
df.to_csv('counts.csv', index=False)

print(df)
