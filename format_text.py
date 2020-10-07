mylist = ["Mecanica, 7Cavalos, Rua Ernestina Loschi 76, Itatiba Park, Itatiba, 11971512237, 11971512237",
          "Funilaria, Martelo de Ouro, Rua Cruzeiro do Sul 176, Jundiai-Mirim, Jundiai, 11975618992, 11971512237",
          "AutoVidros, AutoGlass, Rua 23 de Maio 76, Centro, Fernandopolis, 11975618992, 11971512237"
          ]

arquivo = open("data.txt", "a", encoding="utf-8")
for line in mylist:
    arquivo.writelines(line.title() + '\n')

