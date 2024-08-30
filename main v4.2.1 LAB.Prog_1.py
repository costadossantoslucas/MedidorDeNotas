import math

RED   = "\033[1;31m"  
BLUE  = "\033[1;49;96m"
YELLOW = "\033[1;49;33m"
CYAN = "\033[5;49;90m"
WHITES = "\033[4;49;37m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
MAGENTA = "\033[1;35;335m"
BOLD  = "\033[;1m"

print("⁣⁣⁣")
print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)

print("⁣⁣⁣")
print("Olá Aluno!")
print("Seja Bem-vindo ao " + BOLD + BLUE + "Medidor de Notas" + RESET + "!" + RESET)
print("Aqui você pode calcular suas notas adquiridas no semestre entre " + BOLD + YELLOW + "C1" + RESET + "," + BOLD + YELLOW + " C2" + RESET + " e " + BOLD + YELLOW + "C3" + RESET + " resultando em sua Média Parcial e Média Final." + BOLD + RED + " OBS.: Avaliações 1 valem 8 pontos, e avaliações 2 valem 2 pontos."+ RESET)
print("⁣⁣⁣")

print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
print("⁣⁣⁣")

start = int(input("Digite " + YELLOW + "[1]" + RESET + " para iniciar o procedimento ou " + YELLOW + "[0]" + RESET + " para cancelar: "))
print("⁣⁣⁣")

if start == 1:

  print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
  print("⁣⁣⁣")

  C1_A1 = float(input("Para começar, por favor, insira sua nota em C1.A1: "))
  print("⁣⁣⁣")

  while C1_A1 > 8:
    print("⁣⁣⁣")
    print(BOLD + RED + "[!]" + RESET + " Digite novamente, a Avaliação 1 (PROVA) vale 8 pontos " + BOLD + RED + "[!]" + RESET)
    print("⁣⁣⁣")

    print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)

    print("⁣⁣⁣")  
    C1_A1 = float(input("Digite a nota alcançada em C1.A1 novamente: "))
    print("⁣⁣⁣")
  
  C1_A2 = float(input("Por favor, agora insira sua nota em C1.A2: "))
  print("⁣⁣⁣")

  while C1_A2 > 2:
    print("⁣⁣⁣")
    print(BOLD + RED + "[!]" + RESET + " Digite novamente, a Avaliação 2 (QUESTIONÁRIO NO AVA) vale 2 pontos " + BOLD + RED + "[!]" + RESET)
    print("⁣⁣⁣")

    print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
    print("⁣⁣⁣")
    
    C1_A2 = float(input("Digite a Nota alcançada em C1.A2 novamente: "))
    print("⁣⁣⁣")
  
  print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
  print("⁣⁣⁣")

  C1_T = float((C1_A1 + C1_A2))
  if C1_T >= 7:
    print(BOLD + GREEN + "UAU! Parabéns! " + RESET + "Você não ficou de " + YELLOW + "recuperação" + RESET + " na C1!")
    print("⁣⁣⁣") 

  else:
    print("⁣⁣⁣")
    print(BOLD + RED + "Poxa! Que pena! " + RESET + "Você ficou de " + YELLOW + "recuperação" + RESET + " na C1!")
    print("⁣⁣⁣")
  
  print(WHITES + "Logo, o total da nota adquirida em C1 é:" + RESET + f" {C1_T:.2f}")
  print("⁣⁣⁣")

  print("⁣⁣⁣")
  print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
  print("⁣⁣⁣")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-= C2 -=-=-=-=-=-=-=-=-=-=-=-=-

  C2_A1 = float(input("Por favor, insira a sua nota em C2.A1: "))
  print("⁣⁣⁣")
  
  while C2_A1 > 8:

    print("⁣⁣⁣")
    print(BOLD + RED + "[!]" + RESET + " Digite novamente, a Avaliação 1 (PROVA) vale 8 pontos " + BOLD + RED + "[!]" + RESET)
    print("⁣⁣⁣")

    print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
    print("⁣⁣⁣")

    C2_A1 = float(input("Digite a nota alcançada em C2.A1 novamente: "))
    print("⁣⁣⁣")
  
  C2_A2 = float(input("Por favor, agora insira sua nota em C2.A2: "))
  print("⁣⁣⁣")
  
  while C2_A2 > 2:
    print("⁣⁣⁣")
    print(BOLD + RED + "[!]" + RESET + " Digite novamente, a Avaliação 2 (QUESTIONÁRIO NO AVA) vale 2 pontos " + BOLD + RED + "[!]" + RESET)
    print("⁣⁣⁣")
    print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
    print("⁣⁣⁣")


    C2_A2 = float(input("Digite a nota alcançada em C2.A2: "))
    print("⁣⁣⁣")
    
  C2_T = float((C2_A1 + C2_A2))
  print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
  print("⁣⁣⁣")

  if C2_T >= 7:
    print(BOLD + GREEN + "UAU! Parabéns! " + RESET + "Você não ficou de " + YELLOW + "recuperação" + RESET + " na C2! ")
    print("⁣⁣⁣")

  else:
    print("⁣⁣⁣")
    print(BOLD + RED + "Poxa! Que pena! " + RESET + "Você ficou de " + YELLOW + "recuperação" + RESET + " na C2!")
    print("⁣⁣⁣")

  print(WHITES + "Logo, o total de nota adquirida em C2 é:" + RESET + f" {C2_T:.2f}")
  print("⁣⁣⁣")

  print("⁣⁣⁣")
  print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
  print("⁣⁣⁣")

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

  C3_A1 = float(input("Por favor, insira sua nota em C3.A1: "))
  print("⁣⁣⁣")
  
  while C3_A1 > 8:
    print("⁣⁣⁣")
    print(BOLD + RED + "[!]" + RESET + " Digite novamente, a Avaliação 1 (PROVA) vale 8 pontos " + BOLD + RED + "[!]" + RESET)
    print("⁣⁣⁣")

    print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
    print("⁣⁣⁣")

    C3_A1 = float(input("Digite a nota alcançada em C3.A1 novamente: "))
    print("⁣⁣⁣")

    
  C3_A2 = float(input("Por favor, por último, insira sua nota em C3.A2: "))
  print("⁣⁣⁣")

  while C3_A2 > 2:
    print("⁣⁣⁣")
    print(BOLD + RED + "[!]" + RESET + " Digite novamente, a Avaliação 2 (QUESTIONÁRIO NO AVA) vale 2 pontos " + BOLD + RED + "[!]" + RESET)
    print("⁣⁣⁣")

    print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
    print("⁣⁣⁣")

    C3_A2 = float(input("Digite a nota alcançada em C3.A2 uma última vez: "))
    print("⁣⁣⁣")

  print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
  print("⁣⁣⁣")
    
  C3_T = float((C3_A1 + C3_A2))
  if C3_T >= 7:
    print(BOLD + GREEN + "UAU! Parabéns! " + RESET + "Você não ficou de " + YELLOW + "recuperação" + RESET + " na C3! ")
    print("⁣⁣⁣")
    print("⁣⁣⁣")
  
  else:
    print("⁣⁣⁣")
    print(BOLD + RED + "Poxa! Que pena! " + RESET + "Você ficou de " + YELLOW + "recuperação" + RESET + " na C3!")
    print("⁣⁣⁣")

  print(WHITES + "Logo, o total de nota adquirida em C3 é:" + RESET + f" {C3_T:.2f}")
  print("⁣⁣⁣")

  print("⁣⁣⁣")
  print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
  print("⁣⁣⁣")

