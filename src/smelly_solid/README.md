# SOLID Violations Kata

## Overview

This is a **verification fixture, not a practice exercise**. Each folder
contains a small, self-contained example of exactly one SOLID principle
violation, translated directly from *Agile Technical Practices Distilled*'s
SOLID chapter worked examples (Car/`save`, `CarEngineStatusReportController`,
`Chef`/`Oven`/`Microwave`, `IAmACar`, `Kitchen`/`MicrowaveOven`). Its purpose
is to give static-analysis/AI code-review tooling (specifically
[jev-review](https://github.com/pedromsantos/jev-review)) a known-answer set
to check its SOLID rules against -- every file's violation is deliberate and
documented below, not hidden.

This is the Python translation of the reference kata in ts-kata's
`25_SmellySolid`; equivalent kata exist for Go, Java, C#, and C too.

## What's here

| File | Violates | Why |
|---|---|---|
| `srp/car.py` | SRP | `save()` mixes a persistence concern into a class otherwise about domain behaviour (mileage/travel) |
| `ocp/*.py` | OCP (and DIP) | every new report format needs a new method on the controller, and it constructs its concrete views directly instead of receiving them injected |
| `lsp/microwave.py` | LSP | overrides `cook()` to raise instead of honouring the base contract |
| `lsp/chef.py` | -- | not itself a violation, but its `isinstance(oven, Microwave)` special-case is the client-code tell of `Microwave`'s LSP violation |
| `isp/i_am_a_car.py` | ISP | bundles `refill_gasoline`/`refill_electricity`, capabilities no single car supports both of |
| `isp/electric_car.py` | -- | the forced implementer: raises on the gasoline method it can't honestly support |
| `dip/kitchen.py` | DIP (and OCP) | constructs `MicrowaveOven` directly; can't work with any other oven without being edited |
| `dip/microwave_oven.py` | DIP | constructs `MicrowaveGenerator` directly instead of receiving it injected |
