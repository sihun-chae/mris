import sys
import os
import subprocess
import time
import ctypes

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from src import simulation, memory, register_file
from .rv32i.base import addi, slti, sltiu, xori, ori, andi, slli, srli, srai, add, sub, sll, slt, sltu, xor, srl, sra, or_, and_

# Set path
path_dir = os.path.dirname(__file__)
path_asm = f"{path_dir}/build/test.s"
path_config = f"{path_dir}/build/test.config"
path_log = f"{path_dir}/build/test.log"
path_hex = f"{path_dir}/build/test.hex"
path_object = f"{path_dir}/build/test.o"

def append_ecall():
    """
    Appends ecall at file_asm and file_config
    """
    global file_asm, file_config

    file_asm.write("\tecall\n")
    file_config.write("ecall\n")

def append_i_type(opcode, num_dest, num_src_1, data_dest, data_src_1, imm):
    """
    Append i_type instruction at file_asm and file_config

    Args:
        opcode (str): Instruction opcode
        num_dest (int): Number of destination register
        num_src_1 (int): Number of source 1 register
        data_dest (int): Data of destination register
        data_src_1 (int): Data of source 1 register
        imm (int): Instruction immediate
    """
    global file_asm, file_config

    if imm > 2047:
        imm -= 4096

    inst = f"{opcode}\tx{num_dest}, x{num_src_1}, {imm}"

    file_asm.write(f"\t{inst}\n")
    file_config.write(f"{num_dest} 0x{ctypes.c_uint32(data_dest).value:08x} {num_src_1} 0x{ctypes.c_uint32(data_src_1).value:08x}\n")

def append_r_type(opcode, num_dest, num_src_1, num_src_2, data_dest, data_src_1, data_src_2):
    """
    Append r_type instruction at file_asm and file_config

    Args:
        opcode (str): Instruction opcode
        num_dest (int): Number of destination register
        num_src_1 (int): Number of source 1 register
        num_src_2 (int): Number of source 2 register
        data_dest (int): Data of destination register
        data_src_1 (int): Data of source 1 register
        data_src_2 (int): Data of source 2 register
    """
    global file_asm, file_config

    inst = f"{opcode}\tx{num_dest}, x{num_src_1}, x{num_src_2}"

    file_asm.write(f"\t{inst}\n")
    file_config.write(f"{num_dest} 0x{ctypes.c_uint32(data_dest).value:08x} {num_src_1} 0x{ctypes.c_uint32(data_src_1).value:08x} {num_src_2} 0x{ctypes.c_uint32(data_src_2).value:08x}\n")

def append_s_type(opcode, num_src_1, num_src_2, data_src_1, data_src_2, imm, mem_value):
    """
    Append s_type instruction at file_asm and file_config

    Args:
        opcode (str): Instruction opcode
        num_src_1 (int): Number of source 1 register
        num_src_2 (int): Number of source 2 register
        data_src_1 (int): Data of source 1 register
        data_src_1 (int): Data of source 2 register
        imm (int): Instruction immediate
    """
    global file_asm, file_config

    if imm > 2047:
        imm -= 4096

    inst = f"{opcode}\tx{num_src_2}, {imm}(x{num_src_1})"

    file_asm.write(f"\t{inst}\n")
    file_config.write(f" {num_src_2} 0x{ctypes.c_uint32(data_src_2).value:08x} {num_src_1} 0x{ctypes.c_uint32(data_src_1).value:08x} {imm} 0x{ctypes.c_uint32(mem_value).value:08x}\n")

