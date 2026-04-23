# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior - F = AB + C'")

    # A=0, B=0, C=0 -> F=1 (C'=1)
    dut.ui_in[0].value = 0
    dut.ui_in[1].value = 0
    dut.ui_in[2].value = 0
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 1

    # A=0, B=0, C=1 -> F=0
    dut.ui_in[0].value = 0
    dut.ui_in[1].value = 0
    dut.ui_in[2].value = 1
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 0

    # A=0, B=1, C=0 -> F=1
    dut.ui_in[0].value = 0
    dut.ui_in[1].value = 1
    dut.ui_in[2].value = 0
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 1

    # A=0, B=1, C=1 -> F=0
    dut.ui_in[0].value = 0
    dut.ui_in[1].value = 1
    dut.ui_in[2].value = 1
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 0

    # A=1, B=0, C=0 -> F=1
    dut.ui_in[0].value = 1
    dut.ui_in[1].value = 0
    dut.ui_in[2].value = 0
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 1

    # A=1, B=0, C=1 -> F=0
    dut.ui_in[0].value = 1
    dut.ui_in[1].value = 0
    dut.ui_in[2].value = 1
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 0

    # A=1, B=1, C=0 -> F=1
    dut.ui_in[0].value = 1
    dut.ui_in[1].value = 1
    dut.ui_in[2].value = 0
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 1

    # A=1, B=1, C=1 -> F=1 (AB=1)
    dut.ui_in[0].value = 1
    dut.ui_in[1].value = 1
    dut.ui_in[2].value = 1
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 1
