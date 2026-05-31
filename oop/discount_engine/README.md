# Discount Engine (Strategy Pattern)

## Overview
This module implements the **Strategy Design Pattern**, a behavioral pattern that enables selecting an algorithm at runtime. Instead of hard-coding discount logic into the `Product` or `Engine` classes, the `DiscountEngine` acts as an orchestrator that delegates calculations to concrete strategy classes.

## Architectural Design
- **Abstraction Layer:** `DiscountStrategy` (Abstract Base Class) defines the contract (`is_applicable` and `apply_discount`) that all concrete strategies must fulfill.
- **Implementation Layer:** Concrete classes (`PercentageDiscount`, `FixedAmountDiscount`, `PremiumUserDiscount`) encapsulate specific pricing algorithms.
- **Engine Layer:** `DiscountEngine` manages a list of strategies and optimizes price calculation via the `calculate_best_price` method.

## Key Features
- **Scalability:** New discount types can be added by simply creating a new subclass of `DiscountStrategy` without modifying the `DiscountEngine` or existing product logic.
- **Decoupling:** Business rules (discounts) are separated from the data model (`Product`).
- **Safety:** The `abc` (Abstract Base Class) module enforces the implementation of required methods, preventing runtime crashes due to missing logic.

## Usage
```python
# Initialize strategies
strategies = [
    PercentageDiscount(10),
    FixedAmountDiscount(5),
    PremiumUserDiscount()
]

# Initialize engine
engine = DiscountEngine(strategies)

# Calculate optimal price
best_price = engine.calculate_best_price(product, user_tier)
