def parse_log_line(line):

    parts = line.split(" ", 2)

    timestamp = parts[0] + " " + parts[1]
    rest = parts[2]

    if "ERROR" in rest:
        level = "ERROR"
    elif "WARNING" in rest:
        level = "WARNING"
    else:
        level = "INFO"

    message = rest.replace(level, "").strip()

    return{
        "timestamp": timestamp,
        "level": level,
        "message": message
    }