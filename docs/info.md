## How it works

This project implements the combinational logic expression F = AB + C'.

Inputs:
- A
- B
- C

The circuit computes:
- e = A AND B
- y = NOT C
- f = e OR y = AB + C'

So the outputs are:
- f = final output
- y = complement of C

## How to test

Apply all 8 combinations of A, B, and C.

| A | B | C | f | y |
|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

## External hardware

None

## Pinout

### Inputs
- ui[0] = A
- ui[1] = B
- ui[2] = C

### Outputs
- uo[0] = f
- uo[1] = y
