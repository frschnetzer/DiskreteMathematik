# Multiplicating a number by 14 with bit shifting
def MultiplicateWith14(digit):
    return (digit << 1) + (digit << 2) + (digit << 3) # (digit << 1) = 2, (digit << 2) = 4, (digit << 3) = 8 => 2+4+8 = 14

print(MultiplicateWith14(5))