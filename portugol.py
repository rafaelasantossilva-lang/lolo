
print("---CARDÁPIO---")
print("1 - Cookie(R$ 5,00)")
print("2 - Sorvete(R$ 3,00)")
print("3 - Bolo(R$ 4,00)")
print("4 - Cupcake(R$ 6,00)")
print("5 - Chocolate Quente(R$ 4,00)")
print("6 - Chá(R$ 2,00)")
print("7 - Café(R$ 1,00)")
print("8 - Panqueca(R$ 5,00)")
print("9 - Croissant(R$ 3,00)")
print("0 - Finalizar Pedido\n\n")
print("---------------------------------\n\n")

total = 0.0
opcao = -1
while opcao != 0:
    opcao = int(input("Escolha o número do item que deseja pedir: "))
    match opcao:

        case 1:
         print("Cookie\nPreço: R$ 5,00\n")
         total += 5.00
        case 2:
         print("Sorvete\nPreço: R$ 3,00\n\n")
         print("1 - Chocolate\n2 - Baunilha\n3 - Morango\n4 - Blue Ice\n5 - Continuar pedido\n---------------------------------\n\n")
         sorvete = 0
         while sorvete != 5:
          sorvete = int(input("Escolha o sabor do sorvete: "))
         match sorvete:
            case 1:
             print("Chocolate\nPreço: R$ 3,00\n")
             total += 3.00
            case 2:
             print("Baunilha\nPreço: R$ 3,00\n")
             total += 3.00
            case 3:
             print("Morango\nPreço: R$ 3,00\n")
             total += 3.00
            case 4:
             print("Blue Ice\nPreço: R$ 3,00\n")
             total += 3.00
            case 5:
             print("Continuando pedido...\n")
            case _:
                        print("Sabor inválido! Tente novamente.")
        case 3:
         print("Bolo\nPreço: R$ 4,00\n\n")
         print("1 - Chocolate\n2 - Cenoura\n3 - Prestígio\n4 - Aniversário\n5 - Continuar pedido\n---------------------------------\n\n")
         bolo = 0
         while bolo != 5:
          bolo = int(input("Escolha o sabor do bolo: "))
         match bolo:
            case 1:
             print("Chocolate\nPreço: R$ 4,00\n")
             total += 4.00
            case 2:
             print("Cenoura\nPreço: R$ 4,00\n")
             total += 4.00
            case 3:
             print("Prestígio\nPreço: R$ 4,00\n")
             total += 4.00
            case 4:
             print("Aniversário\nPreço: R$ 4,00\n")
             total += 4.00
            case 5:
             print("Continuando pedido...\n")
            case _:
                        print("Sabor inválido! Tente novamente.")
        case 4:
         print("Cupcake\nPreço: R$ 6,00\n")
         total += 6.00
        case 5:
         print("Chocolate Quente\nPreço: R$ 4,00\n")
         total += 4.00
        case 6:
         print("Chá\nPreço: R$ 2,00\n\n")
         print("1 - Chá de Erva-Príncipe\n2 - Chá Matte\n3 - Chá de Camomila\n4 - Chá de Hortelã\n5 - Continuar pedido\n---------------------------------\n\n")
         cha = 0
         while cha != 5:
          cha = int(input("Escolha o tipo de chá: "))
         match cha:
            case 1:
             print("Chá de Erva-Príncipe\nPreço: R$ 2,00\n")
             total += 2.00
            case 2:
             print("Chá Matte\nPreço: R$ 2,00\n")
             total += 2.00  
            case 3:
             print("Chá de Camomila\nPreço: R$ 2,00\n")
             total += 2.00
            case 4:
             print("Chá de Hortelã\nPreço: R$ 2,00\n")
             total += 2.00
            case 5:
             print("Continuando pedido...\n")
        case 7:
         print("Café\nPreço: R$ 1,00\n\n")
         print("1 - Café Simples\n2 - Café com Leite\n3 - Cappuccino\n4 - Mocha\n5 - Café Gelado\n6 - Continuar pedido\n---------------------------------\n\n")
         cafe = 0
         while cafe != 6:
            cafe = int(input("Escolha o tipo de café: "))
            match cafe:
                case 1:
                 print("Café Simples\nPreço: R$ 1,00\n")
                 total += 1.00
                case 2:
                 print("Café com Leite\nPreço: R$ 1,00\n")
                 total += 1.00  
                case 3:
                 print("Cappuccino\nPreço: R$ 1,00\n")
                 total += 1.00
                case 4:
                 print("Mocha\nPreço: R$ 1,00\n")
                 total += 1.00
                case 5:
                 print("Café Gelado\nPreço: R$ 1,00\n")
                 total += 1.00
                case 6:
                 print("Continuando pedido...\n")
        case 8:
         print("Panqueca\nPreço: R$ 5,00\n\n")
         print("ACRÉSCIMOS\n\n1 - Chocolate\n2 - Morango\n3 - Banana\n4 - Ovos Mexidos\n5 - Continuar pedido\n---------------------------------\n\n")
         panqueca = 0
         total += 5.00
         while panqueca != 5:
            panqueca = int(input("Escolha o acréscimo da panqueca: "))
            match panqueca:
                case 1:
                 print("Chocolate\nPreço: R$ 5,00\n")
                 total += 3.00
                case 2:
                 print("Morango\nPreço: R$ 5,00\n")
                 total += 0.50  
                case 3:
                 print("Banana\nPreço: R$ 5,00\n")
                 total += 0.50
                case 4:
                 print("Ovos Mexidos\nPreço: R$ 5,00\n")
                 total += 1.00
                case 5:
                 print("Continuando pedido...\n")
        case 9:
         print("Croissant\nPreço: R$ 3,00\n")
         total += 3.00
        case 0:
         print("Pedido finalizado.\n")
         print(f"Total do pedido: R$ {total:.2f}")   
        case _:
         print("Opção inválida. Por favor, escolha um número de 0 a 9.")
print("FORMA DE PAGAMENTO\n\n1 - Dinheiro\n2 - Cartão de Crédito\n3 - Cartão de Débito\n4 - Pix\n---------------------------------\n\n")
pagamento_opcao = int(input("Escolha a forma de pagamento: "))
if pagamento_opcao == 1:
  total = total
  print(f"Total do pedido: R$ {total:.2f}")
elif pagamento_opcao == 2:
  total = total + (total * 0.05)
  print(f"Total do pedido com acréscimo de 5%: R$ {total:.2f}")
elif pagamento_opcao == 3:
  total = total + (total * 0.02)
  print(f"Total do pedido com acréscimo de 2%: R$ {total:.2f}")
elif pagamento_opcao == 4:
  total = total - (total * 0.10)
  print(f"Total do pedido com desconto de 10%: R$ {total:.2f}")
else: 
    print("Opção de pagamento inválida. Por favor, escolha uma opção válida.")
print("Obrigado por comprar conosco! Volte sempre!🤎")