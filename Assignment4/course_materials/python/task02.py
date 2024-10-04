# -*- coding: utf-8 -*-
"""Task02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wrpjuk9LC4DCUYzfLQvecw9IFaRz_u_A

**Task 02: Managing statements**

Comenzamos con un grafo vacío
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4"

from rdflib import Graph, Namespace, Literal
g = Graph()

"""Creamos el recurso John Smith con su nombre completo"""

fullName = Literal("John Smith")
EX = Namespace("http://example.org/")
johnURI = EX.JohnSmith

"""Generamos la sentencia añadiendo el predicado (propiedad)"""

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

resource = (johnURI, VCARD.FN, fullName)

print(resource)

g.add(resource)

"""Creamos otro recurso para Jane con su nombre completo e email

Podemos abreviar un poco lo que hemos hecho en la tarea anterior, atención a los dobles paréntesis, add() acepta un solo parámetro en forma de tupla, no 3 parámetros.
"""

g.add((EX.JaneSmith, VCARD.FN, Literal("Jane Smith")))
g.add((EX.JaneSmith, VCARD.hasEmail, Literal("jsmith@example.org")))

"""Añadimos una relación entre John y Jane mediante el vocabulario FOAF

Hay ciertos espacios de nombres que son nativos a RDFlib, FOAF es uno de ellos y no hace falta que lo declaremos nosotros
"""

from rdflib import FOAF

g.add((EX.JohnSmith, FOAF.knows, EX.JaneSmith))

"""Vemos el resultado conjunto"""

print(g.serialize(format="ttl").decode("UTF-8"))