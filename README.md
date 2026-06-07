# 🔢 Matrix Inverse Calculator

> A pure-Python tool for computing the inverse of any square matrix (up to 10×10).  
> Implements determinant calculation, cofactor matrix, and adjugate — from scratch, no libraries.

![Python](https://img.shields.io/badge/Language-Python-blue)
![Math](https://img.shields.io/badge/Topic-Linear%20Algebra-purple)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 🧠 How It Works

The inverse is computed using the classical adjugate method:

```
A⁻¹ = (1 / det(A)) × adj(A)
```

| Step | Function | Description |
|---|---|---|
| 1 | `determinant()` | Recursive cofactor expansion along the first row |
| 2 | `small_matrix()` | Extracts the (n−1)×(n−1) submatrix by removing a row and column |
| 3 | `alhagi_matrix()` | Builds the cofactor matrix with alternating signs |
| 4 | `tranahade()` | Transposes the cofactor matrix to get the adjugate |
| 5 | `reverse_matrix()` | Divides every element of the adjugate by det(A) |

---

## 🖥️ Usage

### Run

```bash
python matrix.py
```

### Example — 3×3 matrix

```
please enter numbers row to row(0<n<11): 3
1: 1 2 3
2: 0 1 4
3: 5 6 0
determinant: 1.0
reverse matrix:
-24.0 18.0 5.0
20.0 -15.0 -4.0
-5.0 4.0 1.0
```

---

## ✅ Input Validation

| Check | Message |
|---|---|
| `n` outside 1–10 | `this number is not acceptable.` |
| Wrong number of elements in a row | `the number of elements is wrong` |
| Non-numeric input | `you should enter numbers.` |
| `det(A) = 0` | `determinant is 0 and It doesn't have reverse matrix` |

The program re-prompts on every invalid input — no crashes.

---

## 📐 Supported Matrix Sizes

| Size | Supported |
|---|---|
| 1×1 | ✅ |
| 2×2 | ✅ (direct formula) |
| 3×3 to 10×10 | ✅ (recursive cofactor expansion) |
| Singular matrix (det = 0) | ⚠️ Detected and reported |

---

## 📁 Project Structure

```
matrix-inverse/
└── matrix.py     # All matrix operations + input handling
```

---

## ⚠️ Note

For large matrices (n ≥ 8), recursive cofactor expansion becomes slow due to O(n!) time complexity. For performance-critical use cases, consider `numpy.linalg.inv()`.

---

## 👩‍💻 Author

**Sepideh Pashayan** 
