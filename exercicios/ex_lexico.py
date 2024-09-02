import re

def token_transform(equacao):
    if re.search(r'[^0-9+\-*/() ]', equacao):
        raise ValueError("Expressão contém caracteres inválidos. Use apenas números e os operadores +, -, *, /, (, ).")

    token_pattern = re.compile(r'\d+\.?\d*|[+\-*/()]')
    tokens = token_pattern.findall(equacao)
    return tokens
    
def classificar_token(tokens):
    tokens_classificados = []
    
    for token in tokens:
        if re.match(r'^\d+\.?\d*$', token):
            tokens_classificados.append(('Numero', token))
        elif token == '+': 
            tokens_classificados.append(('Operador', 'SOMA'))
        elif token == '-':
            tokens_classificados.append(('Operador', 'SUB'))
        elif token == '*':  
            tokens_classificados.append(('Operador', 'MULT'))
        elif token == '/':
            tokens_classificados.append(('Operador', 'DIV'))
        elif token == '(': 
            tokens_classificados.append(('Parentese', 'PARESQ'))
        elif token == ')':  
            tokens_classificados.append(('Parentese', 'PARDIR'))    
    return tokens_classificados

equacao = input('Digite uma expressão básica utilizando e/ou +, -, *, /, =, (, ), numeros: ')
print("===== Analise =====")    
tokens = token_transform(equacao)

tokens_classificados = classificar_token(tokens)
for tipo, valor in tokens_classificados:
    print(f"Tipo: {tipo} -- Valor: {valor}")