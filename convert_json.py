import json

# o arquivo que será convertido para
# format jason
filename = "data.txt"

# resultado do dicionario
dict1 = {}

# campos no arquivo
fields = ['Categoria', 'Prestador', 'Endereco', 'Bairro', 'Cidade', 'cep', 'Telefone2']

with open(filename) as fh:
    # contador de variaveis para criar um id para cada Prestador
    l = 1

    for line in fh:  # le cada linha e tira os espaços extra
        description = list(line.strip().split(",", 7))
        # para ver a saida
        print(description)

        # contador de variaveis para criar um id para cada Prestador
        pno = 'prest' + str(l)

        # loop na variavel
        i = 0
        # dicionário intermediário
        dict2 = {}
        while i < len(fields):
            # cria dicionario para cada prestador
            dict2[fields[i]] = description[i]
            i += 1
            # print(dict2)
        # appending o registro de cada Prestador
        # para o dicionario principal
        dict1[pno] = dict2
        l += 1

#     cria o arquivo json
out_file = open("prestadores.json", "w", encoding="utf-8")
json.dump(dict1, out_file, indent=4)
out_file.close()