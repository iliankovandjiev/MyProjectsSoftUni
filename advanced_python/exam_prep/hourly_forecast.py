def forecast(*weather):
    data_to_display = []
    total_data = sorted(weather, key=lambda x: ((x[1] == "Rainy", x[1] == "Cloudy", x[1] == "Sunny"), x[0]))
    for data in total_data:
        data_to_display.append(f"{data[0]} - {data[1]}")

    return "\n".join(data_to_display)

