import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load your data into a pandas dataframe
df = pd.read_csv('par_tots.csv')

# separate your data into two groups - Parkinson's patients and controls
parkinsons_data = df[df['diagnosis'] == 'Parkinson']
control_data = df[df['diagnosis'] == 'Control']

# create 6 subplots, each containing 1 biomarker
fig, axs = plt.subplots(4, 4, figsize=(10, 12))

# set the color palette for the boxplots
palette = {'Parkinson': '#009ACD', 'Control': 'gold'}

# iterate over each biomarker and create a boxplot for each
for i, biomarker in enumerate(df.columns[1:17]):
    row = i // 4  # determine which row to place the plot in
    col = i % 4   # determine which column to place the plot in
    sns.boxplot(x='diagnosis', y=biomarker, data=df, ax=axs[row, col], showfliers=False, palette=palette)
    sns.stripplot(x='diagnosis', y=biomarker, data=df, ax=axs[row, col], color='black', alpha=0.5)
    axs[row, col].set_title(biomarker)
    # Remove axis labels and titles
    axs[row, col].set_xlabel('')
    axs[row, col].set_ylabel('')
    axs[row, col].set_xticklabels([])  # Remove X labels

plt.tight_layout()

# Save the figure as a TIFF file with a resolution of 300 ppi
plt.savefig('boxplots.tiff', dpi=300, format='tiff')

# Show the plot
plt.show()