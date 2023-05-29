import sys

class Memory:
    def __init__(self, path_mem_text, path_mem_data = None):
        self.mem_text_start = 0x00100000
        self.mem_text_length = 0x40000 # 256K
        self.mem_text_end = self.mem_text_start + self.mem_text_length

        self.mem_data_start = 0x10000000
        self.mem_data_length = 0x160000 # 1M
        self.mem_data_end = self.mem_data_start + self.mem_data_length

        # Load text area
        self.mem_seg_text = self._load(path_mem_text, "text")

        # Load data area
        if path_mem_data is not None:
            self.mem_seg_data = self._load(path_mem_data, "data")
        else:
            self.mem_seg_data = {}

    def reset_data(self):
        self.mem_seg_data = {}

    def _load(self, path_mem, segment):
        """
        Loads initial memory values from memory data file

        Args:
            path_mem (str): Path of memory file
            segment (str): Indicates which segment

        Returns:
            mem_state (dict): {address (int): value (int)}
        """
        try:
            with open(path_mem, 'r') as file_mem:
                lines = file_mem.readlines()

        except FileNotFoundError:
            sys.exit(f"File not found: {path_mem}")

        # Contains value for each address
        # Uninitialized address does not exist as a key
        mem_state = {}

        if segment == "text":
            mem_start = self.mem_text_start
            mem_end = self.mem_text_end
        else:
            mem_start = self.mem_data_start
            mem_end = self.mem_data_end

        mem_offset = 0
        mem_index = 0
        mem_value = 0

        byte_index = 0

        for line in lines:
            if line.startswith('@'):
                mem_offset = mem_start + int(line[1:9], 16)
                mem_index = 0
            else:
                bytes = line.split()
                for byte in bytes:
                    mem_value += int(byte, 16) << (byte_index * 8)
                    byte_index += 1
                    if (byte_index == 4):
                        if (mem_offset + mem_index * 4 < mem_start or
                            mem_offset + mem_index * 4 >= mem_end):
                            sys.exit("Segmentation fault")
                        else:
                            mem_state[mem_offset + mem_index * 4] = mem_value
                            mem_index += 1
                            mem_value = 0
                            byte_index = 0

        return mem_state

    def fetch(self, pc):
        """
        Read instruction with given pc

        Args:
            pc (int): Program counter
        
        Returns:
            inst (str): Instruction
        """
        inst = format(self.mem_seg_text[pc], '032b')
        return inst
    
    def read(self, address, unit, sign_extend = False):
        """
        Read value of memory from given address

        Args:
            address (int): Memory address to read
            unit (str): "w" if word, "h" if halfword, "byte" if byte
        
        Returns:
            value (int): Value of memory at given address
        """
        index = address % 4
        offset = address - index

        mask = 0
        shamt = 0

        if unit == "w":
            if index != 0:
                sys.exit("Alignment exception")
            else:
                mask = 0xffffffff
                shamt = 0

        elif unit == "h":
            if index == 0:
                mask = 0x0000ffff
                shamt = 0
            elif index == 2:
                mask = 0xffff0000
                shamt = 16
            else:
                sys.exit("Alignment exception")

        elif unit == "b":
            if index == 0:
                mask = 0x000000ff
                shamt = 0
            elif index == 1:
                mask = 0x0000ff00
                shamt = 8
            elif index == 2:
                mask = 0x00ff0000
                shamt = 16
            elif index == 3:
                mask = 0xff000000
                shamt = 24

        else:
            sys.exit()

        # Read memory
        if offset >= self.mem_text_start and offset < self.mem_text_end:
            if offset in self.mem_seg_text:
                value = self.mem_seg_text[offset]
            else:
                value = 0
            
        elif offset >= self.mem_data_start and offset < self.mem_data_end:
            if offset in self.mem_seg_data:
                value = self.mem_seg_data[offset]
            else:
                value = 0

        else:
            sys.exit("Illegal memory access")

        value = (value & mask) >> shamt

        # Sign extend
        if sign_extend == True:
            if unit == "h":
                if value & 0x8000:
                    value += 0xffff0000
            elif unit == "b":
                if value & 0x80:
                    value += 0xffffff00

        return value

    def write(self, address, value, unit):
        """
        Write value of memory at given address

        Args:
            address (int): Memory address to write
            value (int): Memory value to write
            unit (str): "w" if word, "h" if halfword, "byte" if byte
        """
        index = address % 4
        offset = address - index

        mask = 0
        shamt = 0

        if unit == "w":
            if index != 0:
                sys.exit("Alignment exception")
            else:
                mask = 0xffffffff
                shamt = 0

        elif unit == "h":
            if index == 0:
                mask = 0x0000ffff
                shamt = 0
            elif index == 2:
                mask = 0xffff0000
                shamt = 16
            else:
                sys.exit("Alignment exception")

        elif unit == "b":
            if index == 0:
                mask = 0x000000ff
                shamt = 0
            elif index == 1:
                mask = 0x0000ff00
                shamt = 8
            elif index == 2:
                mask = 0x00ff0000
                shamt = 16
            elif index == 3:
                mask = 0xff000000
                shamt = 24

        else:
            sys.exit()

        if offset >= self.mem_text_start and offset < self.mem_text_end:
            if offset in self.mem_seg_text:
                value = (self.mem_seg_text[offset] & ~mask) + ((value << shamt) & mask)
                self.mem_seg_text[offset] = value
            else:
                value = (value << shamt) & mask
                self.mem_seg_text[offset] = value

        elif offset >= self.mem_data_start and offset < self.mem_data_end:
            if offset in self.mem_seg_data:
                value = (self.mem_seg_data[offset] & ~mask) + ((value << shamt) & mask)
                self.mem_seg_data[offset] = value
                
            else:
                value = (value << shamt) & mask
                self.mem_seg_data[offset] = value

        else:
            sys.exit("Illegal memory access")
    
    def dump_text(self):
        """
        Print value of text area in memory
        """
        for key, value in self.mem_seg_text.items():
            print("0x{:08x}:\t0x{:08x}".format(key, value))

    def dump_data(self):
        """
        Print value of data area in memory
        """
        for key, value in self.mem_seg_data.items():
            print("0x{:08x}:\t0x{:08x}".format(key, value))

    def dump(self, address, file_output = None):
        """
        Print value of given address
        """
        value = self.read(address, "w", False)
        if file_output is not None:
            file_output.write(f"0x{value:08x}\n")
        else:
            print(value)