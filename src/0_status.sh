# TODO this needs improvement
# this checks if bioplanet has changed by
# download index.html from the bioplanet website
# and treating it as a DVC out
# DVC checks the md5 of the file
# if the MD5 changes then 1_download.sh runs again
wget -P ./downloads https://tripod.nih.gov/bioplanet/
mv ./downloads/index.html ./downloads/bioplanet.html