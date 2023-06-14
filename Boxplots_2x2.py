import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load your data into a pandas dataframe
df = pd.read_csv('par_aminas_PCA.csv')

# separate your data into two groups - Parkinson's patients and controls
parkinsons_data = df[df['diagnosis'] == 'Parkinson']
control_data = df[df['diagnosis'] == 'Control']

# create 2 subplots, each containing 2 biomarkers
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# set the color palette for the boxplots
palette = {'Parkinson': '#009ACD', 'Control': 'gold'}

# iterate over each biomarker and create a boxplot for each
for i, biomarker in enumerate(df.columns[1:5]):
    row = i // 2  # determine which row to place the plot in
    col = i % 2   # determine which column to place the plot in
    sns.boxplot(x='diagnosis', y=biomarker, data=df, ax=axs[row, col], showfliers=False, palette=palette)
    sns.stripplot(x='diagnosis', y=biomarker, data=df, ax=axs[row, col], color='black', alpha=0.5)
    axs[row, col].set_title(biomarker)

plt.tight_layout()

# Save the figure as a TIFF file with a resolution of 300 ppi
plt.savefig('boxplots.tiff', dpi=300, format='tiff')

# Show the plot
plt.show()
