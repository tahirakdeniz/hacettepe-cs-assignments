print([number for number in range(2, 50) if all([number%divisor != 0 for divisor in range(2, number)])])