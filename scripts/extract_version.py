import rdflib
import re

OWL_FILE = "sulo.ttl"
OUTPUT_SVG = "version.svg"

g = rdflib.Graph()
g.parse(OWL_FILE)

# Extract versionIRI or owl:versionInfo
version = None
for s, p, o in g.triples((None, rdflib.OWL.versionInfo, None)):
    version = str(o)
    break

if not version:
    print("::error::No owl:versionInfo found.")
    exit(1)

# Write badge using shields.io format
with open(OUTPUT_SVG, "w") as f:
    f.write(f"""<svg xmlns="http://www.w3.org/2000/svg" width="120" height="20">
  <rect width="60" height="20" fill="#555"/>
  <rect x="60" width="60" height="20" fill="#4c1"/>
  <text x="30" y="14" fill="#fff" font-family="Verdana" font-size="11" text-anchor="middle">version</text>
  <text x="90" y="14" fill="#fff" font-family="Verdana" font-size="11" text-anchor="middle">{version}</text>
</svg>""")