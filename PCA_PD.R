
install.packages('rgl')
install.packages('ellipse')
install.packages("C:/Users/joan.serrano.marin/Downloads/pca3d_0.10.2.tar", repos = NULL, type = "source")
library(pca3d)
df <- data.frame(Parkinson_3chosen)
pca <- prcomp(df[,-1], scale.=TRUE)
gr <- factor(df[,1])
pca3d(pca, group=gr)
pca3d(pca, group=gr, show.ellipses=TRUE,
      ellipse.ci=0.4, show.plane=FALSE)

