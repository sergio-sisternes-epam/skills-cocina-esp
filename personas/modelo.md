---
type: decision
title: "Modelo de perfiles personales"
created: "2026-09-14"
work_id: "2026-09-14-cocina-atlas-schema"
status: settled
description: "Las preferencias y restricciones alimentarias pertenecen a personas concretas."
origin: user
sensitivity: internal
source_discussion: "github.com/sergio-sisternes-epam/discuss-atlas/cocina/person-contract.md"
relates_to:
  - path: work/2026-09-14-cocina-atlas-schema.md
    kind: implements
  - path: planificacion/modelo.md
    kind: related
---

## Decision

Cada persona tendrá nombre, preferencias, aversiones, alérgenos y nivel de
tolerancia o severidad cuando sea relevante. La evaluación familiar combinará
los perfiles de los comensales seleccionados.

## Consequences

Una receta puede ser adecuada para una persona y no para otra. Las
recomendaciones deben explicar qué perfil causa una exclusión y si una
sustitución puede resolverla.
