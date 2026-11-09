💵 Calculadora de Troco e Cédulas em Python

Script em Python desenvolvido para calcular a diferença entre o valor cobrado em uma compra e o valor efetivamente pago pelo cliente,
determinando a decomposição exata do troco ou do saldo devedor nas cédulas disponíveis (R$ 10, R$ 5, R$ 1) e centavos restantes.

🛠️ Funcionalidades

Cálculo de Saldo e Troco: 

Determina se o valor pago cobre a compra, se há troco a ser devolvido ou se o cliente ainda possui saldo pendente.

Decomposição em Cédulas: Decompõe o valor calculado no menor número de notas possíveis considerando os valores de R$ 10, R$ 5, R$ 1 e a fração em centavos.

Formatação Dinâmica de Saída: Constrói frases legíveis e aplica pontuação gramatical (vírgulas e ponto final) de acordo com a quantidade de tipos de notas envolvidas.

📐Estrutura do Código

Funções 

Quantas_Notas_Cabem() Realiza as divisões inteiras (//) e operações de resto (%) para calcular a quantidade de notas de R$ 10, R$ 5, R$ 1 e centavos.

MontaMensagem() Mapeia os valores não nulos em strings legíveis e aplica a pontuação adequada à frase final. 

Set_Valor_Compra() Solicita o valor da compra via entrada de terminal (input).

Pergunta_Valores() Solicita o valor pago pelo cliente via entrada de terminal (input).

Calcular_Troco() Subtrai o valor pago do valor da compra.

Avalia_Troco() Avalia se o saldo é nulo (sem troco), positivo (valor pendente) ou negativo (troco a devolver).

Mensagem_final() Concatena a mensagem base com a lista de notas formatada e imprime no console.principal()Função principal (entry point) que orquestra a execução das demais funções.

💻 Exemplo de Uso no Terminal

Digite o valor em dinheiro a ser cobrado 
13.50
Digite o valor em dinheiro a ser pago 
50.00
Voce será pago em 3 notas de 10, 1 notas de 5, 1 notas de 1, 0.5 centavos.  

🚀 Como Executar 

Pré-requisitosPython 3.6+ instalado no ambiente.

ExecuçãoSalve o código em um arquivo com a extensão .py (exemplo: calculadora_troco.py).

Abra o terminal na pasta do arquivo e execute:Bashpython calculadora_troco.py
