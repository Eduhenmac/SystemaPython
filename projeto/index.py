from banco import Banco_de_Dados as Banco
from vendedor import Vendedor
from produto import Produto

print("Bem vindo")
print("Deseja continuar? (S/N)")
continuar = input().strip().upper()
if (continuar == "S"):
    opcao = 0
    while (opcao != 6):
        print("=====Menu Principal=====")
        print("1 - Adicionar vendedor:")
        print("2 - Adicionar Produto:")
        print("3 - Mostrar produtos:")
        print("4 - Mostrar vendedores:")
        print("5 - Mostrar maior venda:")
        print("6 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        match opcao:
            case 1:
                nome = input("Digite o nome do vendedor: ")
                empresa = input("Digite o nome da empresa: ")
                vendedor = Vendedor(nome, 0, empresa)
                banco = Banco()
                banco.inserir_vendedor(vendedor)    
            case 2:
                print("====Vendedores disponiveis:====")
                banco = Banco()
                vendedores = banco.selecionar_vendedor()
                for vendedor in vendedores:
                    print(vendedor.toString())
                
                vendedor = input("Digite o número do vendedor para este produto: ")    
                nome = input("Digite o nome do produto: ")
                preco = float(input("Digite o preço do produto: "))
                empresa = input("Digite a empresa do produto: ")
                produto = Produto(nome=nome, preco=preco, empresa=empresa, vendedor=vendedor, numero=0)
                banco.inserir_produto(produto)
            case 3:
                banco = Banco()
                produtos = banco.selecionar_produto()
                if (produtos == []):
                    print("Não existem produtos cadastrados")
                else:
                    print("====Produtos cadastrados=====")  
                    for produto in produtos:
                        print(produto.toString())
            case 4:
                banco = Banco() 
                vendedores = banco.selecionar_vendedor()
                if (vendedores == []):
                    print("Não existem vendedores cadastrados")
                else:
                    print("====Vendedores cadastrados=====")
                    for vendedor in vendedores:
                        print(vendedor.toString())  
            case 5:
                banco = Banco()
                maior_venda = banco.selecionar_vendedor_com_maior_valor_produtos()
                valor_venda = banco.selecionar_valor_venda()
                produtos = banco.selecionar_produto_por_vendedor(maior_venda.get_numero())
                lista_vendedores = banco.selecionar_vendedor_valor()
                maior_venda_unica = banco.selecionar_maior_venda(maior_venda)
                if maior_venda_unica is None:
                    print("Não existem produtos cadastrados")
                if lista_vendedores == []:
                    print("Não existem vendedores cadastrados")
                if produtos == []:
                    print("Não existem produtos cadastrados para este vendedor")
                if (maior_venda is None and valor_venda is None):
                    print("Não existem vendas cadastradas") 
                else:
                    print("====Analise de vendas=====")
                    print("Total de vendas de", maior_venda.get_nome(), ": R$", valor_venda)
                    print("\n")
                    print("Produtos do vendedor:", maior_venda.get_nome())
                    for produto in produtos:
                        print("Nome do produto:", produto.get_nome())
                        print("Preço do produto:", produto.get_preco())
                        print("Marca do produto:", produto.get_empresa())
                    print("\n")
                    print("Comparação de Vendas:")
                    for vendedor, preco in lista_vendedores:
                        if(preco == None):
                            preco = 0
                        print(vendedor.get_numero(),"Vendedor:", vendedor.get_nome(), " R$", preco)
                    print("\n")
                    print("Maior venda: ", maior_venda_unica.get_preco())

                        

                    

            case 6:
                print("Saindo do sistema...")
                exit()
            case _:
                print("Opção inválida, tente novamente.")
        if (opcao == 6):
            print("Saindo do sistema...")
            exit()
else:
    print("Obrigado por utilizar nosso sistema")