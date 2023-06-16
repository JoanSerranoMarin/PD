import matplotlib.pyplot as plt
metabolites = ['Phe', 'DOPA', 'Putrescine', 'C2', 'SDMA', 'total DMA', 'C3-DC (C4-OH)', 'C0', 'Spermidine', 'Orn', 'Trp', 'Tyr', 'ADMA', 'Taurine', 'Ac-Orn', 'C5-OH (C3-DC-M)', 'Cit', 'Creatinine', 'Thr', 'C9', 'Asn', 'C3', 'Gln', 'PC aa C36:1', 'PC aa C38:4', 'PC aa C38:6', 'PC ae C34:3', 'C5', 'SM C16:0', 'C12:1', 'Kynurenine', 'Glu', 'PC ae C36:4', 'PC aa C36:4', 'PC aa C34:2', 'His', 'PC aa C36:3', 'PC aa C36:2', 'PC aa C34:1', 'PC ae C34:2', 'PC ae C38:2', 'Ala', 'SM C24:1', 'C4', 'PC ae C30:1', 'PC aa C38:5', 'C4:1', 'PC aa C36:5', 'SM C24:0', 'C5-DC (C6-OH)', 'Lys', 'Asp', 'Ser', 't4-OH-Pro', 'PC ae C38:6', 'Met', 'C10', 'lysoPC a C20:4', 'H1', 'Arg', 'PC aa C32:2', 'Met-SO', 'Ile', 'Gly', 'PC ae C36:3', 'PC ae C40:3', 'alpha-AAA', 'Val', 'Leu', 'Pro', 'PC aa C42:1', 'PC ae C32:1']
adjp_values = [2.96, 2.96, 2.96, 2.69, 2.49, 2.46, 2.15, 2.10, 2.10, 2.04, 2.04, 2.04, 2.04, 2.04, 1.39, 1.37, 1.33, 1.20, 1.19, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.90, 0.82, 0.77, 0.74, 0.74, 0.73, 0.73, 0.71, 0.66, 0.61, 0.60, 0.60, 0.58, 0.55, 0.52, 0.51, 0.51, 0.46, 0.46, 0.44, 0.43, 0.42, 0.33, 0.32, 0.32, 0.28, 0.28, 0.28, 0.27, 0.26, 0.26, 0.26, 0.23, 0.23, 0.19, 0.10, 0.09, 0.06, 0.06, 0.06, 0.05, 0.03, 0.02, 0.01, 0.00]
fold_changes = [0.41, 1.82, 1.12, 1.17, 1.12, 0.99, 0.83, 0.64, 1.21, 0.77, 0.53, 0.77, 0.65, 0.84, 1.61, 0.55, 0.75, 0.70, 0.62, 0.37, 0.46, 0.65, 0.50, 1.25, 1.37, 1.05, 1.46, 0.44, 0.96, 0.27, 0.59, 0.89, 1.31, 1.06, 1.11, 0.34, 0.89, 1.02, 0.86, 1.19, 0.72, 0.34, 1.15, 0.43, 0.33, 0.97, 0.20, 0.65, 0.54, 0.20, 0.09, 0.23, 0.22, 0.23, -0.75, 0.40, 0.11, 0.33, 0.10, 0.11, 0.31, 0.06, 0.19, -0.20, 0.24, -0.07, 0.02, 0.02, 0.01, 0.00]
plt.scatter(fold_changes, adjp_values, c='grey', alpha=0.5)
highlighted_metabolites = [metabolite for metabolite, adjp_value in zip(metabolites, adjp_values) if adjp_value > 1.3]
highlighted_adjp_values = [adjp_value for adjp_value in adjp_values if adjp_value > 1.3]
highlighted_fold_changes = [fold_change for adjp_value, fold_change in zip(adjp_values, fold_changes) if adjp_value > 1.3]
plt.scatter(highlighted_fold_changes, highlighted_adjp_values, c='orange', alpha=0.5)
plt.xlabel('log₂(FC)')
plt.ylabel('-log₁₀(adj. p-value)')
plt.title('Metabolite Scatter Plot')
plt.savefig('metabolite_plot.tiff', dpi=300, format='tiff')
plt.show()

