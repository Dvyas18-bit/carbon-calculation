def normalize_quantity(quantity: float, item_unit: str, factor_unit: str) -> float:
    """
    Converts the product quantity into the unit used by the emission factor.

    Example:
    500 G with factor per KG
    500 G = 0.5 KG
    """

    # Check for missing units
    if not item_unit or not factor_unit:
        raise ValueError("Item unit or factor unit is missing.")

    item_unit = item_unit.strip().upper()
    factor_unit = factor_unit.strip().upper()

    # Convert factor unit into a simple base unit
    if "KG" in factor_unit:
        base_factor_unit = "KG"
    elif "G" in factor_unit:
        base_factor_unit = "G"
    elif "ML" in factor_unit:
        base_factor_unit = "ML"
    elif "L" in factor_unit:
        base_factor_unit = "L"
    else:
        base_factor_unit = factor_unit

    # If both units are already the same
    if item_unit == base_factor_unit:
        return quantity

    # Gram -> Kilogram
    if item_unit == "G" and base_factor_unit == "KG":
        return quantity / 1000

    # Kilogram -> Gram
    if item_unit == "KG" and base_factor_unit == "G":
        return quantity * 1000

    # Millilitre -> Litre
    if item_unit == "ML" and base_factor_unit == "L":
        return quantity / 1000

    # Litre -> Millilitre
    if item_unit == "L" and base_factor_unit == "ML":
        return quantity * 1000

    # If conversion is not available
    raise ValueError(
        f"Cannot convert {item_unit} to {base_factor_unit}"
    )


def calculate_emission(
    quantity: float,
    item_unit: str,
    emission_factor: float,
    factor_unit: str
) -> float:
    """
    Calculates carbon emission.

    Formula:
    Emission = Normalized Quantity × Emission Factor
    """

    normalized_qty = normalize_quantity(
        quantity,
        item_unit,
        factor_unit
    )

    emission = normalized_qty * emission_factor

    return emission


# -------------------------------
# TESTING
# -------------------------------

if __name__ == "__main__":

    # Example 1
    quantity = 500
    item_unit = "G"
    emission_factor = 2.0
    factor_unit = "KG"

    emission = calculate_emission(
        quantity,
        item_unit,
        emission_factor,
        factor_unit
    )

    print("Product Quantity:", quantity, item_unit)
    print("Emission Factor:", emission_factor, "kg CO2e per", factor_unit)
    print("Carbon Emission:", emission, "kg CO2e")


    # Example 2
    quantity = 2
    item_unit = "KG"
    emission_factor = 2.0
    factor_unit = "KG"

    emission = calculate_emission(
        quantity,
        item_unit,
        emission_factor,
        factor_unit
    )

    print("\nProduct Quantity:", quantity, item_unit)
    print("Emission Factor:", emission_factor, "kg CO2e per", factor_unit)
    print("Carbon Emission:", emission, "kg CO2e")