#=-=-=-=-=-=-=-=-=-=-=-=-=-= MP =-=-=-=-=-=-=-=-=-=-=-=-=-

  MP = (C1_T + C2_T + C3_T)/3

  print("⁣⁣⁣")
  print(WHITES + "Em conclusão... Sua Média Parcial (Nota Final) é:" + RESET + f" {MP:,.2f}")
  print("⁣⁣⁣")

  print("⁣⁣⁣")
  print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
  print("⁣⁣⁣")

  if  MP >= 6.95:
    print("⁣⁣⁣")
    print(BOLD + GREEN + "PARABÉNS!" + RESET + " Você alcançou uma nota mínima! Continue assim!")
    print("⁣⁣⁣")

    print("⁣⁣⁣")
    print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
    print("⁣⁣⁣")

    print("É mais fácil ser o primeiro, ")
    print("do que continuar a ser o primeiro.")
    print(" ─ " + WHITES + "Bill Gates" + RESET)
    print("⁣⁣⁣")

    print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
    print("⁣⁣⁣")

    print("⁣⁣⁣")
    print("Situação Final: " + BOLD + GREEN + "APROVADO" + RESET)
    print("⁣⁣⁣")

    print("⁣⁣⁣")
    print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
    print("⁣⁣⁣")
    
    print("Agradecemos por usar o " + BOLD + BLUE + "Medidor de Notas" + RESET + "!" + RESET) 
    print("Volte sempre que necessário!")
    print("⁣⁣⁣")

    print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
    print("⁣⁣⁣")
  
  else:
    print("⁣⁣⁣")
    print(BOLD + RED +"Infelizmente " + RESET + "você não alcançou a nota mínima!")
    print("⁣⁣⁣")

    print("⁣⁣⁣")
    print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
    print("⁣⁣⁣")

    print("⁣⁣⁣")
    print("Situação Final: "+ BOLD + RED + "REPROVADO" + RESET)
    print("⁣⁣⁣")

    print("⁣⁣⁣")
    print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
    print("⁣⁣⁣")
          
    print("⁣⁣⁣")  
    print("É genial festejar o sucesso, ")
    print("mas é mais importante aprender com as lições do fracasso. ")
    print(" ─ " + WHITES + "Bill Gates" + RESET)
    print("⁣⁣⁣")

    print("⁣⁣⁣")
    print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
    print("⁣⁣⁣")
    
    print("Agradecemos por usar o " + BOLD + BLUE + "Medidor de Notas" + RESET + "!" + RESET)
    print("Volte sempre que necessário!")
    print("⁣⁣⁣")

    print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
    print("⁣⁣⁣")

  print("⁣⁣⁣")
  print(BOLD + MAGENTA + "Trabalho desenvolvido por: " + RESET + "Catharina B., Lucas C., Rulity A.")
  print("⁣⁣⁣")

  print("⁣⁣⁣")
  print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
  print("⁣⁣⁣")

else:
  print("⁣⁣⁣")
  print("Operação" + BOLD + RED + " CANCELADA " + RESET + "pelo usuário.")
  print("⁣⁣⁣")
  print("Agradecemos por usar o " + BOLD + BLUE + "Medidor de Notas" + RESET + "!" + RESET)
  print("Volte sempre que necessário!")
  print("⁣⁣⁣")

  print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
  print("⁣⁣⁣")

  print("⁣⁣⁣")
  print(BOLD + MAGENTA + "Trabalho desenvolvido por: " + RESET + "Catharina B., Lucas C., Rulity A.")
  print("⁣⁣⁣")

  print("⁣⁣⁣")
  print(BOLD + CYAN + "ー・ー・ー・ー・ー・ー・ー・ー・ー・ー" + RESET)
  print("⁣⁣⁣")