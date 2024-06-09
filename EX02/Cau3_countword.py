def count_word (file_path):
# create an emty dic
    counter={}
# open file
    with open(file_path,'r') as file:
# iterates over each line and split ""
        for word in file:
            words=word.split()
# iterates over word and count in dic counter
            for word in words:
                if word in counter:
                    counter[word]+=1
                else:
                    counter[word]=1
    return counter
file_path='C:\\Users\Admin\\OneDrive - VNU-HCMUS\\Desktop\\P1_data.txt'
result=count_word(file_path)
print(result['man'])