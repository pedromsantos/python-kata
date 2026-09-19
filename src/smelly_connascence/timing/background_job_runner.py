"""BackgroundJobRunner demonstrating Connascence of Timing."""

import asyncio
import threading


# Connascence of Timing: waiting a fixed, arbitrary delay instead of
# actually waiting on the job's completion -- correctness depends on the
# job finishing within 1000ms, a race condition disguised as a constant.
class BackgroundJobRunner:
    def __init__(self) -> None:
        self._job_result: str | None = None

    def start_job(self) -> None:
        threading.Timer(0.3, self._finish_job).start()

    def _finish_job(self) -> None:
        self._job_result = "done"

    async def wait_for_result(self) -> str | None:
        await asyncio.sleep(1)
        return self._job_result
