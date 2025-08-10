[![Syntax checking](https://github.com/AIDAVA-DEV/sulo/actions/workflows/syntax_check.yml/badge.svg)](https://github.com/AIDAVA-DEV/sulo/actions/workflows/syntax_check.yml)
[![Ontology Reasoning](https://github.com/AIDAVA-DEV/sulo/actions/workflows/reasoning.yml/badge.svg)](https://github.com/AIDAVA-DEV/sulo/actions/workflows/reasoning.yml)
[![Ontology Documentation](https://github.com/AIDAVA-DEV/sulo/actions/workflows/documentation.yml/badge.svg)](https://github.com/AIDAVA-DEV/sulo/actions/workflows/documentation.yml)
[![pages-build-deployment](https://github.com/AIDAVA-DEV/sulo/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/AIDAVA-DEV/sulo/actions/workflows/pages/pages-build-deployment)
[![FOOPS!](https://github.com/AIDAVA-DEV/sulo/actions/workflows/foops-scan.yml/badge.svg)](https://github.com/AIDAVA-DEV/sulo/actions/workflows/foops-scan.yml)
[![FOOPS! score](https://raw.githubusercontent.com/AIDAVA-DEV/sulo/refs/heads/main/foops-badge.svg)](https://github.com/AIDAVA-DEV/sulo/actions/workflows/foops-scan.yml)


# Simplified Upper Level Ontology (SULO)

SULO offers a minimal set of classes and relations to guide the representation of knowledge in RDF/OWL.

The Ontology IRI is : [https://w3id.org/sulo/](https://w3id.org/sulo/)

![Ontology Version](version.svg)

Here's the SULO Postcard showing all the classes and relations (solid line indicates connection between domain/range; dotted line indicates restriction on use in class axiom)<br>
<img src="sulo-overview.png" alt="SULO Postcard" width="800">

The ontology is available in a number of formats:
* [Turtle](https://w3id.org/sulo/sulo.ttl)
* [RDF/XML](https://w3id.org/sulo/sulo.owl)
* [JSON-LD](https://w3id.org/sulo/sulo.jsonld)
* [NTriples](https://w3id.org/sulo/sulo.nt)

You can retrieve any of these through content type negotiation
```
curl -L -H "Accept: text/turtle https://w3id.org/sulo
curl -L -H "Accept: application/ld+json" https://w3id.org/sulo
curl -L -H "Accept: application/rdf+xml" https://w3id.org/sulo
curl -L -H "Accept: application/n-triples" https://w3id.org/sulo
```

In addition, individual versions of SULO are available through the ontology IRI pattern ```https://w3id.org/sulo/sulo-X.X.X.ttl```  All versions of the ontology are available from [github](versions/)

Documentation for SULO is available using:
* [OntoSpy](https://aidava-dev.github.io/sulo/ontospy/index.html)
* [Pylode](https://aidava-dev.github.io/sulo/pylode/index.html)

FAIRness assessment performed with [FOOPS!](https://foops.linkeddata.es/FAIR_validator.html)




