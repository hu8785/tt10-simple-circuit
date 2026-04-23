import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    tests = [
        ((0, 0, 0), (1, 1)),
        ((0, 0, 1), (0, 0)),
        ((0, 1, 0), (1, 1)),
        ((0, 1, 1), (0, 0)),
        ((1, 0, 0), (1, 1)),
        ((1, 0, 1), (0, 0)),
        ((1, 1, 0), (1, 1)),
        ((1, 1, 1), (1, 0)),
    ]

    for (A, B, C), (f_exp, y_exp) in tests:
        dut.ui_in[0].value = A
        dut.ui_in[1].value = B
        dut.ui_in[2].value = C
        await ClockCycles(dut.clk, 2)

        assert dut.uo_out[0].value == f_exp, f"f failed for A={A}, B={B}, C={C}"
        assert dut.uo_out[1].value == y_exp, f"y failed for A={A}, B={B}, C={C}"
