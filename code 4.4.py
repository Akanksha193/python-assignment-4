n = input("enter alphabets")
items=[n for n in input().split('-')]
items.sort()    
print('-'.join(items))