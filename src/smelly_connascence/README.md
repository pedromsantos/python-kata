# Connascence Violations Kata

## Overview

This is a **verification fixture, not a practice exercise**. Each folder
contains a small, self-contained example of exactly one Connascence type,
translated directly from *Agile Technical Practices Distilled*'s
Connascence chapter worked examples. Its purpose is to give a known-answer
set for [jev-review](https://github.com/pedromsantos/jev-review)'s upcoming
Connascence rules to be verified against before those rules are implemented.

`CoV` (Connascence of Value) is intentionally not represented -- already
covered by jev-review's existing checks. `CoMT` (Connascence of Manual
Task) is intentionally not represented either -- it's connascence with an
external, undocumented manual step no code review can see.

This is the Python translation of the reference kata in ts-kata's
`26_SmellyConnascence`; equivalent kata exist for Go, Java, C#, and C.

## What's here

| File | Type | Why |
|---|---|---|
| `position/notification_system.py` | Connascence of Position | three same-typed `str` parameters carry meaning only through argument order |
| `meaning/transport_selector.py` | Connascence of Meaning | `"1"`/`"2"`/`"3"`/`"4"` mean bike/car/train/bus only by an unstated, shared convention |
| `algorithm/checksum_calculator.py` | Connascence of Algorithm | the checksum computation (`sum % 10`) is duplicated across two methods instead of extracted once |
| `execution_order/receipt_sender.py` | Connascence of Execution Order | `archive()` is only correct after `send_to_customer()`, but nothing enforces that order |
| `timing/background_job_runner.py` | Connascence of Timing | waits a fixed, arbitrary delay instead of the job's actual completion |
| `identity/global_counter.py` + `identity/counter_consumer.py` | Connascence of Identity | every consumer's correctness depends on sharing this exact module-level instance |
