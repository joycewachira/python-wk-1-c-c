# Define the conversion function
def convert_to_24_hour(hour, minute, period):
    if period == "pm":
        hour = (hour + 12) % 24 if hour != 12 else 12
    else:
        hour = hour % 12

    return f"{hour:02d}{minute:02d}"

# Example usage
input_hour = 1
input_minute = 30
input_period = "am"

result = convert_to_24_hour(input_hour, input_minute, input_period)
print("Converted 24-hour time:", result)
