from analyser import analyse_log_lines


def test_analyse_log_lines_basic():
    lines = [
        "2026-01-12 14:33:01 ERROR Something failed",
        "INVALID LINE",
        "2026-01-12 14:33:02 INFO All good"
    ]

    counts, malformed = analyse_log_lines(lines)

    assert counts["ERROR"] == 1
    assert counts["WARNING"] == 0
    assert counts["INFO"] == 1
    assert malformed == 1
