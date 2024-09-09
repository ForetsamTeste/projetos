import re  # Importa a biblioteca 're' para trabalhar com expressões regulares

# Função que transforma uma equação em uma lista de tokens
def token_transform(equacao):
    # Verifica se a equação contém caracteres inválidos (qualquer coisa que não seja números, operadores ou parênteses)
    if re.search(r'[^0-9+\-*/() ]', equacao):
        # Se encontrar algum caractere inválido, lança um erro
        raise ValueError("Expressão contém caracteres inválidos. Use apenas números e os operadores +, -, *, /, (, ).")
    
    # Cria um padrão de expressão regular para identificar números e operadores matemáticos (+, -, *, /, parênteses)
    token_pattern = re.compile(r'\d+\.?\d*|[+\-*/()]')
    
    # Aplica o padrão à equação para encontrar todos os tokens correspondentes
    tokens = token_pattern.findall(equacao)
    
    # Retorna a lista de tokens encontrados
    return tokens

# Função que classifica os tokens em categorias, como números e operadores
def classificar_token(tokens):
    tokens_classificados = []  # Lista para armazenar os tokens classificados
    
    # Percorre cada token encontrado e separa eles em números, operadores ou parentesis
    for token in tokens:
        # Se o token for um número (inteiro ou decimal)
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
    
    # Retorna a lista de tokens classificados
    return tokens_classificados

# Solicita ao usuário uma expressão matemática
equacao = input('Digite uma expressão básica utilizando e/ou +, -, *, /, =, (, ), numeros: ')

print("===== Analise =====")  # Exibe um título para os resultados

# Chama a função que transforma a equação em tokens
tokens = token_transform(equacao)

# Chama a função que classifica os tokens encontrados
tokens_classificados = classificar_token(tokens)

# Percorre sobre a lista de tokens classificados e imprime o tipo e o valor de cada token
for tipo, valor in tokens_classificados:
    print(f"Tipo: {tipo} -- Valor: {valor}")
