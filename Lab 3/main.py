import itertools


def replace_symbols(logic_function):
    replacements = {
        '!': ' not ',
        '&': ' and ',
        '|': ' or ',
        '->': ' <= ',
        '~': ' == ',
    }
    for old, new in replacements.items():
        logic_function = logic_function.replace(old, new)
    return logic_function


def evaluate(expression, values):
    a, b, c, d, e = (False,) * 5
    a, b, c, d, e = values + (False,) * (5 - len(values))
    expression = replace_symbols(expression)
    return eval(expression)


def generate_truth_table(expression, variables='abcde'):
    terms_num = sum(1 for var in variables if var in expression)
    table = list(itertools.product([0, 1], repeat=terms_num))
    processed_expr = replace_symbols(expression)
    results = [evaluate(processed_expr, row) for row in table]
    return terms_num, list(zip(table, results))


def print_truth_table(entries, terms_num, variables='abcde'):
    print("\nТаблица истинности:")
    headers = " ".join(variables[:terms_num]) + " | Result"
    print(headers)
    print("-" * len(headers))
    for combo, result in entries:
        print(" ".join(str(val) for val in combo), "|", int(result))
    print()
    return True


def build_sdnf_cnf(entries, terms_num, variables='abcde'):
    sdnf, cnf = [], []
    for entry in entries:
        combo, result = entry
        if result:
            sdnf.append(combo)
        else:
            cnf.append(combo)
    sdnf_expr = ' | '.join(
        ' & '.join(f'{var}' if val else f'!{var}' for var, val in zip(variables[:terms_num], combo)) for combo in sdnf)
    cnf_expr = ' & '.join(
        f"({' | '.join(f'!{var}' if val else f'{var}' for var, val in zip(variables[:terms_num], combo))})" for combo in
        cnf)
    return sdnf_expr, cnf_expr


def combine_terms(term1, term2):
    combined = []
    diff_count = 0
    for bit1, bit2 in zip(term1, term2):
        if bit1 == bit2:
            combined.append(bit1)
        else:
            combined.append('-')
            diff_count += 1
    return combined if diff_count == 1 else None


def find_prime_implicants(minterms):
    prime_implicants = set()
    while minterms:
        new_minterms = []
        used = set()
        for i, term1 in enumerate(minterms):
            for term2 in minterms[i + 1:]:
                combined = combine_terms(term1, term2)
                if combined:
                    print(f"Склеивание: {term1} и {term2} -> {combined}")
                    new_minterms.append(combined)
                    used.add(tuple(term1))
                    used.add(tuple(term2))
        prime_implicants.update(set(map(tuple, minterms)) - used)
        minterms = new_minterms
    return prime_implicants


def essential_prime_implicants(prime_implicants, minterms):
    essential = set()
    for term in minterms:
        covers = [implicant for implicant in prime_implicants if
                  all((bit == '-' or bit == t_bit) for bit, t_bit in zip(implicant, term))]
        if len(covers) == 1:
            essential.add(covers[0])
    return essential


def quine_mccluskey(entries, terms_num, is_sdnf=True):
    minterms = [entry[0] for entry in entries if entry[1] == is_sdnf]
    print(f"\nНачальные минтермы {'СДНФ' if is_sdnf else 'СКНФ'}: {minterms}")
    prime_implicants = find_prime_implicants(minterms)
    print(f"Простые импликанты: {prime_implicants}")
    essential_implicants = essential_prime_implicants(prime_implicants, minterms)
    remaining_minterms = [term for term in minterms if not any(
        all((bit == '-' or bit == t_bit) for bit, t_bit in zip(implicant, term)) for implicant in essential_implicants)]
    return essential_implicants, remaining_minterms


def format_implicant(implicant, terms_num, variables='abcde', is_sdnf=True):
    logic = ' & ' if is_sdnf else ' | '
    formatted = logic.join(
        f'{var}' if bit == '1' else f'!{var}' for var, bit in zip(variables[:terms_num], implicant) if bit != '-')
    return formatted


def print_result(essential_implicants, terms_num, variables='abcde', is_sdnf=True):
    if not essential_implicants:
        print("No essential implicants found.")
        return

    formatted_implicants = [format_implicant(implicant, terms_num, variables, is_sdnf) for implicant in
                            essential_implicants]
    logic = ' | ' if is_sdnf else ' & '
    result = logic.join(formatted_implicants)
    print(f"\nРезультат минимизации {'СДНФ' if is_sdnf else 'СКНФ'}:")
    print(result)
    return True


