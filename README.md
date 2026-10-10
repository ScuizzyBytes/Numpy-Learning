# 🐍 NumPy Learning Roadmap & Mini-Projects

Welcome to my **NumPy Learning** repository! 🚀  
Here I practice core Data Analysis techniques, array manipulations, statistical calculations, and logical data filtering using Python and `numpy`.

---

## 📌 Features & Topics Covered

- **Array Creation & Reshaping:** Working with multi-dimensional arrays (`np.array`, shapes, `axis` operations).
- **Logical Filtering & Boolean Masking:** Extracting specific data slices based on conditions using bitwise operators (`&`, `|`).
- **Statistical Operations:**
  - `np.mean()` — Calculating average values
  - `np.std()` — Standard deviation (data variance)
  - `np.var()` — Variance
  - `np.argmin()` / `np.argmax()` — Locating indices of minimum & maximum values
- **Data Manipulation & Replacement:**
  - `np.where()` — Conditional replacement and filtering
  - Python unpacking operator (`*`) for clean terminal outputs

---

## 💡 Code Example: Age Categorization & Data Filtering

```python
import numpy as np

# Sample dataset representing ages
ages = np.array([[122, 22, 13, 54, 35, 62, 47], [38, 18, 7, 0, 12, 23, 94]])

# Cleaning noise / anomalies (e.g., ages <= 0 or > 100)
cleaned_ages = np.where((ages <= 0) | (ages > 100), -1, ages)

# Categorization using Boolean Masking
teenagers = cleaned_ages[(cleaned_ages > 0) & (cleaned_ages < 18)]
adults = cleaned_ages[(cleaned_ages >= 18) & (cleaned_ages < 65)]
grands = cleaned_ages[cleaned_ages >= 65]

print("Kids:   ", *teenagers)
print("Adults: ", *adults)
print("Grands: ", *grands)
