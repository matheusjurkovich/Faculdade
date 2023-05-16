def download(fileSize, speed):
    downloadTime = fileSize / (speed / 8)
    secondToMinute = downloadTime / 60
    return secondToMinute

fileSize = int(input("Digite o tamanho do arquivo em MB: "))
speed = int(input("Digite a velocidade de download em Mbps: "))
print ("O tempo de download é de %.2f minutos" % download(fileSize, speed))