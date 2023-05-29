import subprocess

def asm2hex(path_mem_text, path_build):
    subprocess.run(f"mkdir -p {path_build}", shell = True)
    subprocess.run(f"riscv32-unknown-elf-as -o {path_build}/temp.o {path_mem_text}", shell = True)
    subprocess.run(f"riscv32-unknown-elf-objcopy -O verilog {path_build}/temp.o {path_build}/temp.hex", shell = True)

    return f"{path_build}/temp.hex"