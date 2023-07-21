from tqdm import tqdm
import glob, rdflib, re
import networkx as nx
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph

owl_files = glob.glob("downloads/biopax/individual_pathways/*.owl")
g = rdflib.Graph()

for owl_file in tqdm(owl_files):
    with open(owl_file, 'r') as f:
        data = f.read()
    cleaned_data = re.sub(r'&(?!(#[0-9]+|[a-z]+);)', '&amp;', data)
    _ = g.parse(data=cleaned_data, format="xml", publicID="https://tripod.nih.gov/bioplanet/")

# Convert the RDF graph to a NetworkX graph
G = rdflib_to_networkx_multidigraph(g)

# Save the NetworkX graph as a GraphML file
nx.write_graphml(G, "brick/bioplanet.graphml")