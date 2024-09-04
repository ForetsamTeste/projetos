def calcular_nota_algebra():
    print("1º Nota: Prova (40%); 2º Nota: Trabalho em grupo (60%).")
    p1 = float(input("Digite a nota da prova: "))
    t2 = float(input("Digite a nota do trabalho: "))

    se = input("Participou na semana de engenharia? (s/n): ").lower()
    n1 = p1
    n2 = t2

    if se == "s":
        if n2 >= 9:
            n2 = 9
        nota_atual = n1 * 0.4 + n2 * 0.6 + 0.6
    elif se == "n":
        nota_atual = n1 * 0.4 + n2 * 0.6
    else:
        print("Opção inválida. Responda com s ou n.")
        return 

    if nota_atual < 5.75:
        nota_faltando = 5.75 - nota_atual
        print(f"Sua nota atual é: {nota_atual:.2f}, você precisa de mais: {nota_faltando:.2f} para passar.")
        menu_principal()
    else:
        print(f"Você passou com a nota: {nota_atual:.2f}")
        menu_principal()

def calcular_nota_calculo():
    atividades=[]
    print("1º Nota: Prova (40%); 2º Nota: Prova (42%) + Média Atividades (18%).")
    np1 = float(input("Digite a nota da prova 1: "))
    np2 = float(input("Digite a nota da prova 2: "))
    ma = input("Digite a nota da sua atividade (ou digite 'sair' para calcular a média): ")

    while ma != "sair":
        if ma == "":
            print("Atividade vazia, digite um número ou sair.")
        else:
            try:
                atividade = float(ma)
                atividades.append(atividade)
            except ValueError or ma == "":
                print("Entrada inválida. Por favor, digite um número ou 'sair'.")
            
        ma = input("Digite a nota da sua atividade (ou digite 'sair' para calcular a média): ")

    if atividades:
        ma_media = sum(atividades) / len(atividades)
    else:
        print("Nenhuma atividade foi inserida.")
        return

    se = input("Participou na semana de engenharia? (s/n): ").lower()
    n1 = np1
    n2 = np2*0.7 + ma_media*0.3

    if se == "s":
        if n2 >= 9:
            n2 = 9
        nota_atual = n1 * 0.4 + n2 * 0.6 + 0.6
    elif se == "n":
        nota_atual = n1 * 0.4 + n2 * 0.6
    else:
        print("Opção inválida. Responda com s ou n.")
        return 

    if nota_atual < 5.75:
        nota_faltando = 5.75 - nota_atual
        print(f"Sua nota atual é: {nota_atual:.2f}, você precisa de mais: {nota_faltando:2f} para passar.")
        menu_principal()
    else:
        print(f"Você passou com a nota: {nota_atual:2f}")
        menu_principal()

def calcular_nota_engenharia_inovacao(): 
    print("1º Nota: Prova (40%); 2º Nota: Prova (60%).")
    np1 = float(input("Digite a nota da prova 1: "))
    np2 = float(input("Digite a nota da prova 2: "))

    se = input("Participou na semana de engenharia? (s/n): ").lower()
    n1 = np1
    n2 = np2

    if se == "s":
        if n2 >= 9:
            n2 = 9
        nota_atual = n1 * 0.4 + n2 * 0.6 + 0.6
    elif se == "n":
        nota_atual = n1 * 0.4 + n2 * 0.6
    else:
        print("Opção inválida. Responda com s ou n.")
        return 

    if nota_atual < 5.75:
        nota_faltando = 5.75 - nota_atual
        print(f"Sua nota atual é: {nota_atual:.2f}, você precisa de mais: {nota_faltando:.2f} para passar.")
        menu_principal()
    else:
        print(f"Você passou com a nota: {nota_atual:.2f}")
        menu_principal()

