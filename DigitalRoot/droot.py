def digital_root(n):
    dig_root = str(n)
    a = 0
    # We will see here if we have the desired length of the digital root
    if len(dig_root) ==  1:
        return int(n)
    else:
        for i in dig_root:
            a += int(i)
        num = str(a)
        # This is the most interesting thing. Our digital root will execute itself again and we will only have an output if the length is 1
        return digital_root(num)
