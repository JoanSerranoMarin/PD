
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

