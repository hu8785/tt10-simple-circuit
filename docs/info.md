## How it works

This project implements the combinational logic expression F = AB + C'.

Inputs:
- A
- B
- C

The circuit first computes:
- e = A AND B
- y = NOT C

Then it computes:
- f = e OR y = AB + C'

So:
- f is the final output
- y is the complement of C

## How to test

Apply all 8 input combinations and verify the outputs:

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
