---
type: decision
title: "Modelo de inventario y despensa"
created: "2026-09-14"
work_id: "2026-09-14-cocina-atlas-schema"
status: settled
description: "La despensa se deriva de eventos inmutables y conserva cantidades, ubicaciones y fechas."
origin: user
sensitivity: internal
source_discussion: "github.com/sergio-sisternes-epam/discuss-atlas/cocina/immutable-inventory-history.md"
relates_to:
  - path: work/2026-09-14-cocina-atlas-schema.md
    kind: implements
  - path: ingredientes/modelo.md
    kind: follows
  - path: planificacion/modelo.md
    kind: related
---

## Decision

Una existencia concreta será un registro ligado a una compra o producción.
Conservará cantidad, unidad, ubicación, lote cuando exista, fecha de compra,
fecha de elaboración, caducidad y consumo preferente. Podrá promoverse a
página si acumula historial propio.

Los cambios se expresarán mediante eventos inmutables de compra, consumo,
producción, desperdicio, ajuste manual y traslado. Los errores se corrigen con
nuevos ajustes, no editando el historial.

Las sobras y preparaciones intermedias son existencias preparadas con cantidad,
elaboración y caducidad propias. La lista de compra calcula el déficit exacto
después de descontar existencias; los formatos comerciales se dejan para una
fase posterior.

## Consequences

El estado actual puede reconstruirse y explicarse desde el historial. Las
recomendaciones priorizan productos próximos a caducar y no recomiendan
automáticamente productos caducados.
