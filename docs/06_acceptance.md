# Acceptance

The repository contains a reduced acceptance layer.

## It checks

- intake coverage against source files
- processing of files without an extension
- detected modality counts
- mapping target-class counts
- invalid target classes
- review totals
- split multi-target cases
- default-run behavior regarding target code generation

## Key idea

Acceptance here does not claim semantic perfection.
It verifies that the recovery baseline behaves within its declared public-safe rules.
