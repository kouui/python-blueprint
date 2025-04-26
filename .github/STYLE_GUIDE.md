# Coding Style Guide

This document outlines coding standards for our project.

## Python

### Formatting
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters
- Use trailing commas in multi-line structures

### Naming
- Variables and functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private members: prefix with underscore `_private_var`

### Strings
- Use double quotes (`"`) for dict keys and regular strings
- Use single quotes (`'`) for single characters
- Use triple double quotes (`"""`) for docstrings and multi-line strings
- for long strings, use parentheses to break them into multiple lines

### Comments
- Use `"""` for docstrings for modules, classes, and functions
- Use `"""` for explaining (the purpose of) complex code blocks
- Use `#` for inline comments (right after some code) and commenting out code
- Include type hints in function definitions

### Error Handling
- Always use try/except blocks for operations that may fail
- Specify exact exception types when catching exceptions
- Include logging for exceptions