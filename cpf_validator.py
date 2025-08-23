def validate_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_digit(cpf_part):
        s = sum(int(a) * b for a, b in zip(cpf_part, range(len(cpf_part)+1, 1, -1)))
        d = 11 - s % 11
        return d if d < 10 else 0

    digit1 = calc_digit(cpf[:9])
    digit2 = calc_digit(cpf[:9] + str(digit1))

    return cpf[-2:] == f"{digit1}{digit2}"