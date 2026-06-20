# Medical Record Validator

## 🎯 Overview
A modular, defensive data validation engine designed to enforce strict schema compliance and business-rule constraints on medical datasets. This utility ensures that incoming JSON-like dictionary structures meet pre-defined integrity standards before being processed by downstream systems.

## 🏗️ Technical Implementation
* **Schema Enforcement:** Uses set theory to validate that all required data keys (`patient_id`, `age`, `gender`, etc.) are present and no unauthorized keys exist.
* **Semantic Validation:** Employs `re` (Regular Expressions) for pattern matching and logic-gate constraints to ensure data values (e.g., age ranges, gender categories) are operationally valid.
* **Error Reporting:** Implements a granular error-reporting loop that identifies the exact location and nature of malformed data, enabling rapid debugging in production environments.

## 📂 Design Philosophy
* **Decoupled Logic:** The `find_invalid_records` function isolates business logic (constraints) from the structural validation, allowing for easy updates to rules without breaking the core validator.
* **Short-Circuit Evaluation:** Uses Python's native boolean logic (`and`/`or`) to optimize performance and prevent unnecessary checks on invalid objects.

## 🚀 Usage
```python
# Import the validation logic
from medical_validator import validate

# Example dataset
records = [{
    'patient_id': 'P1001',
    'age': 34,
    'gender': 'Female',
    'diagnosis': 'Hypertension',
    'medications': ['Lisinopril'],
    'last_visit_id': 'V2301'
}] 

# Run validation
if validate(records):
    print("System state: SECURE")
else:
    print("System state: INTEGRITY_FAILURE")