Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
print('Transform all names to uppercase using [normal list - list comprehension - functional programming]')
print('NORMAL LIST')
normal_list = []
for name in Names :
    normal_list.append(name)
    
print(normal_list)

print('--------------------------------------')
print('LIST COMPREHENSION')

comp_list =[name.upper() for name in Names]
print(list(comp_list))
print('--------------------------------------')
print('FUNCTIONAL PROGRAMMING')
def ToUpper(name):
    return name.upper()

func_list= map(ToUpper,Names)
print(list(func_list))

print('*********************************************************************************************************************')        
print('Get the names that contains ‘a’ in a list using [normal list - list comprehension - functional programming]')
print('NORMAL LIST')
print('--------------------------------------')
normal_list=[]
for name in Names:
    if 'a' in name:
        normal_list.append(name)
print(normal_list)

print('--------------------------------------')
print('LIST COMPREHENSION')
#newlist = [expression for item in iterable if condition == True]
comp_list =[name for name in Names if 'a' in name]

print(list(comp_list))
print('--------------------------------------')
print('FUNCTIONAL PROGRAMMING')
def isContain(name):
    if 'a' in name :
        return name
    else:
        return 'NOT Contain'
func_list =map(isContain,Names)
print(list(func_list))


print('*********************************************************************************************************************') 
print('Get the names that starts with ‘t’ in a list using [normal list - list comprehension - functional programming]')
normal_list=[]
for name in Names:
    if name.startswith('t'):
        normal_list=[name]
print(normal_list)

print('--------------------------------------')
print('LIST COMPREHENSION')
comp_list=[name for name in Names if name.startswith('t')]
print(list(comp_list))

print('--------------------------------------')
print('FUNCTIONAL PROGRAMMING')
def Startswith(name):
    if name.startswith('t'):
        return name
func_list=map(Startswith,Names)
print(list(func_list))

print('*********************************************************************************************************************') 
print('Get the names that contains 2 or more ‘a’ letter using [normal list - list comprehension - functional programming]')
normal_list=[]
word=[]
for name in Names:
    if name.count('a')>=2:
        normal_list.append(name)
print(normal_list)

print('--------------------------------------')
print('LIST COMPREHENSION')
comp_list=[name for name in Names if name.count('a')>=2]
print(comp_list)

print('--------------------------------------')
print('FUNCTIONAL PROGRAMMING')
def doubleChar(name):
    if name.count('a')>=2:
        return name
func_list=map(doubleChar,Names)
print(list(func_list))

print('--------------------------------------')
print('Unpack the list in :')
print('- a,b , a= the first index , b = rest of the list')
a,*b = Names
print(a)
print(b)

print('--------------------------------------')
print('- a = the first index , b = the last index')
a,*_,b= Names
print(a)
print(b)

print('--------------------------------------')
print('- a= the first index , b = the second index')
a,b,*_=Names
print(a)
print(b)




