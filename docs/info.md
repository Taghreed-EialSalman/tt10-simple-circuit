# NAND Gate

## Project Overview
This project implements a **2-input NAND gate** using the TinyTapeout open-source ASIC flow.
The design is written in Verilog and verified using cocotb-based simulation before GDS generation.

## Functionality
The NAND gate outputs logic LOW only when both inputs are HIGH.  
For all other input combinations, the output is HIGH.

## Inputs and Outputs
- **Inputs**
  - A (ui[0])
  - B (ui[1])

- **Output**
  - Y = ~(A & B) (uo[0])

## Design Notes
- The design is purely combinational.
- No clock is required.
- Unused inputs and outputs are safely tied off.

## Author
Taghreed EialSalman
