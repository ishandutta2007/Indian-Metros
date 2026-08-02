import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Dataset of Indian Metropolitan areas and their respective states & GDP estimates
data = {
    "Metropolitan_Area": [
        "Mumbai", "Delhi NCR", "Kolkata", "Bengaluru", "Chennai", 
        "Hyderabad", "Ahmedabad", "Pune", "Surat", "Visakhapatnam",
        "Coimbatore", "Kochi", "Nagpur", "Lucknow", "Jaipur", 
        "Indore", "Patna", "Kanpur", "Vadodara", "Nashik"
    ],
    "State": [
        "Maharashtra", "Delhi NCT", "West Bengal", "Karnataka", "Tamil Nadu", 
        "Telangana", "Gujarat", "Maharashtra", "Gujarat", "Andhra Pradesh",
        "Tamil Nadu", "Kerala", "Maharashtra", "Uttar Pradesh", "Rajasthan", 
        "Madhya Pradesh", "Bihar", "Uttar Pradesh", "Gujarat", "Maharashtra"
    ],
    "GDP_Billion_USD": [
        310.0, 293.6, 150.0, 110.0, 78.6, 
        75.0, 72.0, 69.0, 60.0, 48.5,
        45.0, 40.0, 36.5, 34.0, 31.5, 
        29.0, 25.0, 22.0, 21.0, 20.5
    ]
}

# 2. Convert to DataFrame
df = pd.DataFrame(data)

# 3. Filter for Metropolitan Areas with GDP > $10 Billion
df_filtered = df[df["GDP_Billion_USD"] > 10]

# 4. Group by State and count the number of high-GDP areas
state_counts = (
    df_filtered.groupby("State")["Metropolitan_Area"]
    .count()
    .reset_index(name="Count_of_10B_Plus_Areas")
)

# 5. Sort states by count descending (Ranking)
state_counts_sorted = state_counts.sort_values(by="Count_of_10B_Plus_Areas", ascending=False)

# 6. Generate the Rank Plot
plt.figure(figsize=(10, 5))
sns.set_theme(style="whitegrid")

# Create a horizontal bar chart for clean ranking presentation
ax = sns.barplot(
    x="Count_of_10B_Plus_Areas", 
    y="State", 
    data=state_counts_sorted, 
    palette="viridis",
    hue="State",
    legend=False
)

# Customize title and axis labels
plt.title("Rank of Indian States by Number of $10B+ GDP Metro Areas", fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Number of Metropolitan Areas (> $10B GDP)", fontsize=11, labelpad=10)
plt.ylabel("State", fontsize=11)

# Format x-axis to only display whole integers
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True))

# Add count value labels to the end of each bar
for p in ax.patches:
    width = p.get_width()
    if width > 0:
        ax.text(
            width + 0.1, 
            p.get_y() + p.get_height() / 2, 
            f'{int(width)}', 
            ha='left', 
            va='center', 
            fontsize=10, 
            fontweight='bold'
        )

plt.tight_layout()
plt.show()