def calcular_nota_fisica():
    atividades=[]
    atividades2=[]
    print("1º Nota: Media das atividades (40%); 2º Nota: Media das atividades (42%) + Prova (18%).")
    ma = input("Digite a nota da sua atividade (ou digite 'sair' para calcular a média): ")

    while ma != "sair":
        if ma == "":
            print("Atividade vazia, digite ou número ou use sair.")
        else:
            try:
                atividade = float(ma)
                atividades.append(atividade)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número ou 'sair'.")
        
        ma = input("Digite a nota da sua atividade (ou digite 'sair' para calcular a média): ")

    if atividades:
        ma_media = sum(atividades) / len(atividades)
    else:
        print("Nenhuma atividade foi inserida.")
        return
    
    ma2 = input("Digite a nota da sua atividade 2 (ou digite 'sair' para calcular a média): ")

    while ma2 != "sair":
        if ma2 == "":
            print("Atividade não inseridade, use sair ou digite um número.")
        else:
            try:
                atividade2 = float(ma2)
                atividades2.append(atividade2)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número ou 'sair'.")
        
        ma2 = input("Digite a nota da sua atividade (ou digite 'sair' para calcular a média): ")

    if atividades:
        ma2_media = sum(atividades2) / len(atividades2)
    else:
        print("Nenhuma atividade foi inserida.")
        return
    
    np2 = float(input("Digite a nota da prova 2: "))
    

    se = input("Participou na semana de engenharia? (s/n): ").lower()
    n1 = ma_media
    n2 = np2*0.3 + ma2_media*0.7

    if se == "s":
        if n2 >= 9:
            n2 = 9
        nota_atual = n1 * 0.4 + n2 * 0.6 + 0.6
    elif se == "n":
        nota_atual = n1 * 0.4 + n2 * 0.6
    else:
        print("Opção inválida. Responda com s ou n.")
        return 

    if nota_atual < 5.75:
        nota_faltando = 5.75 - nota_atual
        print(f"Sua nota atual é: {nota_atual:.2f}, você precisa de mais: {nota_faltando:2f} para passar.")
        menu_principal()
    else:
        print(f"Você passou com a nota: {nota_atual:2f}")
        menu_principal()


def calcular_nota_grafos():
    print("1º Nota: Prova (40%); 2º Nota: Prova 2 (60%).")
    p1 = float(input("Digite a nota da prova: "))
    p2 = float(input("Digite a nota do prova 2: "))

    se = input("Participou na semana de engenharia? (s/n): ").lower()
    n1 = p1
    n2 = p2

    if se == "s":
        if n2 >= 9:
            n2 = 9
        nota_atual = n1 * 0.4 + n2 * 0.6 + 0.6
    elif se == "n":
        nota_atual = n1 * 0.4 + n2 * 0.6
    else:
        print("Opção inválida. Responda com s ou n.")
        return 

    if nota_atual < 5.75:
        nota_faltando = 5.75 - nota_atual
        print(f"Sua nota atual é: {nota_atual:.2f}, você precisa de mais: {nota_faltando:.2f} para passar.")
        menu_principal()
    else:
        print(f"Você passou com a nota: {nota_atual:.2f}")
        menu_principal()

def calcular_nota_compiladores():
    print("1º Nota: Prova (40%); 2º Nota: Prova 2 (60%).")
    p1 = float(input("Digite a nota da prova: "))
    p2 = float(input("Digite a nota do prova 2: "))

    se = input("Participou na semana de engenharia? (s/n): ").lower()
    n1 = p1
    n2 = p2

    if se == "s":
        if n2 >= 9:
            n2 = 9
        nota_atual = n1 * 0.4 + n2 * 0.6 + 0.6
    elif se == "n":
        nota_atual = n1 * 0.4 + n2 * 0.6
    else:
        print("Opção inválida. Responda com s ou n.")
        return 

    if nota_atual < 5.75:
        nota_faltando = 5.75 - nota_atual
        print(f"Sua nota atual é: {nota_atual:.2f}, você precisa de mais: {nota_faltando:.2f} para passar.")
        menu_principal()
    else:
        print(f"Você passou com a nota: {nota_atual:.2f}")
        menu_principal()

