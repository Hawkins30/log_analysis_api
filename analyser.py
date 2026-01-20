def analyse_log_lines(lines):
    valid_levels = ["ERROR", "WARNING", "INFO"]
    counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}
    malformed_lines = 0

    for line in lines:
        parts = line.split(" ")

        if len(parts) < 4:
            malformed_lines += 1
            continue

        level = parts[2]

        if level not in valid_levels:
            malformed_lines += 1
            continue

        counts[level] += 1

    return counts, malformed_lines
