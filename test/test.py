import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1

    vectors = [
        (0,0,1),
        (0,1,1),
        (1,0,1),
        (1,1,0),
    ]

    for A,B,Yexp in vectors:
        dut.ui_in[0].value = A
        dut.ui_in[1].value = B
        await ClockCycles(dut.clk, 1)
        assert int(dut.uo_out[0].value) == Yexp
