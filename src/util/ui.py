def get_health_bar(value, max_value, width):
    health_bar = "|"
    filled = int(value / max_value * width)
    for i in range(filled):
        health_bar += "#"

    for i in range(width - filled):
        health_bar += "-"
    health_bar += "|"
    return health_bar