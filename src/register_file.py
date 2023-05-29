import ctypes

class RegisterFile:
    register_name = ["zero", "ra", "sp", "gp", "tp", "t0", "t1", "t2",
                     "s0/fp", "s1", "a0", "a1", "a2", "a3", "a4", "a5",
                     "a6", "a7", "s2", "s3", "s4", "s5", "s6", "s7",
                     "s8", "s9", "s10", "s11", "t3", "t4", "t5", "t6"]

    def __init__(self, reset_value = 0):
        self.reset_value = reset_value
        self.register_state = [self.reset_value] * 32

    def reset(self):
        """
        Resets register values
        """
        self.register_state = [self.reset_value] * 32

    def set(self, num, data):
        """
        Sets register value
        
        Args:
            num (int): Number of register
        """
        self.register_state[num] = ctypes.c_uint32(data).value

    def read(self, num_src):
        """
        Reads register value

        Args:
            num_src (int): Number of register

        Returns:
            data_src (int): Value of register

        Raises:
            IndexError: If num_src is out of register index
        """
        if (num_src < 0 or num_src > 31):
            raise IndexError("Invalid register index")
        data_src = self.register_state[num_src]

        return data_src
    
    def write(self, num_dest, data_dest):
        """
        Writes register value

        Args:
            num_dest (int): Number of register
            data_dest (int): Data to write

        Raises:
            IndexError: If num_dest is out of register index
        """
        if (num_dest > 31):
            raise IndexError("Invalid register index")
        
        if (num_dest != 0):
            self.register_state[num_dest] = ctypes.c_uint32(data_dest).value

    def dump_all(self):
        """
        Prints values of all registers
        """
        print("Register dump:")
        for num, name, data in zip(range(32), self.register_name, self.register_state):
            f_name = f"({name})"
            print(f"x{str(num):2s}{f_name:>7s}:\t0x{data:08x} ({data})")

    def dump(self, num, file_output = None):
        """
        Prints value of a given register

        Args:
            num (int): Number of register
            file_output
        """
        f_name = f"({self.register_name[num]})"

        if file_output is not None:
            file_output.write(f"x{str(num):2s}{f_name:>7s}:\t0x{self.register_state[num]:08x} ({self.register_state[num]})\n")
        else:
            print(f"x{str(num):2s}{f_name:>7s}:\t0x{self.register_state[num]:08x} ({self.register_state[num]})")