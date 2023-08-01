vertices = list(set([str(s) for s, p, o in g] + [str(o) for s, p, o in g]))

# for v in vertices[0:100]:
#     print(v)
    

# for (i,(s,p,o)) in enumerate(g):
#     print(s)
#     if i > 10:
#         break

# subject = rdflib.URIRef("5294")
# up = set()
# for s,p,o in g.triples((None,None,"5294")):
#     print(f"Subject: {s}, Predicate: {p}, Object: {o}")
#     up = up.union({p})

# for p in up: print(p)

# pre = rdflib.URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")
# pre = rdflib.URIRef("http://www.biopax.org/release/biopax-level3.owl#id")
# tset = set()
# for s,p,o in g.triples((None,pre,None)):
#     print(f"Subject: {s}, Predicate: {p}, Object: {o}")
#     tset = tset.union({o})

# for t in tset: print(t)

# sub = rdflib.URIRef("Protein14981")
# pre = rdflib.URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")
# obj = rdflib.URIRef("http://www.biopax.org/release/biopax-level3.owl#SmallMolecule")
# mol = set()
# for s,p,o in g.triples((None,pre,obj)):
#     print(f"Subject: {s}, Predicate: {p}, Object: {o}")
#     mol = mol.union({s})
    
# f1 = "downloads/"