---
type: decision
title: "Modelo de ingredientes"
created: "2026-09-14"
work_id: "2026-09-14-cocina-atlas-schema"
status: settled
description: "Los ingredientes conceptuales tienen identidad estable y se separan de sus existencias concretas."
origin: user
sensitivity: internal
source_discussion: "github.com/sergio-sisternes-epam/discuss-atlas/cocina/ingredient-contract.md"
relates_to:
  - path: work/2026-09-14-cocina-atlas-schema.md
    kind: implements
  - path: recetas/modelo.md
    kind: related
  - path: inventario/modelo.md
    kind: follows
---

## Decision

Cada ingrediente conceptual tendrá nombre canónico, sinónimos, categoría,
unidades válidas, alérgenos, sustituciones relacionadas y equivalencias
específicas cuando una conversión dependa del producto o de su presentación.

Las unidades canónicas iniciales son `g`, `kg`, `ml`, `l`, `unidad`, `envase` y
`ración`. Las conversiones ambiguas deben conservar contexto y no imponerse
como reglas universales.

## Consequences

“Tomate” puede ser una identidad reutilizable aunque las recetas usen
sinónimos. La disponibilidad se calcula sobre existencias reales, no sobre la
ficha conceptual.
