

install.packages('rgl')
install.packages('ellipse')
install.packages("C:/Users/joan.serrano.marin/Downloads/pca3d_0.10.2.tar", repos = NULL, type = "source")
library(pca3d)
library(rgl)
library(ellipse)
df <- data.frame(par_todos_PCA_5)
df
pca <- prcomp(na.omit(df[,-1]), scale = TRUE)
pca

gr <- factor(df[,1])
gr
pca3d(pca, gr=gr)
pca3d(pca, gr=gr, show.ellipses=TRUE,
      ellipse.ci=0.4, show.plane=FALSE)


# Extract the standard deviations of the principal components
pca_variances <- pca$sdev^2

# Calculate the total variance
total_variance <- sum(pca_variances)

# Calculate the percentage of variability explained by each component
percentage_variability_explained <- (pca_variances / total_variance) * 100

# Print the results
percentage_variability_explained
