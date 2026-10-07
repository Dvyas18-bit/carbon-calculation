# carbon-calculation
Carbon Calculation & Sustainability Score

Overview

This module is responsible for two main parts of the project:

1. Carbon Emission Calculation
2. Sustainability Score Calculation

The carbon calculation module first converts the product quantity into the same unit used by the emission factor. It then calculates the carbon emission.

The sustainability score module uses the total carbon emission and number of items to calculate a score from 10 to 100.

---

My Contribution

I worked on the Carbon Calculation and Sustainability Score module.

Responsibilities

- Normalize product quantities and units
- Convert grams to kilograms
- Convert kilograms to grams
- Convert millilitres to litres
- Convert litres to millilitres
- Calculate carbon emissions
- Handle missing or unsupported units
- Calculate the sustainability score
- Test the calculation functions

---

1. Carbon Emission Calculation

The carbon calculation is implemented using two functions:

normalize_quantity()
calculate_emission()

"normalize_quantity()"

This function converts the product quantity into the unit required by the emission factor.

Function

normalize_quantity(quantity, item_unit, factor_unit)

Parameters

Parameter| Description
"quantity"| Quantity of the product
"item_unit"| Unit of the product quantity
"factor_unit"| Unit used by the emission factor

Supported conversions

G → KG
KG → G
ML → L
L → ML

Example

If a product has:

Quantity = 500 G
Emission Factor Unit = KG

The function converts:

500 G ÷ 1000 = 0.5 KG

Therefore, the normalized quantity becomes:

0.5 KG

---

2. Carbon Emission Calculation

The "calculate_emission()" function calculates the carbon emission after normalizing the quantity.

Function

calculate_emission(
    quantity,
    item_unit,
    emission_factor,
    factor_unit
)

Formula

Carbon Emission = Normalized Quantity × Emission Factor

Example

Given:

Quantity = 500 G
Emission Factor = 2.0 kg CO2e per KG

First:

500 G = 0.5 KG

Then:

Carbon Emission = 0.5 × 2.0
                = 1.0 kg CO2e

Output

Carbon Emission: 1.0 kg CO2e

---

3. Error Handling

The module also handles invalid or missing units.

If the item unit or factor unit is missing, the function raises:

ValueError: Item unit or factor unit is missing.

If a conversion is not supported, the function raises an error such as:

ValueError: Cannot convert G to L

This prevents the system from performing an incorrect emission calculation.

---

4. Sustainability Score

The sustainability score is calculated using:

calculate_sustainability_score(total_emission, num_items)

The function uses the average emission per item.

Step 1: Calculate average emission

Average Emission per Item =
Total Emission / Number of Items

Step 2: Compare with baseline

The baseline used in the code is:

Baseline = 5.0

The code uses twice the baseline as the upper emission limit:

5.0 × 2 = 10.0

If the average emission is higher than or equal to "10.0", the score becomes:

10

If the average emission is zero, the score becomes:

100

For values between these limits, the score decreases as average emissions increase.

---

5. Score Range

The final score is restricted between:

Minimum Score = 10
Maximum Score = 100

Therefore:

Higher emission → Lower score
Lower emission → Higher score

A score of "100" represents the lowest emission condition handled by the formula, while "10" is the minimum score allowed by the calculation.

---

6. Example Sustainability Score

The test case in the code uses:

Total Emission = 6.0 kg CO2e
Number of Items = 3

Average emission:

6.0 / 3 = 2.0 kg CO2e per item

Using the baseline of "5.0", the sustainability score is calculated by the implemented formula.

The program then prints:

Total Emission: 6.0 kg CO2e
Number of Items: 3
Sustainability Score: 80 /100

---

7. Project Workflow

The two modules can be used in the following workflow:

Bill Data
   ↓
Product Quantity & Unit
   ↓
Unit Normalization
   ↓
Normalized Quantity
   ↓
Emission Factor
   ↓
Carbon Emission
   ↓
Total Carbon Emission
   ↓
Number of Items
   ↓
Sustainability Score

---

8. Files

The contribution contains the following main functionality:

Carbon Calculation
│
├── normalize_quantity()
│       └── Converts product units
│
└── calculate_emission()
        └── Calculates carbon emission


Sustainability Score
│
└── calculate_sustainability_score()
        └── Calculates score from emission and number of items

---

9. Testing

Both modules contain test examples to verify that the functions work correctly.

Carbon Calculation Test 1

Quantity = 500 G
Emission Factor = 2.0 kg CO2e/KG

Result = 1.0 kg CO2e

Carbon Calculation Test 2

Quantity = 2 KG
Emission Factor = 2.0 kg CO2e/KG

Result = 4.0 kg CO2e

Sustainability Score Test

Total Emission = 6.0 kg CO2e
Number of Items = 3

Result = 80 / 100

---

10. Technologies Used

- Python
- Python functions
- Floating-point calculations
- Unit conversion
- Carbon emission calculations
- Error handling

---

Conclusion

This module provides the calculation layer for the project's carbon footprint analysis. It ensures that product quantities are converted into compatible units before calculating emissions and then uses the resulting emissions to generate a sustainability score.

The implementation focuses on simple, transparent, and reproducible calculations so that the carbon emission and sustainability score can be understood and verified easily.
