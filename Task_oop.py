

class Game():

    def __init__(self):
        while True:
            print('''Welcome , Enter Game Number To access the Game
1- List of numbers to know which is odd numbers & even numbers
2- write sentence to now which word is repeated and length of your setnence
3- Choose number to show you < numbers before it
4- insert two numbers to divide  from zero to first number/ secoend number
5- Coming Soon
************************* if you want Exit Game type 'x' *************************
''')
        
            game_choice =(input('Choose Game number : '))
            if(game_choice == '1'):
                self.odd_even()
            elif(game_choice == '2'):
                self.checkSentence()
            elif(game_choice == '3'):
                self.numbers_added()
            elif(game_choice == '4'):
                self.isDivision()
            elif(game_choice == '5'):
                print('This Game Coming Soon')
            elif(game_choice == 'x' or 'X'):
                print('Good Bye')
                break
            else:
                print('Please be sure your input 1-2-3-4-5-x')
            print('----------------------------------------------------------------------------- \n \n \n \n\n ')
          
                

        
    def odd_even(self):
        print('Choose numbers be sure there is space between them : ')
        user_input= list(map(int,input().split(' ')))
        odd=[]
        even=[]
        print(user_input)
        for num in user_input:
            if(num % 2)== 0:
                odd.append(num)
            else:
                even.append(num)
        result = print(f'odd number is {odd}, Even number is {even}')
        return result
        

    def checkSentence(self):
        print("write your sentence : ")
        txt = input()
        sentence = txt.split()
        x=[]
        txt_deleted=[]
        sentence_len= len(txt)
        for txt in sentence:
            if(txt not in x):
                x.append(txt)
                result = ' '.join(x)
            else:
                txt_deleted.append(txt)
        answer= print(f'''this is the orginal sentence : {sentence}
    this is after remove same words : {result}
    this is same word : {txt_deleted}
    this is number of characters : {sentence_len}''')
        return answer
        

    def numbers_added(self):
        number = int(input("Choose your number : "))
        i = 0
        while i <= number :
            print(i)
            i+=1

    def isDivision(self):
        number1 = int(input("first number : "))
        number2 = int(input("seconed number :"))
        i=1
        for num in range(0+1,number1+1):
            print(f'{number2} / {num} = ', number2/num)
               

    def isDivisible(self):
        number1= int(input("insert first number : "))
        #number2= int(input("insert seconed number : "))
        for x in range(1,101):
            print(f'{number1} % {x} =' ,number1 % x)
            '''
        if(number1 % number2 == 0):
            print(f'{number1} % {number2} = ' ,number1 % number2)
        else:
            print("False")
            print(f'{number1} % {number2} = ' ,number1 % number2)
    '''

g1=Game()