def create_prime_implicant_chart(prime_implicants, minterms):
    chart = {tuple(minterm): [implicant for implicant in prime_implicants if
                              all((bit == '-' or bit == t_bit) for bit, t_bit in zip(implicant, minterm))] for minterm
             in minterms}
    return chart


def print_prime_implicant_chart(chart):
    for minterm, implicants in chart.items():
        minterm_str = ''.join(str(bit) for bit in minterm)
        implicants_str = ', '.join(''.join(implicant) for implicant in implicants)
        print(f"{minterm_str}: {implicants_str}")
    print()
    return True


def quine_mccluskey_with_chart(entries, terms_num, is_sdnf=True):
    minterms = [entry[0] for entry in entries if entry[1] == is_sdnf]
    print(f"\nНачальные минтермы {'СДНФ' if is_sdnf else 'СКНФ'}: {minterms}")
    prime_implicants = find_prime_implicants(minterms)
    print(f"Простые импликанты: {prime_implicants}")
    essential_implicants = essential_prime_implicants(prime_implicants, minterms)
    remaining_minterms = [term for term in minterms if not any(
        all((bit == '-' or bit == t_bit) for bit, t_bit in zip(implicant, term)) for implicant in essential_implicants)]
    chart = create_prime_implicant_chart(prime_implicants, remaining_minterms)
    return essential_implicants, remaining_minterms, chart


def to_decimal(binary_values):
    return int(''.join(str(b) for b in binary_values), 2)


def create_kmap(entries, terms_num, is_sdnf=True):
    size = 2 ** ((terms_num + 1) // 2)  # Adjust size calculation to handle different number of variables
    kmap = [[None for _ in range(size)] for _ in range(size)]
    for combo, result in entries:
        if (is_sdnf and result) or (not is_sdnf and not result):
            row = to_decimal(combo[:len(combo) // 2])
            col = to_decimal(combo[len(combo) // 2:])
            kmap[row][col] = 1
    return kmap


def print_kmap(kmap):
    print("\nКарта Карно:")
    for row in kmap:
        print(" ".join('.' if x is None else str(x) for x in row))
    print()


def karno_minimize(entries, terms_num, is_sdnf=True):
    kmap = create_kmap(entries, terms_num, is_sdnf)
    print_kmap(kmap)
    return True
    # Here should be the implementation of minimization using the Karnaugh map.


# Full program example usage
# if __name__ == "__main__":
#     user_input = input("Введите логическую функцию с использованием a, b, c, d, e и операций &, |, !, ->, ~: ")
#     terms_num, entries = generate_truth_table(user_input)
#
#     print_truth_table(entries, terms_num)
#
#     sdnf, cnf = build_sdnf_cnf(entries, terms_num)
#     print(f"СДНФ: {sdnf}\nСКНФ: {cnf}\n")
#
#     # Calculation Method
#     print("Минимизация СДНФ расчетным методом:")
#     essential_implicants, remaining_minterms = quine_mccluskey(entries, terms_num, is_sdnf=True)
#     print_result(essential_implicants, terms_num, is_sdnf=True)
#
#     print("Минимизация СКНФ расчетным методом:")
# essential_implicants, remaining_minterms = quine_mccluskey(entries, terms_num, is_sdnf=False)
# print_result(essential_implicants, terms_num, is_sdnf=False)
#
# # Calculation-Table Method
# print("Минимизация СДНФ расчетно-табличным методом:")
# essential_implicants, remaining_minterms, chart = quine_mccluskey_with_chart(entries, terms_num, is_sdnf=True)
# print_result(essential_implicants, terms_num, is_sdnf=True)
# print_prime_implicant_chart(chart)
#
# print("Минимизация СКНФ расчетно-табличным методом:")
# essential_implicants, remaining_minterms, chart = quine_mccluskey_with_chart(entries, terms_num, is_sdnf=False)
# print_result(essential_implicants, terms_num, is_sdnf=False)
# print_prime_implicant_chart(chart)
#
# # Karnaugh Map Method
# print("Минимизация СДНФ табличным методом (карта Карно):")
# karno_minimize(entries, terms_num, is_sdnf=True)
#
# print("Минимизация СКНФ табличным методом (карта Карно):")
# karno_minimize(entries, terms_num, is_sdnf=False)

