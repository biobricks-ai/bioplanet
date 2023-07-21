pacman::p_load(tidyverse, arrow)

pw = readr::read_csv("downloads/pathway.csv")
pwcat = readr::read_csv("downloads/pathway-category.csv")
pwdis = readr::read_tsv("downloads/pathway-disease-mapping.tsv.zip")
pwass = readr::read_tsv("downloads/pathway-assay-mapping.tsv.zip")

# write each as a parquet file
fs::dir_create("brick")
arrow::write_parquet(pw, "brick/pathway.parquet")
arrow::write_parquet(pwcat, "brick/pathway-category.parquet")
arrow::write_parquet(pwdis, "brick/pathway-disease-mapping.parquet")
arrow::write_parquet(pwass, "brick/pathway-assay-mapping.parquet")