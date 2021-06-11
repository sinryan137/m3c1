import pandas as pd

df=pd.read_csv("homelessness.csv")

print(df.head())
# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(df.values)

# Print the column index of homelessness
print(df.columns)

# Print the row index of homelessness
print(df.index)

# Sort homelessness by individual
homelessness_ind = df.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())

# Select the individuals column
individuals = df["individuals"]

# Print the head of the result
print(individuals.head())

# Filter for rows where individuals is greater than 10000
ind_gt_10k = df[df["individuals"] > 10000]

# See the result
print(ind_gt_10k)

# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = df[(df["region"] == "South Atlantic") | (df["region"] == "Mid-Atlantic")]

# See the result
print(south_mid_atlantic)

# Add total col as sum of individuals and family_members
df["total"]= df["individuals"]+df["family_members"]

# Add p_individuals col as proportion of individuals
df["p_individuals"]= df["individuals"]/df["total"]

# See the result
print(df)

# Create indiv_per_10k col as homeless individuals per 10k state pop
df["indiv_per_10k"] = 10000 * df["individuals"] / homelessness["state_pop"]

# Subset rows for indiv_per_10k greater than 20
high_homelessness = df[df["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)

