#Data di python = list,array,dictionary,tuple
# list/array = [ ]
# dictionary = { }
# tuple = ( ), untuk data nilai permanen

#Formula Dictionary 
# variabel dictionary = { 
#   'variabel data' : 'data real'
# }
data_dictionary = {
    #nickname : fullname
    'filbert' : 'filbert owen limantara',
    'aiko' : 'mikaela aiko',
    'class' : 'Class 10 D',
}
print(data_dictionary['aiko'])
print(data_dictionary['filbert'])
print(data_dictionary['class'])
#jumlah data
length_dictionary = len(data_dictionary)
print(f"Jumlah Data: {length_dictionary}")

#Formula edit data 1
# variabel dictionary ['nickname'] = 'data baru'
# print(variabel dictionary)

data_dictionary ['aiko'] = 'Mikaela Aiko Hananta'
print (data_dictionary)
#Formula edit data 2
# variabel dictionary.update({'nickname':'data baru'})
# print(variabel dictionary)
data_dictionary.update ({'filbert': 'Filbert Owen Limantara 10 D'})
print(data_dictionary)
#Formula Delete Data
# del variabel dictionary ['nickname']
# print (variabel dictionary)
del data_dictionary ['class']
print (data_dictionary)

