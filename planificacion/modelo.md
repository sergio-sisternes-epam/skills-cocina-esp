---
type: decision
title: "Modelo de recomendaciones y planificación"
created: "2026-09-14"
work_id: "2026-09-14-cocina-atlas-schema"
status: settled
description: "La primera capacidad de planificación es recomendar qué cocinar ahora aprovechando caducidades."
origin: user
sensitivity: internal
source_discussion: "github.com/sergio-sisternes-epam/discuss-atlas/cocina/planning-goal.md"
relates_to:
  - path: work/2026-09-14-cocina-atlas-schema.md
    kind: implements
  - path: inventario/modelo.md
    kind: follows
  - path: personas/modelo.md
    kind: related
---

## Decision

La primera prioridad es identificar recetas cocinables con lo disponible y
aprovechar productos próximos a caducar. Las recomendaciones considerarán
tiempo, dificultad, preferencias y alérgenos.

La lista de compra se deriva como déficit exacto para una receta o menú. La
planificación semanal y los formatos comerciales quedan fuera de la primera
versión.

## Consequences

La recomendación no solo pregunta si hay ingredientes: también comprueba
cantidades, sustituciones, utensilios, seguridad alimentaria y perfiles de los
comensales.
