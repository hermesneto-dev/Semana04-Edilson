// Semana 04: cadastro e análise de produtos em Portugol.
// Esta versão usa vetor de tamanho fixo, laços e bubble sort.
programa {
    funcao inicio() {
        // Vetores paralelos representam nome, preço e categoria.
        cadeia nomes[10]
        cadeia categorias[10]
        real precos[10]
        inteiro quantidade, i, j
        escreva("Quantidade de produtos (máximo 10): ")
        leia(quantidade)

        // Leitura dos dados para o vetor.
        para (i = 0; i < quantidade; i++) {
            escreva("Nome: ")
            leia(nomes[i])
            escreva("Preço: ")
            leia(precos[i])
            escreva("Categoria: ")
            leia(categorias[i])
        }

        // Bubble sort: troca vizinhos fora de ordem até ordenar os preços.
        para (i = 0; i < quantidade - 1; i++) {
            para (j = 0; j < quantidade - i - 1; j++) {
                se (precos[j] > precos[j + 1]) {
                    real preco_aux = precos[j]
                    precos[j] = precos[j + 1]
                    precos[j + 1] = preco_aux
                    cadeia nome_aux = nomes[j]
                    nomes[j] = nomes[j + 1]
                    nomes[j + 1] = nome_aux
                }
            }
        }

        escreva("\nProdutos em ordem crescente:\n")
        para (i = 0; i < quantidade; i++) {
            escreva(nomes[i], " - R$ ", precos[i], "\n")
        }
        // A média é calculada manualmente percorrendo o vetor.
        real soma = 0
        para (i = 0; i < quantidade; i++) soma = soma + precos[i]
        escreva("Média dos preços: R$ ", soma / quantidade, "\n")
    }
}
