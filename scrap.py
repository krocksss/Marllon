from random import randint
fichas = 100
repost=input("você quer apostar?(s/n)")

while fichas>0 and repost=='s':
    x=input("que modo de jogo você quer jogar? Pass line(pl), field(f), any craps(ac) ou Twelve(t)?")
    #modo de jogo PL
    while x=='pl' and fichas>0:
        print("você tem %d fichas"%(fichas))
        aposta=int(input("quantas fichas você quer apostar?"))
        while aposta<=0:
            print("apenas valores positivos e maiores que 0! Digite novamente")
            aposta=int(input("quantas fichas você quer apostar?"))
        d1=randint(1,6)
        d2=randint(1,6)
        s=d1+d2
        if s==7 or s==11:
            fichas=fichas+aposta
            print("você ganhou! Agora pussui %d fichas"%(fichas))
        elif s==2 or s==3 or s==12:
            fichas=fichas-aposta
            print("você perdeu! Agora possui %d fichas"%(fichas))
        else:
            #modo POINT
            print("POINT TIME")
            d3=randint(1,6)
            d4=randint(1,6)
            print("Os dados foram rolados! Que a força esteja contigo!")
            d=d3+d4
            l=0
            while l==0:
                d3=randint(1,6)
                d4=randint(1,6)
                d=d3+d4
                if d==7:
                    fichas=fichas-aposta
                    print("você tirou 7 e perdeu! agora possui %d fichas"%(fichas))
                    l+=1
                elif d==s:
                    fichas=fichas+aposta
                    print("Que sorte! a soma dos dados foi %d, a mesma do point e por isso ganhou e agora possui %d fichas"%(d3,fichas))
                    l+=1
                else:
                    print('não foi dessa vez! rolando os dados  novamente.')
                    
        
        x=input("você ainda quer jogar Pass Line?(type pl para continuar, g para acessar o menu e n para parar de jogar)")
    #modo field
    while x=='f' and fichas>0:
        print("você possui %d fichas"%(fichas))
        aposta=int(input("quantas fichas você quer apostar?"))
        while aposta<=0:
            print("apenas valores positivos e maiores que 0! Digite novamente")
            aposta=int(input("quantas fichas você quer apostar?"))
        d1=randint(1,6)
        d2=randint(1,6)
        s=d1+d2
        if s==5 or s==6 or s==7 or s==8:
            fichas=fichas-aposta
            print ("você perdeu! agora possui %d fichas"%(fichas))
        if  s==3 or s==4 or s==9 or s==10 or s==1:
            fichas=fichas+aposta
            print("você ganhou! agora possui %d fichas"%(fichas))
        if s==2:
            fichas=fichas+(2*aposta)
            print("que sorte! você tirou um 2 e ganhou o dobro pelo feito! agora você possui %d fichas"%(fichas))
        if s==12:
            fichas=fichas+(3*aposta)
            print("você está cagado, heim? conseguiu tirar 12! Meus parabéns")
            print("você possui %d fichas agora"%(fichas))
        x=input("você ainda quer jogar field?(type f para continuar, g para acessar o menu e n para parar de jogar)")

#modo de jogo twelve
    while x=="t" and fichas>0:
        print("você tem %d fichas"%(fichas))
        aposta=int(input("quantas fichas você quer apostar?"))
        while aposta<=0:
            print("apenas valores positivos e maiores que 0! Digite novamente")
            aposta=int(input("quantas fichas você quer apostar?"))
        d1=randint(1,6)
        d2=randint(1,6)
        s=d1+d2
        if s==12:
            fichas=fichas+(30*aposta)
            print("CARAI MENÓ! você ganhou. Agora você possui %d"%(fichas))
        else:
            fichas=fichas-aposta
            print("Você gosta de arriscar hein! pena q perdeu. Agora você possui %d fichas"%(fichas))
        x=input("você ainda quer jogar Twelve?(type t para continuar, g para acessar o menu e n para parar de jogar)")

#any scrap
    while x=='ac' and fichas>0:
        print("você tem %d fichas"%(fichas))
        aposta=int(input("quantas fichas você quer apostar?"))
        while aposta<=0:
            print("apenas valores positivos e maiores que 0! Digite novamente")
            aposta=int(input("quantas fichas você quer apostar?"))
        d1=randint(1,6)
        d2=randint(1,6)
        s=d1+d2
        if s==2 or s==3 or s==12:
            fichas=fichas+(aposta*7)
            print("Você ganhou! agora voce ganhou 7x oque apostou! total de fichas: %d"%(fichas))
        else:
            fichas=fichas-aposta
            print("que pena! você não ganhou dessa vez! total de fichas restantes:%d"%(fichas))
        x=input("você ainda quer jogar Any Scraps?(type ac para continuar, g para acessar o menu e n para parar de jogar)")
    if repost=='n' or fichas==0 or x=='n':
        print("Obrigado pelo tempo que pudemos passar juntos! Espero que tenhamos outras oportunidades! ")
        print("Você terminou o jogo com %d fichas"%(fichas))
        print(":)")
        quit
        repost='n'


        


        

