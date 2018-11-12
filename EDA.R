library(dplyr)
library(readr)
library(tidyr)
library(plyr)
library(ggplot2)

df.x <- read_csv("data/preprocessed/merged/X.csv")
df.y <- read_csv("data/preprocessed/merged/Y.csv")
sensitive <- read_csv("data/raw/SensitiveColumns.csv")

df.y$X1 <- NULL

df_filt <- df.x %>% select(sensitive$ColumnCode, 'SEQN')
df_filt <- join(df_filt, df.y)
