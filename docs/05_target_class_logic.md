# Target class logic

The workbench maps recovered results into a deliberately small stable class set.

## Stable classes

- `discord`
- `bot`
- `repo`
- `review_required`

## Why the set stays small

A recovery workbench should not silently invent a growing ontology from weak hints.
Stable classes make review, reporting, and later downstream planning easier.

## Mapping principle

One source may map to multiple stable classes.
This is not treated as a failure by itself.
It becomes review-relevant when overlap or ambiguity remains unresolved.
