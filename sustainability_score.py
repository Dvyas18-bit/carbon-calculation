def calculate_sustainability_score(total_emission: float, num_items: int) -> int:
    """
    Calculates a sustainability score from 0 to 100 based on a defined baseline.
    Lower emissions mean higher score.
    """

    if num_items == 0:
        return 0

    average_emission_per_item = total_emission / num_items

    baseline = 5.0

    if average_emission_per_item == 0:
        score = 100

    elif average_emission_per_item >= (baseline * 2):
        score = 10

    else:
        score = 100 - (
            (average_emission_per_item / (baseline * 2)) * 100
        )

    return int(max(10, min(100, score)))


# Test the function
total_emission = 6.0
num_items = 3

score = calculate_sustainability_score(
    total_emission,
    num_items
)

print("Total Emission:", total_emission, "kg CO2e")
print("Number of Items:", num_items)
print("Sustainability Score:", score, "/100")
