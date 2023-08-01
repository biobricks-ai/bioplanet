#!/bin/bash

# URL list
urls=(
'https://tripod.nih.gov/bioplanet/download/pathway.csv'
'https://tripod.nih.gov/bioplanet/download/pathway-category.csv'
'https://tripod.nih.gov/bioplanet/download/pathway-biopax.tar.gz'
'https://tripod.nih.gov/bioplanet/download/pathway-disease-mapping.tsv.zip'
'https://tripod.nih.gov/bioplanet/download/pathway-assay-mapping.tsv.zip'
)

# Make sure the downloads directory exists
mkdir -p ./downloads

# Loop over the URLs
for url in "${urls[@]}"
do
    # Download the file to the downloads directory
    wget -P ./downloads "$url"
done

# unzip pathway-biopax.tar.gz
tar -xzf ./downloads/pathway-biopax.tar.gz -C ./cache
