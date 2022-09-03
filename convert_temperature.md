# **`convert_temperature`**

Specification file for `convert_temperature` function.

<br>

## 1. Requirements
---

### 1.1 ID
---
> f_005

<br>

### 1.2 Signature
---
> `t_2 = convert_temperature(t_i, s_i, s_o)`

<br>

### 1.3 Type and language
---
> Python function

<br>

### 1.4 Purpose
---
> Convert temperature between the following scales: celsius, farenheit and kelvin

<br>

### 1.5 Inputs
---

| Input | Description | Type & Domain |
|---|---|---|
| `t_i` | Tempareture input | *real number* <br> `int/float`
| `s_i` | Scale input | *string* <br> `str`
| `s_o` | Scale output | *string* <br> `str`

<br>

### 1.6 Outputs
---
| Output | Description | Type & Domain |
|---|---|---|
| `t_o` | Temparature output | *real number* <br> `int/float` |

<br>

## 1. Test cases
---

| Id | `t_i` | `s_i` | `s_o` | Output expected |
|---|---|---|---|---|
| 1 | `None` | `None` | `None` | None |
| 2 | `25` | `CELSIUS` | `FAHRENHEIT` | 77.0 |
| 3 | `25` | `CELSIUS` | `FAHRENHEITT` | None |
| 4 | `25` | `CELSIUS` | `None` | None |
| 5 | `-273` | `CELSIUS` | `KELVIN` | 0.15 |

<br>

## 2. Algorithm
---
 ![Algorithm](f_005_algorithm.drawio.png)