def verify(opcode):
    """
    Tests given opcode

    Args:
        opcode (str): Instruction opcode

    Returns:
        passed (bool): If true all testcases passed
    """
    global file_asm, file_config, file_log
    global reg_file, mem

    clean()

    # Set testcases
    file_asm = open(path_asm, "a")
    file_config = open(path_config, "a")

    if opcode.lower() == "addi":
        type_op = "OP_IMM"
        addi.set_tests()
    elif opcode.lower() == "slti":
        type_op = "OP_IMM"
        slti.set_tests()
    elif opcode.lower() == "sltiu":
        type_op = "OP_IMM"
        sltiu.set_tests()
    elif opcode.lower() == "xori":
        type_op = "OP_IMM"
        xori.set_tests()
    elif opcode.lower() == "ori":
        type_op = "OP_IMM"
        ori.set_tests()
    elif opcode.lower() == "andi":
        type_op = "OP_IMM"
        andi.set_tests()
    elif opcode.lower() == "slli":
        type_op = "OP_IMM"
        slli.set_tests()
    elif opcode.lower() == "srli":
        type_op = "OP_IMM"
        srli.set_tests()
    elif opcode.lower() == "srai":
        type_op = "OP_IMM"
        srai.set_tests()
    elif opcode.lower() == "add":
        type_op = "OP_RR"
        add.set_tests()
    elif opcode.lower() == "sub":
        type_op = "OP_RR"
        sub.set_tests()
    elif opcode.lower() == "sll":
        type_op = "OP_RR"
        sll.set_tests()
    elif opcode.lower() == "slt":
        type_op = "OP_RR"
        slt.set_tests()
    elif opcode.lower() == "sltu":
        type_op = "OP_RR"
        sltu.set_tests()
    elif opcode.lower() == "xor":
        type_op = "OP_RR"
        xor.set_tests()
    elif opcode.lower() == "srl":
        type_op = "OP_RR"
        srl.set_tests()
    elif opcode.lower() == "sra":
        type_op = "OP_RR"
        sra.set_tests()
    elif opcode.lower() == "or":
        type_op = "OP_RR"
        or_.set_tests()
    elif opcode.lower() == "and":
        type_op = "OP_RR"
        and_.set_tests()

    file_asm.close()
    file_config.close()

    # Make hexadecimal file from assembly
    asm2hex()

    # Initialize register file and memory
    reg_file = register_file.RegisterFile()
    mem = memory.Memory(path_hex)
    
    # Simulate testcodes
    simulate = simulation.Simulation()

    with open(path_config, "r") as file_config:
        line_config = file_config.readlines()

    file_log = open(path_log, "a")
    
    while simulate.halted() == False:
        word_config = line_config[simulate.get_cycle()].split()

        if word_config[0] == "ecall":
            simulate.run_cycle(reg_file, mem)

        else:
            # Initialize register from test.config
            if type_op == "OP_IMM":
                reg_file.set(int(word_config[2]), int(word_config[3], 16))
                simulate.run_cycle(reg_file, mem)
                reg_file.dump(int(word_config[0]), file_log)
                reg_file.reset()

            elif type_op == "OP_RR":
                reg_file.set(int(word_config[2]), int(word_config[3], 16))
                reg_file.set(int(word_config[4]), int(word_config[5], 16))
                simulate.run_cycle(reg_file, mem)
                reg_file.dump(int(word_config[0]), file_log)
                reg_file.reset()

            elif type_op == "LOAD":
                pass

            elif type_op == "STORE":
                reg_file.set(int(word_config[0]), int(word_config[1], 16))
                reg_file.set(int(word_config[2]), int(word_config[3], 16))
                simulate.run_cycle(reg_file, mem)
                mem.dump(int(word_config[3], 16) + int(word_config[4]), file_log)
                reg_file.reset()
        
    file_log.close()
    
    # Check
    with open(path_log, "r") as file_log:
        line_log = file_log.readlines()

    cnt_pass = 0
    cnt_fail = 0

    for i in range(len(line_config) - 1):
        word_config = line_config[i].split()
        word_log = line_log[i].split()

        if int(word_log[2], 16) == int(word_config[1], 16):
            cnt_pass += 1

        else:
            print(f"testcase{i}: FAIL")
            print(f"Should be 0x{int(word_config[1], 16):08x} but is {word_log[2]}")
            cnt_fail += 1

        if i == (len(line_config) - 2):
            print(f"{opcode.upper():5s} verification:\t{cnt_pass}/{i + 1} testcases passed")
            if cnt_pass == i + 1:
                passed = True
            else:
                passed = False
    return passed

def verify_all():
    """
    Verifies with all specified testcases
    """
    start_time = time.time()

    verify_dict = {}
    failed_dict = {}

    verify_dict["ADDI"] = verify("addi")
    verify_dict["SLTI"] = verify("slti")
    verify_dict["SLTIU"] = verify("sltiu")
    verify_dict["XORI"] = verify("xori")
    verify_dict["ORI"] = verify("ori")
    verify_dict["ANDI"] = verify("andi")
    verify_dict["SLLI"] = verify("slli")
    verify_dict["SRLI"] = verify("srli")
    verify_dict["SRAI"] = verify("srai")
    verify_dict["ADD"] = verify("add")
    verify_dict["SUB"] = verify("sub")
    verify_dict["SLL"] = verify("sll")
    verify_dict["SLT"] = verify("slt")
    verify_dict["SLTU"] = verify("sltu")
    verify_dict["XOR"] = verify("xor")
    verify_dict["SRL"] = verify("srl")
    verify_dict["SRA"] = verify("sra")
    verify_dict["OR"] = verify("or")
    verify_dict["AND"] = verify("and")

    for key, value in verify_dict.items():
        if value == False:
            failed_dict[key] = value

    if len(failed_dict.values()) == 0:
        print("\nAll verification passed\n")
    else:
        print("\nVerification failed:")
        for key in failed_dict.keys():
            print(f"{key}\n")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Total execution time: {end_time - start_time:.4f} seconds")

def asm2hex():
    """
    Converts assembly to hexadecimal file
    """
    subprocess.run(f"riscv32-unknown-elf-as -o {path_dir}/build/test.o {path_dir}/build/test.s", shell = True)
    subprocess.run(f"riscv32-unknown-elf-objcopy -O verilog {path_dir}/build/test.o {path_dir}/build/test.hex", shell = True)

def clean():
    """
    Cleans build files
    """
    subprocess.run(f"mkdir -p {path_dir}/build", shell = True)
    subprocess.run(f"rm -rf {path_asm} {path_config} {path_hex} {path_log} {path_object}", shell = True)