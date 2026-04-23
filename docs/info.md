---

## How it works

This project implements the combinational logic circuit **F = AB + C'** using basic Verilog gate primitives.

The circuit has three inputs: A, B, and C, and one output F.

Logic implementation:
- An AND gate (g1) computes AB from inputs A and B
- A NOT gate (g2) computes C' (complement of C)
- An OR gate (g3) computes F = AB + C'

Truth Table:

| A | B | C | F = AB + C' |
|---|---|---|-------------|
| 0 | 0 | 0 | 1           |
| 0 | 0 | 1 | 0           |
| 0 | 1 | 0 | 1           |
| 0 | 1 | 1 | 0           |
| 1 | 0 | 0 | 1           |
| 1 | 0 | 1 | 0           |
| 1 | 1 | 0 | 1           |
| 1 | 1 | 1 | 1           |

Pinout:
- ui[0] = A (input)
- ui[1] = B (input)
- ui[2] = C (input)
- uo[0] = F (output)

## How to test

Apply all 8 combinations of inputs A, B, C and verify the output F matches the truth table above.

For example:
- A=0, B=0, C=0 → F=1 (C'=1, AB=0, so F=1)
- A=1, B=1, C=1 → F=1 (AB=1, so F=1)
- A=0, B=0, C=1 → F=0 (C'=0, AB=0, so F=0)

## External hardware

None
