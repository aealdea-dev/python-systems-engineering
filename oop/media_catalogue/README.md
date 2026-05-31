# Media Catalogue System

## Overview
This module provides a structured, object-oriented approach to managing a collection of media items, specifically `Movie` and `TVSeries` objects. It demonstrates core principles of object-oriented programming, including inheritance, validation, and error handling.

## Architectural Design
- **Base Model (`Movie`):** Serves as the blueprint for all media items. It implements strict input validation (e.g., checking for non-empty titles, valid release years, and positive durations) to ensure data integrity.
- **Inheritance (`TVSeries`):** Extends the `Movie` class, inheriting core attributes while adding series-specific metadata (`seasons` and `total_episodes`).
- **Catalogue Manager (`MediaCatalogue`):** Acts as a container for media objects, providing categorized retrieval (`get_movies`, `get_tv_series`) and a formatted summary of the entire collection.
- **Exception Handling (`MediaError`):** A custom exception class designed to track specifically where and why a media-related operation fails, including a reference to the offending object.

## Key Features
- **Data Integrity:** Ensures no invalid media data (e.g., negative episodes, years before cinema inception) enters the system.
- **Categorization:** Uses Python's `isinstance` checks to intelligently differentiate between movies and television series within the same collection.
- **Readable Summaries:** The `__str__` methods provide clear, structured representations of both individual media items and the catalogue as a whole.

## Class Hierarchy

* `Movie` (Parent)
    * `TVSeries` (Child)

## Usage Example
```python
catalogue = MediaCatalogue()

# Adding a movie
movie = Movie('The Matrix', 1999, 'The Wachowskis', 136)
catalogue.add(movie)

# Adding a TV series
series = TVSeries('Scrubs', 2001, 'Bill Lawrence', 24, 9, 182)
catalogue.add(series)

# Displaying catalogue
print(catalogue)