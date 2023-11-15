# bibliotecas para rodar "bem"
import os 
import time as tp
import random 


#opções e entre outros

intervalo = 1
energia = 0
fome = 0
# vida = 10
# qi = 0 
opcao = 0

 
#estrutura do código

print("                              --++++..                ########..                          ")
print("                          ##############            ##############                        ")
print("                        ##################          ##############::                      ")
print("                        ##################        @@################                      ")
print("                      ####################        ##################                      ")
print("                      ####################        ##################                      ")
print("                      ####################        ##################                      ")
print("                      mm##################        @@################                      ")
print("                      ::##################@@########################                      ")
print("                        ############################################MM                    ")
print("                      ################################################                  ")
print("                    @@################################################MM                ")
print("                  MM--      mm##########################################                ")
print("                  ##                                                    ##              ")
print("                MM      ############                  ####::            ##              ")
print("                ##    ############  mm--          ::######::mm##          mm            ")
print("                mm    ##....######    ##        ##  ########    ##        ##            ")
print("                ..    ##--@@######    ##        ##  ########    MM        ##            ")
print("                      ############    ##        ############    MM        ++            ")
print("                ++    ..########..  MM--        ############    ##        ++            ")
print("                ##        ######mm##..            ########MM####          ##            ")
print("                ##                                                        ##            ")
print("                --..                                                    ##              ")
print("                  ##                  mmMM    ##                      --@@              ")
print("                    ##++                  ::::                      MMMM                ")
print("                        ####..                                  ::##                    ")
print("                            ..@@####@@mm--..    ::MMMM@@######--                        ")
print("                                ##                        ##                            ")
print("                                ##                        ##                            ")
print("                              ##                        @@  ##                          ")
print("                              ######                    ##@@##                          ")
print("                                                        ##                              ")
print("                                  ..                    @@                              ")
print("                                  ::  ..##########MM    ++                              ")
print("                                  ::  ##            --MM                                ")
print("                                    ##              ##@@                                ")
print("\n")

print(" ___________  ")
print("|           | ")
print("| Tamagotchi | ")
print("| em Python | ")
print("|___________| ")
print("(\__/)||      ")
print("(•ㅅ•) ||      ")
print("/    づ        ")
print("\n")

tp.sleep(5)





nome = input("Qual vai ser o nome do seu Tamagotchi?")
print("Parece que alguém está nascendo...")
tp.sleep(10)
os.system("cls")
print("Nasceu!!")
tp.sleep(3)
print("/\_/\\")
print("(•.•)")
print("(___)~")
print("Bem vindo ao mundo", nome, '!')
tp.sleep(2)
#carregamento 
print("Aguarde um momento...")
print("Loading… 1% █▒▒▒▒▒▒▒▒▒") 
tp.sleep(2)
print("Loading… 10% ███▒▒▒▒▒▒▒")
tp.sleep(4)
print("Loading… 30% █████▒▒▒▒▒")
tp.sleep(2)
print("Loading… 50% ███████▒▒▒")
tp.sleep(1)
print("Loading… 100% ██████████")
tp.sleep(3)
os.system("cls")
#corpo principal
while opcao != 3:
    # print("Nome:",nome)
    print("Nome:",nome)
    print("Energia:",energia,"/100")
    print("Fome:",fome,"/100")
    print("\n")
    print("/\_/\\")
    print("(•.•)")
    print("(___)~")
    print("\n")
    print("""[1]Comer  [2]Ir ao banheiro [3] Sair""")
    opcao = int(input("O que você quer fazer?"))
    os.system("cls")
    #opções onde ocorrem a partir do número de escolha
    if(opcao == 1):

            print("/\__/\\")
            print("(•🍞•)")
            print("(/___\)~")
            print(nome,"está comendo algo")
            tp.sleep(10)
            energia += random.randint(1,4)
            fome += random.randint(4,9)
            print(nome, "ganhou",energia,"de energia e",fome,"de fome")
            os.system('cls')
    elif(opcao == 2):
            print("    　ノヽ")
            print("　 （＿　 ）")
            print("　（＿　　　 ）")
            print("（＿＿＿＿＿＿ ）")
            print("　ヽ(´･ω･)ﾉ")
            print("　 |　 /")
            print("　　U U")
            print(nome,'está fazendo coisas no banheiro...')
            tp.sleep(20)
            energia += random.randint(1,4)
            fome -= random.randint(1,3)
            print(nome, "ganhou",energia,"de energia e perdeu",fome,"de fome")
            tp.sleep(3)
            os.system('cls')
    elif(opcao == 3):
        sair = input("tem certeza? (responda com s ou n)")
        if(sair == "s"):
            break
        elif(sair == 'n'):
            continue 
            tp.sleep(2)

