from microbit import *
import time
class DataError(Exception):
    pass
	
class DHT11:
    def __init__(self, pin):
        self._pin = pin
        self.input_pin = [pin0,pin1,pin2,pin3,pin4,pin6,pin7,pin8,pin9,pin10,pin12,pin13,pin14,pin15,pin16]
        self.shift_value = [3,2,1,4,5,12,11,18,10,6,20,23,22,21,16]
    def read(self):
        # creating these locals speeds things up len() is very slow
        pin = self._pin
        pin2bit = self._pin2bit()
        buffer_ = bytearray(320)
        length = (len(buffer_) // 4) * 4
        for i in range(length, len(buffer_)):
            buffer_[i] = 1
        pin.write_digital(1)
        time.sleep_ms(50)
        self._block_irq()
        pin.write_digital(0)
        time.sleep_ms(20)
        pin.set_pull(pin.PULL_UP)
        if self._grab_bits(pin2bit, buffer_, length) != length:
            self._unblock_irq()
            raise Exception("Grab bits failed.")
        else:
            self._unblock_irq()
        data = self._parse_data(buffer_)
        del buffer_
        if data is None or len(data) != 40:
            if data is None:
                bits = 0
            else:
                bits = len(data)
            raise DataError("Too many or too few bits " + str(bits))
        data = self._calc_bytes(data)
        checksum = self._calc_checksum(data)
        if data[4] != checksum:
            raise DataError("Checksum invalid.")
        temp=data[2] + (data[3] / 10)
        humid=data[0] + (data[1] / 10)
        return (temp, humid)
    def _pin2bit(self):
        # this is a dictionary, microbit.pinX can't be a __hash__
        pin = self._pin
        if pin in self.input_pin:
            shift = self.shift_value[self.input_pin.index(pin)]
        else :
            raise ValueError('function not suitable for this pin')
        return shift
    @staticmethod
    @micropython.asm_thumb
    def _block_irq():
        cpsid('i')          # disable interrupts to go really fast
    @staticmethod
    @micropython.asm_thumb
    def _unblock_irq():
        cpsie('i')          # enable interupts nolonger time critical
    # r0 - pin bit id
    # r1 - byte array
    # r2 - len byte array, must be a multiple of 4
    @staticmethod
    @micropython.asm_thumb
    def _grab_bits(r0, r1, r2):
        b(START)
        # DELAY routine
        label(DELAY)
        mov(r7, 0x2d)
        label(delay_loop)
        sub(r7, 1)
        bne(delay_loop)
        bx(lr)
        label(READ_PIN)
        mov(r3, 0x50)      # r3=0x50
        lsl(r3, r3, 16)    # r3=0x500000
        add(r3, 0x05)      # r3=0x500005
        lsl(r3, r3, 8)     # r3=0x50000500 -- this points to GPIO registers
        add(r3, 0x10)      # r3=0x50000510 -- points to read_digital bits
        ldr(r4, [r3, 0])   # move memory@r3 to r2
        mov(r3, 0x01)      # create bit mask in r3
        lsl(r3, r0)        # select bit from r0
        and_(r4, r3)
        lsr(r4, r0)
        bx(lr)
        label(START)
        mov(r5, 0x00)      # r5 - byte array index
        label(again)
        mov(r6, 0x00)      # r6 - current word
        bl(READ_PIN)
        orr(r6,  r4)       # bitwise or the pin into current word
        bl(DELAY)
        bl(READ_PIN)
        lsl(r4, r4, 8)     # move it left 1 byte
        orr(r6,  r4)       # bitwise or the pin into current word
        bl(DELAY)
        bl(READ_PIN)
        lsl(r4, r4, 16)     # move it left 2 bytes
        orr(r6,  r4)       # bitwise or the pin into current word
        bl(DELAY)
        bl(READ_PIN)
        lsl(r4, r4, 24)     # move it left 3 bytes
        orr(r6,  r4)       # bitwise or the pin into current word
        bl(DELAY)
        add(r1, r1, r5)   # add the index to the bytearra addres
        str(r6, [r1, 0])  # now 4 have been read store it
        sub(r1, r1, r5)   # reset the address
        add(r5, r5, 4)    # increase array index
        sub(r4, r2, r5)   # r4 - is now beig used to count bytes written
        bne(again)
        label(RETURN)
        mov(r0, r5)       # return number of bytes written
    def _parse_data(self, buffer_):
        # changed initial states, tyey are lost in the change over
        INIT_PULL_DOWN = 1
        INIT_PULL_UP = 2
        DATA_1_PULL_DOWN = 3
        DATA_PULL_UP = 4
        DATA_PULL_DOWN = 5
        #state = INIT_PULL_DOWN
        state = INIT_PULL_UP
        max_bits = 50
        bits = bytearray(max_bits)
        length = 0
        bit_ = 0
        for i in range(len(buffer_)):
            current = buffer_[i]
            length += 1
            if state == INIT_PULL_DOWN:
                if current == 0:
                    state = INIT_PULL_UP
                    continue
                else:
                    continue
            if state == INIT_PULL_UP:
                if current == 1:
                    state = DATA_1_PULL_DOWN
                    continue
                else:
                    continue
            if state == DATA_1_PULL_DOWN:
                if current == 0:
                    state = DATA_PULL_UP
                    continue
                else:
                    continue
            if state == DATA_PULL_UP:
                if current == 1:
                    length = 0
                    state = DATA_PULL_DOWN
                    continue
                else:
                    continue
            if state == DATA_PULL_DOWN:
                if current == 0:
                    bits[bit_] = length
                    bit_ += 1
                    state = DATA_PULL_UP
                    continue
                else:
                    continue
            if bit_ >= max_bits:
                break
        if bit_ == 0:
            return None
        results = bytearray(bit_)
        for i in range(bit_):
            results[i] = bits[i]
        return results
    def _calc_bytes(self, pull_up_lengths):
        shortest = 1000
        longest = 0
        for i in range(0, len(pull_up_lengths)):
            length = pull_up_lengths[i]
            if length < shortest:
                shortest = length
            if length > longest:
                longest = length
        halfway = shortest + (longest - shortest) / 2
        data = bytearray(5)
        did = 0
        byte = 0
        for i in range(len(pull_up_lengths)):
            byte = byte << 1
            if pull_up_lengths[i] > halfway:
                byte = byte | 1
            if ((i + 1) % 8 == 0):
                data[did] = byte
                did += 1
                byte = 0
        return data
    def _calc_checksum(self, data):
        return data[0] + data[1] + data[2] + data[3] & 0xff