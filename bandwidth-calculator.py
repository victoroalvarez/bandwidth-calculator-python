# bandwidth calculator

# bit-rate and byte-rate variables
megaBitsSecond = 0.0

megaBytesSecond = 0.0

# ask for bit-rate in mega bits per second
print "Enter your bit-rate in mega bits per second:"
megaBitsSecond = float(raw_input("Bit-rate >"))

# calculate byte-rate in mega bytes per second
megaBytesSecond = megaBitsSecond / 8

# print final byte-rate value
print "Your Byte-rate in Mega bytes per second rate is: \n%r MB/s" % megaBytesSecond

