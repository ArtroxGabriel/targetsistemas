def number_of_A(string: str):
    """Questao 2: retornar o numero de 'a' de uma deterninada string"""
    string = string.lower()
    count: int = 0
    for i in string:
        if i == "a":
            count += 1
    return count


print(number_of_A(input()))
