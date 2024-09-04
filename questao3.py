# 3) Observe o trecho de código abaixo:
#   int INDICE = 12,
#   SOMA = 0, K = 1;
#   enquanto K < INDICE faça {
#       K = K + 1;
#       SOMA = SOMA + K;
#   }
#   imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?
# A resposta é 77, devido a ser uma progressa geometricam, pode-se calcular a soma da PA N(n-1)/2
# mas apenas usar a formula nao funcionara devido ao fato do numero 1 nao ser calculado
# por conta ficaria ((13*12)/ 2) - 1: que é 77


def progressao_aritmetica(idx: int) -> None:
    total: int = 0
    k: int = 1
    while k < idx:
        k += 1
        print(total)
        total += k
    print(total)


progressao_aritmetica(12)
# 77
