# MRIS: Minimal RISC-V ISA Simulator
MRIS is a command-line RISC-V ISA Simulator written in Python.
It is capable of simulating RV32I base integer instruction set, as defined in [riscv-isa-manual](https://github.com/riscv/riscv-isa-manual).
It provides easy debugging experience by allowing the observation of internal values at each stage.

## Prerequisites
The 32-bit RISC-V GNU compiler toolchain is required for simulating. For details on installation: [riscv-gnu-toolchain](https://github.com/riscv-collab/riscv-gnu-toolchain)

## Test Statistics
Simulation verifications are based on [riscv-test-suite](https://github.com/riscv-non-isa/riscv-arch-test/tree/main/riscv-test-suite).
You can see the result of each testcase through the ```-t``` option.
For more details on the test suites: [riscv-arch-test](https://github.com/riscv-non-isa/riscv-arch-test)

## Running MRIS
```bash
$ ./bin/mris <file>
$ ./bin/mris -d <file>  # for debug mode
$ ./bin/mris -t addi    # for simulation verification
```