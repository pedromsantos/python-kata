from datetime import UTC, datetime


class OrderClock:
    @staticmethod
    def now_static() -> str:
        return datetime.now(UTC).isoformat()

    def now(self) -> str:
        return OrderClock.now_static()