def calcular_nota_teoria_economica():
    atividades=[]
    atividades2=[]
    print("1º Nota: Prova (30%) e Atividades(10%); 2º Nota: Prova(40%) e atividades (20%).")
    ma = input("Digite a nota da sua atividade (ou digite 'sair' para calcular a média): ")

    while ma != "sair":
        if ma == "":
            print("Entrada invalida. Use sair ou digite um número.")
        else:
            try:
                atividade = float(ma)
                atividades.append(atividade)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número ou 'sair'.")
        
        ma = input("Digite a nota da sua atividade (ou digite 'sair' para calcular a média): ")

    if atividades:
        ma_media = sum(atividades) / len(atividades)
    else:
        print("Nenhuma atividade foi inserida.")
        return
    
    np1 = float(input("Digite a nota da prova 2: "))

    ma2 = input("Digite a nota da sua atividade 2 (ou digite 'sair' para calcular a média): ")

    while ma2 != "sair":
        if ma2 == "":
            print("Entrada inválidade, digite um número ou use sair.")
        else:
            try:
                atividade2 = float(ma2)
                atividades2.append(atividade2)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número ou 'sair'.")
        
        ma2 = input("Digite a nota da sua atividade (ou digite 'sair' para calcular a média): ")

    if atividades:
        ma2_media = sum(atividades2) / len(atividades2)
    else:
        print("Nenhuma atividade foi inserida.")
        return
    
    np2 = float(input("Digite a nota da prova 2: "))
    
    se = input("Participou na semana de engenharia? (s/n): ").lower()
    n1 = np1*0.75 + ma_media*0.25
    n2 = np2*0.66 + ma2_media*0.33

    if se == "s":
        if n2 >= 9:
            n2 = 9
        nota_atual = n1 * 0.4 + n2 * 0.6 + 0.6
    elif se == "n":
        nota_atual = n1 * 0.4 + n2 * 0.6
    else:
        print("Opção inválida. Responda com s ou n.")
        return 

    if nota_atual < 5.75:
        nota_faltando = 5.75 - nota_atual
        print(f"Sua nota atual é: {nota_atual:.2f}, você precisa de mais: {nota_faltando:2f} para passar.")
        menu_principal()
    else:
        print(f"Você passou com a nota: {nota_atual:2f}")
        menu_principal()

def calcular_nota_ead():
    print("Atividade 1 = 1 ponto; Atividades 3,4 = 2 pontos ; Atividades 5,6,8,9,10 = 1 ponto ; atividade participativa = 5 pontos ; Prova Final = 5 pontos")
    a1 = float(input("Digite a nota da atividade 1: "))
    a3 = float(input("Digite a nota da atividade 3: "))
    a4 = float(input("Digite a nota da atividade 4: "))
    ap = float(input("Digite a nota da atividade participativa: "))
    a5 = float(input("Digite a nota da atividade 5: "))
    a6 = float(input("Digite a nota da atividade 6: "))
    a8 = float(input("Digite a nota da atividade 8: "))
    a9 = float(input("Digite a nota da atividade 9: "))
    a10 = float(input("Digite a nota da atividade 10: "))
    pf = float(input("Digite a nota da Prova Final: "))

    se = input("Participou na semana de engenharia? (s/n): ").lower()
    n1 = a1+a3+a4+ap
    n2 = a5+a6+a8+a9+a10+pf

    if se == "s":
        if n2 >= 9:
            n2 = 9
        nota_atual = n1 * 0.4 + n2 * 0.6 + 0.6
    elif se == "n":
        nota_atual = n1 * 0.4 + n2 * 0.6
    else:
        print("Opção inválida. Responda com s ou n.")
        return 

    if nota_atual < 5.75:
        nota_faltando = 5.75 - nota_atual
        print(f"Sua nota atual é: {nota_atual:.2f}, você precisa de mais: {nota_faltando:.2f} para passar.")
        menu_principal()
    else:
        print(f"Você passou com a nota: {nota_atual:.2f}")
        menu_principal()

def menu_principal():
    print("AL: Álgebra; CA: Cálculo; EI: Engenharia e Inovação; FM: Física; GR: Grafos; CO: Compiladores; TE: Teoria Econômica; EAD.")
    print("0,6 pontos na média se participar da semana da engenharia com 3 certificados, valendo 6h no total.")
    
    nota = input("Selecione a matéria: ").upper()
    
    if nota == "AL":
        calcular_nota_algebra()
    elif nota == "CA":
        calcular_nota_calculo()
    elif nota == "EI":
        calcular_nota_engenharia_inovacao()
    elif nota == "FM":
        calcular_nota_fisica()
    elif nota == "GR":
        calcular_nota_grafos()
    elif nota == "CO":
        calcular_nota_compiladores()
    elif nota == "TE":
        calcular_nota_teoria_economica()
    elif nota == "EAD":
        calcular_nota_ead()
    else:
        print("Responda com as opções descritas acima.")
        return

menu_principal()