---
type: work
title: "Diseñar el Atlas doméstico de cocina"
created: "2026-09-14"
work_id: "2026-09-14-cocina-atlas-schema"
status: in-discussion
description: "Trasladar y consolidar el modelo de recetas, ingredientes, inventario, utensilios y recomendaciones."
origin: user
sensitivity: internal
relates_to:
  - path: cocina/modelo-dominio.md
    kind: implements
  - path: recetas/modelo.md
    kind: implements
  - path: ingredientes/modelo.md
    kind: implements
  - path: inventario/modelo.md
    kind: implements
  - path: utensilios/modelo.md
    kind: implements
  - path: personas/modelo.md
    kind: implements
  - path: planificacion/modelo.md
    kind: implements
---

## Scope

Definir el modelo operativo del Atlas de cocina doméstica y preparar el terreno
para registrar recetas reales, compras y existencias.

## Status

Las decisiones de dominio están consolidadas. Las páginas de recetas,
ingredientes y existencias reales aún están por crear.

## Outcomes

El Atlas separa conocimiento culinario estable de estado doméstico cambiante y
conserva la trazabilidad hacia la discusión original en `discuss-atlas`.
