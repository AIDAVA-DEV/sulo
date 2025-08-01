from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, OWL, DCTERMS, XSD
from datetime import datetime
import os

# === Configuration ===
INPUT_FILE = "sulo.ttl"  # Make sure your ontology is in Turtle format
MODIFIED_DATE = datetime.now().date().isoformat()  # e.g., "2025-07-31"
VERSION_DIR = "versions"  # Directory to store versioned files
LATEST_DIR = VERSION_DIR + "/latest"  # Directory for the latest version

if not os.path.exists(LATEST_DIR):
    os.makedirs(LATEST_DIR)

# === Load ontology ===
g = Graph()
g.parse(INPUT_FILE, format="turtle")

# === Identify ontology URI ===
ontologies = list(g.subjects(RDF.type, OWL.Ontology))
if not ontologies:
    raise ValueError("No owl:Ontology entity found in the file.")
ontology_iri = ontologies[0]

# === Get version info ===
version_literal = next(g.objects(ontology_iri, OWL.versionInfo), None)
if not version_literal:
    raise ValueError("No owl:versionInfo found.")
current_version = str(version_literal)
if not current_version:
    raise ValueError("No owl:versionInfo found for the ontology.")

# === Increment version number ===
def increment_version(ver):
    parts = ver.strip().split(".")
    if not all(p.isdigit() for p in parts):
        raise ValueError(f"Unrecognized version format: {ver}")
    parts[-1] = str(int(parts[-1]) + 1)
    return ".".join(parts)

new_version = increment_version(current_version)


# === Generate new ontology IRI and version IRI ===
base_name = os.path.splitext(os.path.basename(INPUT_FILE))[0]
base_iri = str(ontology_iri).rsplit("/", 1)[0]
new_iri = URIRef(f"{base_iri}/{base_name}-{new_version}.ttl")

# === Remove old version info ===
g.remove((ontology_iri, OWL.versionInfo, None))
g.remove((ontology_iri, DCTERMS.modified, None))
g.remove((ontology_iri, OWL.versionIRI, None))

# === Add updated version info ===
g.add((ontology_iri, OWL.versionInfo, Literal(new_version)))
g.add((ontology_iri, DCTERMS.modified, Literal(MODIFIED_DATE, datatype=XSD.date)))
g.add((ontology_iri, OWL.versionIRI, new_iri))

# === Write updated ontology ===
output_file = INPUT_FILE
g.serialize(destination=output_file, format="turtle")

# === Write different formats in latest ===
g.serialize(destination=f"{LATEST_DIR}/{base_name}.ttl", format="turtle")
g.serialize(destination=f"{LATEST_DIR}/{base_name}.nt", format="nt")
g.serialize(destination=f"{LATEST_DIR}/{base_name}.rdf", format="xml")
g.serialize(destination=f"{LATEST_DIR}/{base_name}.owl", format="xml")
g.serialize(destination=f"{LATEST_DIR}/{base_name}.jsonld", format="json-ld")
g.serialize(destination=f"{LATEST_DIR}/{base_name}.n3", format="n3")


# === Copy all triples from old IRI to new IRI ===
triples_to_copy = list(g.predicate_objects(subject=ontology_iri))
g.remove((ontology_iri, None, None))

# Add same triples to new ontology IRI
for p, o in triples_to_copy:
    g.add((new_iri, p, o))

if not os.path.exists(VERSION_DIR):
    os.makedirs(VERSION_DIR)
output_file = f"{VERSION_DIR}/{base_name}-{new_version}.ttl"
g.serialize(destination=output_file, format="turtle")



# === Report ===
print(f"Updated version: {current_version} → {new_version}")
print(f"New version IRI: {new_iri}")
print(f"Modified date set to: {MODIFIED_DATE}")
print(f"Updated ontology written to: {output_file}")
