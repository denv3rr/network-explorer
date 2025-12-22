# outbound_testing.py
# Orchestrates outbound-facing tests (web/DNS/HTTP) with safe defaults.

from typing import Any, Dict, Optional

from pentest_tools import run_pentest_suite


def run_outbound_suite(
    target_input: str,
    *,
    aggressive: bool = False,
    rate_limit: Optional[float] = None,
    allow_external: bool = False,
) -> Dict[str, Any]:
    """
    Wrapper for outbound testing features. Safe by default.
    """
    report = {}
    safe_rate = 0.5 if rate_limit is None else rate_limit
    report["_meta"] = {"active": aggressive, "external": allow_external, "rate_limit": safe_rate}
    report["webdns"] = run_pentest_suite(
        target_input,
        aggressive=aggressive,
        rate_limit=safe_rate,
        allow_external=allow_external,
    )
    return report
