import sys
import os
import subprocess

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import signal_handler
import argparse
import build
from help_formatter import HelpFormatter
from register_file import RegisterFile
from memory import Memory
from simulation import Simulation
from test_suite import test

# Signal Handling
signal_handler.signal_handler()

# Sets path
path_dir = os.path.dirname(__file__)
path_build = f"{path_dir}/../build"

# Argument Parsing
parser = argparse.ArgumentParser(formatter_class = HelpFormatter)
parser.add_argument("mem_text", nargs = "?")
parser.add_argument("-d", "--debug", action = "store_true")
parser.add_argument("-t", "--test", nargs = "?", const = "all")
args = parser.parse_args()

if args.test == "all":
    test.verify_all()

elif args.test is not None:
    test.verify(args.test)

elif args.mem_text is None:
    sys.exit("No input file\nUsage: mris [options] file")

elif args.debug:
    # Assembles input file
    path_hex = build.asm2hex(args.mem_text, path_build)

    # Instantiate register file and memory
    reg_file = RegisterFile()
    mem = Memory(path_hex)

    # Initialize simulation
    simulate = Simulation()

    while (True):
        print("(mris)", end = " ")
        try:
            command = input().split()
        except EOFError:
            sys.exit()

        if len(command) == 0:
            continue

        elif command[0] == "q" or command[0] == "quit" or command[0] == "e" or command[0] == "exit":
            sys.exit()

        elif command[0] == "h" or command[0] == "help":   
            print("Minimal RISC-V ISA Simulator")
            print("Authored by sihun-chae (sihnchae@gmail.com)\n")
            print("Usage:")
            print("  q, quit\t\tExit from mris")
            print("  h, help\t\tShow this help message")
            print("  r, run <cycle>\tSimulate until halted (with cycle, if specified)")
            print("  s, step\t\tSimulate next line")
            print("  i, init\t\tInitialize simulation")
            print("  x, reg <num>\t\tDump value of register")
            print("  m, mem <addr>\t\tDump value of memory")
            print("  set {reg|mem} <num> <value>\n\t\t\tSet value of register/memory")

        elif command[0] == "r" or command[0] == "run":
            if simulate.halted() == True:
                print("Simulate is already done.")
                print(f"Simulated cycle: {simulate.get_cycle()}")
                continue
    
            if len(command) == 1:
                while (simulate.halted() == False):
                    simulate.run_cycle(reg_file, mem)
            else:
                for i in range(int(command[1])):
                    if (simulate.halted() == False):
                        simulate.run_cycle(reg_file, mem)

            if simulate.halted() == True:
                print("Simulation complete.")
                print(f"Simulated cycle: {simulate.get_cycle()}")
        
        elif command[0] == "s" or command[0] == "step":
            if simulate.halted() == True:
                print("Simulate is already done.")
                print(f"Simulated cycle: {simulate.get_cycle()}")
                continue

            simulate.run_cycle(reg_file, mem)

            if simulate.halted() == True:
                print("Simulation complete.")
                print(f"Simulated cycle: {simulate.get_cycle()}")

        elif command[0] == "i" or command[0] == "init":
            simulate.reset()
            reg_file.reset()
            mem.reset_data()
            print("Simulation initialized")

        elif command[0] == "x" or command[0] == "reg":
            if len(command) == 1:
                reg_file.dump_all()
            else:
                reg_file.dump(int(command[1]))

        elif command[0] == "m" or command[0] == "mem":
            if len(command) == 1:
                print(".text")
                mem.dump_text()
                print(".data")
                mem.dump_data()
            else:
                pass

        elif command[0] == "set":
            if len(command) < 4:
                print("Invalid argument")
                continue
            
            if command[1] == "r" or command[1] == "reg":
                reg_file.set(int(command[2]), int(command[3], 16))
            else:
                print(f"Invalid argument")
        else:
            print(f"Invalid command: {command[0]}")

else:
    # Assembles input file
    path_hex = build.asm2hex(args.mem_text, path_build)

    # Instantiate register file and memory
    reg_file = RegisterFile()
    mem = Memory(path_hex)

    # Initialize simulation
    simulate = Simulation()

    while simulate.halted() == False:
        simulate.run_cycle(reg_file, mem)

    print("Simulation complete.")
    print(f"Simulated cycle: {simulate.get_cycle()}")
    reg_file.dump_all()