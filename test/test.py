import random
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_project(dut):
    # Simple Circuit: F = AB + C'
    # Inputs: A=ui_in[0], B=ui_in[1], C=ui_in[2]
    # Output: F=uo_out[0]

    for _ in range(50):
        A = random.randint(0, 1)
        B = random.randint(0, 1)
        C = random.randint(0, 1)

        # Build ui_in value
        ui = (A << 0) | (B << 1) | (C << 2)
        dut.ui_in.value = ui

        await Timer(1, units="ns")

        Fexp = (A & B) | (1 - C)   # since C is 0/1, C' = 1-C

        assert int(dut.uo_out[0].value) == Fexp, \
            f"Mismatch: A={A} B={B} C={C} => expected F={Fexp}, got {int(dut.uo_out[0].value)}"
