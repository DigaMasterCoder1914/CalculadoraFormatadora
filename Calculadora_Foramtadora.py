
def Quantas_Notas_Cabem(Valor_Troco : float):


    Valor_calcular = abs(Valor_Troco);

    Notas_de_10 = 0
    Notas_de_5 = 0
    Notas_de_1 = 0
    Restante_centavos = 0.0

    if Valor_calcular >= 10:
        Notas_de_10 = int(Valor_calcular // 10);
        Valor_calcular =  Valor_calcular % 10;
    if Valor_calcular >= 5:
        Notas_de_5 = int(Valor_calcular // 5);
        Valor_calcular =  Valor_calcular % 5;
    if  Valor_calcular >= 1:
        Notas_de_1 = int(Valor_calcular // 1);
        Valor_calcular =  Valor_calcular % 1;
    if Valor_calcular < 1:
        Restante_centavos = Valor_calcular;

    Total_Notas = [Notas_de_10, Notas_de_5,Notas_de_1,Restante_centavos];

    return Total_Notas;
     
#Monta a Str de exibição
def MontaMensagem(Lista : list):

    Parte_1 = ' ';
    Parte_2 = ' ';
    Parte_3 = ' ';
    Parte_4 = ' ';

    Contador_Pontuacao = 0;

    Lista_Pontuacao= [False,False,False,False];
    Lista_Partes_Mensagem = [Parte_1, Parte_2,Parte_3,Parte_4]
    Lista_Final = [];

    for indice,valor in enumerate(Lista):

        if indice == 0 and valor >= 1:
            Lista_Partes_Mensagem[indice] = f'{valor } notas de 10';
            Lista_Pontuacao[indice] = True;
            Contador_Pontuacao += 1;
        if indice == 1 and valor >= 1:
            Lista_Partes_Mensagem[indice] = f'{valor } notas de 5';
            Lista_Pontuacao[indice] = True;
            Contador_Pontuacao += 1;
        if indice == 2 and valor >= 1:
            Lista_Partes_Mensagem[indice] = f'{valor } notas de 1';
            Lista_Pontuacao[indice] = True;
            Contador_Pontuacao += 1;
        if indice == 3  and valor >= 0.1:
            Lista_Partes_Mensagem[indice] = f'{valor} centavos';
            Lista_Pontuacao[indice] = True; 
            Contador_Pontuacao += 1;

    for indice,valor in enumerate(Lista_Pontuacao):
            if(Lista_Pontuacao[indice] == True):
                Lista_Final.append(Lista_Partes_Mensagem[indice]);

    for indice,valor in enumerate(Lista_Final):
           
            if(Contador_Pontuacao > 1):
                Lista_Final[indice] = f'{Lista_Final[indice]},'
                Contador_Pontuacao -= 1;
            else:
                Lista_Final[indice] = f'{Lista_Final[indice]}.'
                Contador_Pontuacao -= 1;   

    return  Lista_Final;

        # compara indice com os restos,se  
        # procura os indices verdadeiros e falsos 
        #  
                              
#Define o valor da compra
def Set_Valor_Compra():

    Valor_Compra = float(input('Digite o valor em dinheiro a ser cobrado \n'));
    return Valor_Compra;


# pergunta quanto em dinheiro foi dado
def Pergunta_Valores():
    Numero = float(input('Digite o valor em dinheiro a ser pago \n'));
    return Numero;


# calcula o troco
def Calcular_Troco(Valor_Compra :float,Valor_Pago: float):
    Valor_Troco = Valor_Compra - Valor_Pago;
    return Valor_Troco;


# avalia se teve troco
def Avalia_Troco(valor_Troco : float):

    Lista_Notas = [];


    if valor_Troco == 0:
        print('Não há troco a ser dado');
    elif valor_Troco > 0 :
        print(f'Voce ainda Deve {valor_Troco} reais')
        Lista_Notas = Quantas_Notas_Cabem(Valor_Troco = valor_Troco );
        Mensagem_final(MontaMensagem(Lista = Lista_Notas ),Mensagem = 'Voce pode pagar em ');
    else :
       Lista_Notas = Quantas_Notas_Cabem(Valor_Troco = valor_Troco );
       Mensagem_final(MontaMensagem(Lista = Lista_Notas ),Mensagem = 'Voce será pago em');


#Exibe mensagem final
def Mensagem_final(Lista: list,Mensagem : str):


   print(f'{Mensagem} {" ".join(Lista)}');

def principal():


    
    Valor_Compra_Usuario = Set_Valor_Compra();
    Valor_Pago_Usuario = Pergunta_Valores();
    Valor_Troco_Funcao = Calcular_Troco(Valor_Compra = Valor_Compra_Usuario,Valor_Pago = Valor_Pago_Usuario);    
    Avalia_Troco(valor_Troco = Valor_Troco_Funcao);

    

if __name__ == '__main__':
    principal();



#Algoritimo

#Define o valor da compra - float
# pergunta Quanto ele deu em dinheiro - float


   # calcula troco como -> valor da compra  -  valor pago 


      #  #se for igual:
       # imprime que não há troco 
    #se for maior que 0  :
              # imprime o que falta a ser pago 


#se o restuldo for menor que 0: -else-   
    # calcular valor pago - valor da compra
    #pega o troco e ve quanto dele cab exatamento em 10 
    #em 5 
    #em 1


    #pega os valores e retorna num String
  

 
