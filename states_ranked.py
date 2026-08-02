import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# JSON data loaded from the Wikipedia source

data = ""
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.DataFrame(data)

# Filter: Metropolitan areas with > $10B USD GDP
df_filtered = df[df["gdp_billion_usd"] >= 10.0]

# Aggregate count of cities per state
state_counts = df_filtered.groupby("state").size().reset_index(name="metro_count")
state_counts = state_counts.sort_values(by="metro_count", ascending=False)

# Visualization
plt.figure(figsize=(11, 6))
sns.set_theme(style="whitegrid")
ax = sns.barplot(
    x="metro_count",
    y="state",
    data=state_counts,
    palette="viridis",
    hue="state",
    legend=False,
)
plt.title("Indian States with $10B+ GDP Metropolitan Areas (2022-23)", fontsize=13)
plt.xlabel("Number of Cities", fontsize=11)
plt.ylabel("State / UT", fontsize=11)
plt.tight_layout()
plt.savefig("assets/states_rank.png", bbox_inches="tight", dpi=150)
plt.show()
