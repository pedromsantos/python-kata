"""CounterConsumer relies on the shared module-level global_counter."""

from smelly_connascence.identity.global_counter import global_counter


class CounterConsumer:
    def record_visit(self) -> int:
        return global_counter.increment()

    def total_visits(self) -> int:
        return global_counter.current()
