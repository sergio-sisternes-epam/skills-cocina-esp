---
type: decision
title: "Modelo de dominio de cocina doméstica"
created: "2026-09-14"
work_id: "2026-09-14-cocina-atlas-schema"
status: settled
description: "El Atlas separa conocimiento culinario estable de estado doméstico cambiante."
origin: user
sensitivity: internal
source_discussion: "github.com/sergio-sisternes-epam/discuss-atlas/cocina/hub.md"
relates_to:
  - path: work/2026-09-14-cocina-atlas-schema.md
    kind: implements
  - path: recetas/modelo.md
    kind: related
  - path: inventario/modelo.md
    kind: related
---

## Decision

El dominio tiene dos capas:

1. **Conocimiento culinario:** recetas, ingredientes conceptuales, cantidades,
   pasos, técnicas, utensilios, sustituciones y procedencia.
2. **Estado doméstico:** existencias, compras, consumos, producciones,
   desperdicios, ubicaciones y fechas.

La planificación de comidas y la lista de compra son capacidades derivadas de
ambas capas, no entidades nucleares iniciales.

## Consequences

El núcleo se mantiene pequeño y puede responder qué cocinar ahora, qué falta y
qué productos conviene aprovechar sin mezclar definiciones estables con
cantidades cambiantes.
