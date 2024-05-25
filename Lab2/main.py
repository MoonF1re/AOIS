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

# Построение СДНФ и СКНФ
def build_sdnf_cnf(entries, terms_num, variables='abcde'):
    sdnf, cnf = [], []
    for entry in entries:
        combo, result = entry
        if result:
            sdnf.append(combo)
        else:
            cnf.append(combo)
    sdnf_expr = ' | '.join(' & '.join(f'{var}' if val else f'!{var}' for var, val in zip(variables[:terms_num], combo)) for combo in sdnf)
    cnf_expr = ' & '.join(f"({' | '.join(f'!{var}' if val else f'{var}' for var, val in zip(variables[:terms_num], combo))})" for combo in cnf)
    return sdnf_expr, cnf_expr

def to_decimal(binary_values):
    return int(''.join(str(b) for b in binary_values), 2)

def build_index_forms(entries):
    sdnf_indexes = [to_decimal(entry[0]) for entry in entries if entry[1]]
    cnf_indexes = [to_decimal(entry[0]) for entry in entries if not entry[1]]
    return sdnf_indexes, cnf_indexes

def indexed_form_to_decimal(indexed_form):
    return int(indexed_form, 2)


if __name__ == "__main__":
    user_input = input("Введите логическую функцию с использованием a, b, c, d, e и операций &, |, !, ->, ~: ")
    terms_num, tt_entries = generate_truth_table(user_input)

    print_truth_table(tt_entries, terms_num)

    sdnf, cnf = build_sdnf_cnf(tt_entries, terms_num)
    print(f"СДНФ: {sdnf}\nСКНФ: {cnf}\n")

    sdnf_indexes, cnf_indexes = build_index_forms(tt_entries)
    print(f"Числовые индексы для СДНФ: {sdnf_indexes}")
    print(f"Числовые индексы для СКНФ: {cnf_indexes}")

    indexed_form = ''.join(str(int(result)) for _, result in tt_entries)
    print(f"Индексная форма логической функции: {indexed_form} - {indexed_form_to_decimal(indexed_form)}")