---
type: decision
title: "Modelo de recetas"
created: "2026-09-14"
work_id: "2026-09-14-cocina-atlas-schema"
status: settled
description: "Las recetas son páginas estructuradas con entradas, salidas, pasos, rendimiento y procedencia."
origin: user
sensitivity: internal
source_discussion: "github.com/sergio-sisternes-epam/discuss-atlas/cocina/recipe-contract.md"
relates_to:
  - path: work/2026-09-14-cocina-atlas-schema.md
    kind: implements
  - path: cocina/modelo-dominio.md
    kind: follows
  - path: ingredientes/modelo.md
    kind: related
  - path: utensilios/modelo.md
    kind: related
---

## Decision

Cada receta tendrá nombre, descripción, raciones, tiempo, dificultad,
alérgenos, ingredientes estructurados, pasos ordenados, utensilios y
clasificación por categorías, etiquetas, técnicas y tipo de comida.

Cada ingrediente de una receta declarará cantidad, unidad, opcionalidad y
posibles sustituciones. Los pasos podrán declarar técnica, duración,
temperatura y utensilios.

Las recetas tendrán entradas y salidas explícitas. Una receta puede consumir
ingredientes o existencias y producir raciones, salsas, masas, caldos u otras
preparaciones. Se conservarán rendimiento esperado, autoría, procedencia y
versiones.

## Consequences

Una receta puede escalarse por raciones, producir existencias reutilizables y
ser evaluada tanto por disponibilidad como por tiempo, dificultad, utensilios y
restricciones alimentarias.
