from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# plot 1

#Locates the dataset.
project_folder = Path(__file__).resolve().parent
data_file = project_folder / "data" / "raw" / "winequality-red.csv"

#reads the CSV file, semicolons between values.
wine = pd.read_csv(data_file, sep=";")

#Spearman correlations: correlate the ranked measurements.
correlation_matrix = wine.rank().corr()

#Selects each chemical measurement's correlation with quality.
quality_correlations = (correlation_matrix["quality"].drop("quality").sort_values())

plt.figure(figsize=(9, 6))

bars = plt.barh(quality_correlations.index, quality_correlations.values, color="#4ECDC4")

plt.bar_label(bars, fmt="%.3f", padding=3)
plt.axvline(0, color="black", linewidth=1)

plt.xlim(-1, 1)
plt.xlabel("Spearman correlation with quality")
plt.title("Chemical measurements associated with red-wine quality")

plt.tight_layout()
plt.show()

# Convert quality scores into ranks.
quality_ranks = wine["quality"].rank()

# Spearman correlation = Pearson correlation of the ranks.
alcohol_rho = wine["alcohol"].rank().corr(quality_ranks)

acidity_rho = wine["volatile acidity"].rank().corr(quality_ranks)

# Display the results to three decimal places.
print(f"Alcohol vs quality: Spearman rho = {alcohol_rho:.3f}")
print(f"Volatile acidity vs quality: Spearman rho = {acidity_rho:.3f}")

#categories for the bar chart
qualitycategories = [3, 4, 5, 6, 7, 8]

#locates the 11 value
qualityvalues = wine.iloc[:, 11]

qualitycounts = qualityvalues.value_counts().reindex(qualitycategories, fill_value=0)

plt.figure(figsize=[10, 5])
bars = plt.bar(qualitycategories, qualitycounts, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#A8E6CF'])

plt.bar_label(bars, fmt="%.0f", padding=3) #precise value over reach individual bar
plt.ylim(0, qualitycounts.max() * 1.12)

plt.xlabel("Quality score")
plt.ylabel("Number of wines")
plt.title("Red wine quality distribution")
plt.show()

# plot 2

#Each list contains one group of measurements per score.
alcoholgroups = []
aciditygroups = []
ticklabels = []

for score in qualitycategories:
    #Selects only the wines with this quality score.
    group = wine[wine["quality"] == score]

    #Collects their chemical measurements.
    alcoholgroups.append(group["alcohol"])
    aciditygroups.append(group["volatile acidity"])

    #Includes the number of wines below each box.
    ticklabels.append(f"{score}\n(n={len(group)})")


#Alcohol by quality.
plt.figure(figsize=(8, 5))

plt.boxplot(alcoholgroups, positions=qualitycategories, patch_artist=True, boxprops={"facecolor": "#4ECDC4"}, medianprops={"color": "black"})

plt.xticks(qualitycategories, ticklabels)
plt.xlabel("Quality score")
plt.ylabel("Alcohol (% by volume)")
plt.title("Alcohol content by wine quality")
plt.tight_layout()


#Volatile acidity by quality.
plt.figure(figsize=(8, 5))

plt.boxplot(aciditygroups, positions=qualitycategories, patch_artist=True, boxprops={"facecolor": "#FFA07A"}, medianprops={"color": "black"})

plt.xticks(qualitycategories, ticklabels)
plt.xlabel("Quality score")
plt.ylabel("Volatile acidity (g/L, as acetic acid)")
plt.title("Volatile acidity by wine quality")
plt.tight_layout()

#Displays each figure in its own window.
plt.show()

summary = wine.groupby("quality").agg(number_of_wines=("quality", "size"), median_alcohol=("alcohol", "median"), median_volatile_acidity=("volatile acidity", "median"))

print(summary)

higher_quality = wine[wine["quality"] >= 7]

profile = (higher_quality.drop(columns="quality").describe().loc[["25%", "50%", "75%"]].T)

print(profile)