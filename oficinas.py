from itertools import count

prestadores_lista = [
    'moto,sidney moto pecas e preparacoes,r. petrarca 113,jardim nossa sra. aparecida,francisco morato,07936190,1144882489',
    'moto,leste rr yamaha rua do oratorio 1452,mooca, sao paulo, 23199797, xxxxxxxxxx, xxxxxxxxx',
    'moto,life motos,avenida nordestina 6352, xxxxxx, xxxxxxx, xxxxxxx, xxxxxxxx',
    'moto,cohab motos oficina multi marcas,r. sao francisco do piaui 759,itaquera,sao paulo,08215400,11952151696',
    'moto,four motos pecas, rua yolando malozzi 597, alvinopolis, atibaia, 12942450, 11 44114888',
    'moto,dedel motos,r. eng. silvio alvin soares 351, alvinopolis, atibaia,12942520, 11 44111726',
    'funilaria,oficina premium funilaria e pintura,av. sao paulo 1109,alvinopolis,atibaia, 12942430,11 34023452',
    'funilaria,kauan autos funilaria e pintura,franco da rocha,r. cel. domingos ortiz 784, vila zanela,07851040,11963868763',
    'funilaria,nariscar funilaria e pintura ltda,av. brasilia 671, jd ipê,itatiba,1142000837, xxxxxxxxxx',
    'funilaria,ney costa auto center,r. antonio maximiliano de almeida 68,cidade luiza,jundiai,13214120,11940176917',
    'funilaria,prestador lucar funilaria e pintura,r. adriano cantone 100,retiro,jundiai,13211240,1144925492,1144925492',
    'funilaria,red reparo automotivo,r. luiz brugnolli 171,jardim do lirio,jundiai,13218617,1145335544',
    'funilaria,promocar diagnostico veicular,rua alguma coisa, sao paulo, 13209210, 1158516782,11947425351',
    'mecanica,responcar import pecas e servicos,rua cruzeiro 820, barra funda,sao paulo,01137000,1136123722,',
    'mecanica, mundicar auto,av. vila ema 2190,vila ema,sao paulo,03281001,1120225810',
    'mecanica,renacar 2 funilaria pintura e mecanica,av das colmeias 472,jd umarizal,sao paulo,05756350,1125035579,11983439938',
    'mecanica,velcar,av. das nacões 872,parque erasmo assuncao,santo andre,09260000,11941757229',
    'mecanica,fast service,rua sao gabriel,vila belvedere,americana,xxxxxxxxxx,1934683915',
    'vidro,auto vidros atibaia,r. alfredo andre 111,jardim brasil, atibaia,12940130,1144130161',
    'vidro,alo glass,av. jeronimo de camargo 4500,centro, atibaia,xxxxxxxxxx,12944218,1144117799',
    'vidro,scap pecas e acessorios para auto ltda,rua riachuelo 357,centro,braganca paulista,12900390,1140322755',
    'vidro,reauto auto vidros e acessorios,av. 14 de marco 394,vila maria,batatais,14315734, 1637615885',
    'vidro,leandri centro automotivo,av. dr. oswaldo scatena 480,caso,batatais,14300000, 1637616097',
    'vidro,alexandre chaveiro e auto vidros,av. dom luis do amaral mouzinho 1783,brodowski,14340000,16999968380, xxxxxxxxxx ',
    'vidro,scap pecas e acessorios para autos, rua riachuelo 357,centro,braganca paulista,12900390,1140322755',
    'vidro,autoglass,r. carolina florence 1802,jardim nossa sra. auxiliadora,campinas,13073076, 1921150300',
    'vidro,planeta auto vidros,r. carolina florence 784,vila nova,campinas,13073225,1932421700',
    'vidro,auto vidros santo antonio,r. dr. betim 295,vila marieta,campinas,13042020,1932335955',
    'vidro,acessorios 3vias,rua batista raffi 53,jd. nova aparecida,campinas,13068601,1937826060',
    'vidro,santa lúcia autocenter,av. dos expedicionarios brasileiros 879,coester,fernandopolis,15600000,1734425666',
    'vidro,jXautovidros,av 9 de julho 538,jardim padre bento, itu, xxxxxxxxxx,1140233379,1140230996',
    'vidro,auto vidros bruni e bruni,r. antonio meneguini 70,residencial maria fernanda,itu, xxxxxxxxxx,1140225452',
    'vidro,binho film sound,r. adelino martins 680,jardim das tulipas,jundiai,13212600,11953026661',
    'vidro,fernando vidros automotivos,r. do centenario 168,vila nova jundiai,jundiai,13210660,1145268487',
    'vidro,hollyvidros,r. italia 16,jardim bonfiglioli,jundiai,13207280,1145878125',
    'vidro,auto vidros,av. ver. belarmino pereira de carvalho 190,riacho grande,mairipora,07600000,1146046911',
    'vidro,byzord auto vitrais,parque dr. barbosa de oliveira 10,centro,taubate,12020190,1236218300',
    'vidro,autoglass,rua monte serrat 1097,vila gomes cardim,tatuape,xxxxxxxxxx,1932382300'

]
tamanho = len(prestadores_lista)

print(tamanho)