from tqdm import tqdm
import glob, rdflib, re
import networkx as nx
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import pandas as pd
import pyarrow as pa

owl_files = glob.glob("cache/individual_pathways/*.owl")
g = rdflib.Graph()

for owl_file in tqdm(owl_files):
    with open(owl_file, 'r') as f:
        data = f.read()
    cleaned_data = re.sub(r'&(?!(#[0-9]+|[a-z]+);)', '&amp;', data)
    _ = g.parse(data=cleaned_data, format="xml", publicID="https://tripod.nih.gov/bioplanet/")

triples = [triple for triple in g]

def update_uri(uri):
    # Convert the URI to a string
    uri_str = str(uri)
    # Regular expression pattern to match a sequence of letters immediately followed by a sequence of digits at the end of the string
    pattern = r'([A-Za-z]+)(\d+)$'
    # Check if the URI follows the poor formatting
    if re.search(pattern, uri_str):
        # If it does, add a slash between the sequence of letters and the sequence of digits
        updated_uri = re.sub(pattern, r'\1/\2', uri_str)
        # Return the updated URI as a rdflib.term.URIRef object
        return rdflib.term.URIRef(updated_uri)
    else:
        # If the URI doesn't follow the poor formatting, return it unchanged
        return uri

# Update the triples
updated_triples = []
for s, p, o in tqdm(triples, desc="Updating triples", unit="triple"):
    updated_s = update_uri(s)
    updated_p = update_uri(p)
    if isinstance(o, rdflib.term.URIRef):
        updated_o = update_uri(o)
    else:
        updated_o = o
    updated_triples.append((updated_s, updated_p, updated_o))

# Build a dataframe, each row is an edge
df = pd.DataFrame(updated_triples, columns=['subject', 'predicate', 'object'])

# Convert the URIs to string format
df['subject'] = df['subject'].astype(str)
df['predicate'] = df['predicate'].astype(str)
df['object'] = df['object'].astype(str)

# Count the predicates
predicate_counts = df['predicate'].value_counts()
print("Predicate counts:")
print(predicate_counts)

# Count the subject classes
subject_class_counts = df['subject'].apply(lambda s: s.split('/')[-2] if '/' in s else s).value_counts()
print("\nSubject class counts:")
print(subject_class_counts)

# Count the object classes
object_class_counts = df['object'].apply(lambda o: o.split('/')[-2] if '/' in o else o).value_counts()
print("\nObject class counts:")
print(object_class_counts)

# write as parquet
df.to_parquet('brick/biopax_rdf.parquet')