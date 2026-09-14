---
type: decision
title: "Modelo de utensilios"
created: "2026-09-14"
work_id: "2026-09-14-cocina-atlas-schema"
status: settled
description: "Los utensilios son entidades verificables por receta y paso."
origin: user
sensitivity: internal
source_discussion: "github.com/sergio-sisternes-epam/discuss-atlas/cocina/utensil-contract.md"
relates_to:
  - path: work/2026-09-14-cocina-atlas-schema.md
    kind: implements
  - path: recetas/modelo.md
    kind: related
---

## Decision

Cada utensilio tendrá nombre, categoría, capacidades o límites, disponibilidad
y posibles sustitutos. Los pasos de receta podrán declarar los utensilios que
requieren.

## Consequences

La evaluación de una receta distingue ingredientes faltantes de utensilios
faltantes y puede detectar incompatibilidades de capacidad.
