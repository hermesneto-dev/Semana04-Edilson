# Este módulo demonstra listas, conjuntos, tuplas e ordenação de produtos.
# Cada função foi separada para deixar a solução organizada e fácil de testar.

"""Semana 04 - Estruturas de dados e equivalência lógica em Portugal."""


# Solicita os dados e devolve uma lista de dicionários, um por produto.
def ler_produtos():
    # A lista começa vazia e recebe novos produtos com append().
    produtos = []
    quantidade = int(input("Quantos produtos deseja cadastrar? "))
    # O laço repete a leitura exatamente a quantidade informada.
    for indice in range(quantidade):
        print(f"\nProduto {indice + 1}")
        nome = input("Nome: ").strip()
        preco = float(input("Preço: R$ ").replace(",", "."))
        categoria = input("Categoria: ").strip()
        produtos.append({"nome": nome, "preco": preco, "categoria": categoria})
    return produtos


# Imprime qualquer coleção de produtos usando f-string.
def mostrar_produtos(titulo, produtos):
    print(f"\n{titulo}")
    if not produtos:
        print("Nenhum produto encontrado.")
        return
    for produto in produtos:
        print(f"- {produto['nome']} | R$ {produto['preco']:.2f} | {produto['categoria']}")


# Reproduz a lógica sem depender das estruturas prontas do Python.
def versao_portugal(produtos):
    """Equivalente didático usando vetor fixo, laços e bubble sort."""
    vetor = [None] * len(produtos)
    for indice in range(len(produtos)):
        vetor[indice] = produtos[indice]

    # Ordenação manual pelo método da bolha.
    for limite in range(len(vetor) - 1, 0, -1):
        for indice in range(limite):
            if vetor[indice]["preco"] > vetor[indice + 1]["preco"]:
                vetor[indice], vetor[indice + 1] = vetor[indice + 1], vetor[indice]

    # Simulação manual de conjunto, ignorando categorias repetidas.
    # A lista representa manualmente um conjunto sem valores repetidos.
    categorias_unicas = []
    for produto in vetor:
        repetida = False
        for categoria in categorias_unicas:
            if categoria == produto["categoria"]:
                repetida = True
        if not repetida:
            categorias_unicas.append(produto["categoria"])

    print("\nVersão equivalente em Portugal (vetor/bubble sort):")
    for produto in vetor:
        print(f"- {produto['nome']} | R$ {produto['preco']:.2f}")
    print(f"Categorias sem repetição: {categorias_unicas}")


# Função principal: coordena entrada, processamento e apresentação do relatório.
def main():
    print("=== Cadastro e análise de produtos ===")
    try:
        produtos = ler_produtos()
        if not produtos:
            print("Cadastre pelo menos um produto.")
            return
        valor_filtro = float(input("\nMostrar produtos acima de R$ ").replace(",", "."))
        mostrar_produtos("Produtos filtrados", [p for p in produtos if p["preco"] > valor_filtro])
        ordem_crescente = produtos.copy()
        ordem_crescente.sort(key=lambda p: p["preco"])
        ordem_decrescente = sorted(produtos, key=lambda p: p["preco"], reverse=True)
        mostrar_produtos("Ordem crescente", ordem_crescente)
        mostrar_produtos("Ordem decrescente", ordem_decrescente)
        categorias = {produto["categoria"] for produto in produtos}
        precos = [produto["preco"] for produto in produtos]
        estatisticas = (min(precos), max(precos), sum(precos) / len(precos))
        print(f"\nCategorias únicas: {', '.join(sorted(categorias))}")
        print(f"Estatísticas (menor, maior, média): R$ {estatisticas[0]:.2f}, R$ {estatisticas[1]:.2f}, R$ {estatisticas[2]:.2f}")
        versao_portugal(produtos)
    except ValueError:
        print("Entrada inválida: informe números válidos para quantidade e preços.")


if __name__ == "__main__":
    main()
