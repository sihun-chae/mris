import ctypes

class Simulation:
    def __init__(self):
        """
        Initializes simulation
        """
        self.halt = False
        self.pc = 0x00100000
        self.is_branch = False
        self.cycle = 0

    def reset(self):
        """
        Resets simulation
        """
        self.halt = False
        self.pc = 0x00100000
        self.is_branch = False
        self.cycle = 0

    def halted(self):
        """
        Checks if the simulation is halted

        Returns:
            halt (bool): True if simulation halted
        """
        return self.halt

    def get_cycle(self):
        """
        Gets the simulated cycle of the simulation

        Returns:
            cycle (int): Simulated cycle
        """
        return self.cycle

    def run_cycle(self, reg_file, mem):
        """
        Simulate one cycle with given pc
        
        Args:
            reg_file (RegisterFile): Register file
            mem (Memory): memory
        """
        # Instruction fetch
        inst = mem.fetch(self.pc)

        # Instruction Decode
        self.decode(inst)

        # Execute
        self.execute(reg_file, mem)

        # If execute instruction is branch type, PC is adjusted at execution time
        if not self.is_branch:
            self.pc += 4

        self.cycle += 1

    def decode(self, inst):
        """
        Decodes given instruction
        
        Args:
            inst (str): Instruction
        """

        # With inst_ prefix is string type data
        self.inst_opcode = inst[25:32]
        self.inst_funct_3 = inst[17:20]
        self.inst_funct_7 = inst[0:7]

        self.rs_1   = int(inst[12:17], 2)
        self.rs_2   = int(inst[7:12], 2)
        self.rd     = int(inst[20:25], 2)
        self.shamt  = int(inst[7:12], 2)
        self.imm_i  = int(inst[0] * 21 + inst[1:12], 2)
        self.imm_s  = int(inst[0] * 21 + inst[1:7] + inst[20:25], 2)
        self.imm_b  = int(inst[0] * 20 + inst[24] + inst[1:7] + inst[20:24] + "0", 2)
        self.imm_u  = int(inst[0:20] + "0" * 12, 2)
        self.imm_j  = int(inst[0] * 12 + inst[12:20] + inst[11] + inst[1:11] + "0", 2)

    def execute(self, reg_file, mem):
        """
        Execute an instruction

        Args:
            reg_file (RegisterFile): Register file
            mem (Memory): memory

        Raises:
            KeyError: If no opcode matches
        """
        inst_opcode = self.inst_opcode
        inst_funct_3 = self.inst_funct_3
        inst_funct_7 = self.inst_funct_7

        rs_1 = self.rs_1
        rs_2 = self.rs_2
        rd = self.rd
        shamt = self.shamt
        imm_i = self.imm_i
        imm_s = self.imm_s
        imm_b = self.imm_b
        imm_u = self.imm_u
        imm_j = self.imm_j

        data_rs_1 = reg_file.read(rs_1)
        signed_data_rs_1 = ctypes.c_int32(data_rs_1).value

        data_rs_2 = reg_file.read(rs_2)
        signed_data_rs_2 = ctypes.c_int32(data_rs_2).value

        shamt_rs_2 = data_rs_2 & 0b11111

        signed_imm_i = ctypes.c_int32(imm_i).value

        data_rd = None
        self.is_branch = False

        if inst_opcode == "0110111": # LUI
            data_rd = imm_u
            reg_file.write(rd, data_rd)

        elif inst_opcode == "0010111": # AUIPC
            data_rd = self.pc + imm_u
            reg_file.write(rd, data_rd)

        elif inst_opcode == "1101111": # JAL
            self.is_branch = True
            data_rd = self.pc + 4
            self.pc = imm_j
            reg_file.write(rd, data_rd)

        elif inst_opcode == "1100111": # JALR
            self.is_branch = True
            data_rd = self.pc + 4
            self.pc = ctypes.c_uint32((data_rs_1 + imm_i) << 1).value
            reg_file.write(rd, data_rd)

        elif inst_opcode == "1100011": # BR
            if inst_funct_3 == "000": # BEQ
                if data_rs_1 == data_rs_2:
                    self.is_branch = True
                    self.pc += imm_b

            elif inst_funct_3 == "001": # BNE
                if data_rs_1 != data_rs_2:
                    self.is_branch = True
                    self.pc += imm_b

            elif inst_funct_3 == "100": # BLT
                if signed_data_rs_1 < signed_data_rs_2:
                    self.is_branch = True
                    self.pc += imm_b

            elif inst_funct_3 == "101": # BGE
                if signed_data_rs_1 >= signed_data_rs_2:
                    self.is_branch = True
                    self.pc += imm_b

            elif inst_funct_3 == "110": # BLTU
                if data_rs_1 < data_rs_2:
                    self.is_branch = True
                    self.pc += imm_b

            elif inst_funct_3 == "111": # BGEU
                if data_rs_1 >= data_rs_2:
                    self.is_branch = True
                    self.pc += imm_b
            
            else:
                raise KeyError("Invalid instruction")

        elif inst_opcode == "0000011": # LOAD
            if inst_funct_3 == "000": #LB
                data_rd = mem.read(data_rs_1 + imm_i, "b", True)

            elif inst_funct_3 == "001": #LH
                data_rd = mem.read(data_rs_1 + imm_i, "h", True)

            elif inst_funct_3 == "010": #LW
                data_rd = mem.read(data_rs_1 + imm_i, "w", True)

            elif inst_funct_3 == "100": #LBU
                data_rd = mem.read(data_rs_1 + imm_i, "b", False)

            elif inst_funct_3 == "101": #LHU
                data_rd = mem.read(data_rs_1 + imm_i, "h", False)

            else:
                raise KeyError("Invalid instruction")
            
            reg_file.write(rd, data_rd)
            
        elif inst_opcode == "0100011": # STORE
            if inst_funct_3 == "000": #SB
                mem.write(data_rs_1 + imm_s, data_rs_2, "b")

            elif inst_funct_3 == "001": #SH
                mem.write(data_rs_1 + imm_s, data_rs_2, "h")

            elif inst_funct_3 == "010": #SW
                mem.write(data_rs_1 + imm_s, data_rs_2, "w")

            else:
                raise KeyError("Invalid instruction")

        elif inst_opcode == "0010011": # OP_IMM
            if inst_funct_3 == "000": # ADDI
                data_rd = data_rs_1 + imm_i
                
            elif inst_funct_3 == "010": # SLTI
                data_rd = int(signed_data_rs_1 < signed_imm_i)

            elif inst_funct_3 == "011": # SLTIU
                data_rd = int(data_rs_1 < imm_i)

            elif inst_funct_3 == "100": # XORI
                data_rd = data_rs_1 ^ imm_i

            elif inst_funct_3 == "110": # ORI
                data_rd = data_rs_1 | imm_i

            elif inst_funct_3 == "111": # ANDI
                data_rd = data_rs_1 & imm_i

            elif inst_funct_3 == "001": # SLLI
                data_rd = data_rs_1 << shamt

            elif inst_funct_3 == "101":
                if inst_funct_7 == "0000000": #SRLI
                    data_rd = data_rs_1 >> shamt

                elif inst_funct_7 == "0100000": #SRAI
                    data_rd = data_rs_1 >> shamt
                    if signed_data_rs_1 < 0:
                        data_rd |= int("1" * shamt + "0" * (32 - shamt), 2)

                else:
                    raise KeyError("Invalid instruction")
            
            else:
                raise KeyError("Invalid instruction")
            
            reg_file.write(rd, data_rd)
        
        elif inst_opcode == "0110011": # OP_RR
            if inst_funct_3 == "000":
                if inst_funct_7 == "0000000": # ADD
                    data_rd = data_rs_1 + data_rs_2

                elif inst_funct_7 == "0100000": # SUB
                    data_rd = data_rs_1 - data_rs_2

                else:
                    raise KeyError("Invalid instruction")
                
            elif inst_funct_3 == "001": # SLL
                data_rd = data_rs_1 << shamt_rs_2

            elif inst_funct_3 == "010": # SLT
                data_rd = int(signed_data_rs_1 < signed_data_rs_2)

            elif inst_funct_3 == "011": # SLTU
                data_rd = int(data_rs_1 < data_rs_2)

            elif inst_funct_3 == "100": # XOR
                data_rd = data_rs_1 ^ data_rs_2
            
            elif inst_funct_3 == "101":
                if inst_funct_7 == "0000000": # SRL
                    data_rd = data_rs_1 >> shamt_rs_2

                elif inst_funct_7 == "0100000": # SRA
                    data_rd = data_rs_1 >> shamt_rs_2
                    if signed_data_rs_1 < 0:
                        data_rd |= int("1" * shamt_rs_2 + "0" * (32 - shamt_rs_2), 2)

                else:
                    raise KeyError("Invalid instruction")

            elif inst_funct_3 == "110": # OR
                data_rd = data_rs_1 | data_rs_2

            elif inst_funct_3 == "111": # AND
                data_rd = data_rs_1 & data_rs_2

            else:
                raise KeyError("Invalid instruction")
            
            reg_file.write(rd, data_rd)
            
        elif inst_opcode == "0001111": # FENCE
            pass
        
        elif inst_opcode == "1110011":
            if imm_i == 0: # ECALL
                self.halt = True

            elif imm_i == 1: # EBREAK
                pass

            else:
                raise KeyError("Invalid instruction")

        else:
            raise KeyError("Invalid instruction")
