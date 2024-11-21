# TaiwanID

## Introduction

This is a package for Taiwan ID card number validation, generation and parsing.

## Installation

```bash
pip install taiwanid
```

## Usage

```python
from taiwanid import TaiwanID

# Validate Taiwan ID card number
id_number = 'A123456789'
print(TaiwanID.validate(id_number))
# out TaiwanID.ValidateStatus.SUCCESS

# Generate Taiwan ID card number
id_number = TaiwanID.generate()
print(id_number)
# out 'A123456789'

# Parse Taiwan ID card number
id_number = 'A123456789'
print(TaiwanID.parse(id_number))
# out TODO
```

---

```bash
pip install -e .
```
