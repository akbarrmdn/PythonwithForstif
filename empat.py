umur = int(input("masukan umur : "))

if umur <=20 :
    nasihat = "jadilah siswa yang baik"
elif umur >= 21 and umur <= 30 :
    nasihat = "Ikuti bos yang baik"
elif umur >= 31 and umur <= 40 :
    nasihat = "bekerja untuk dirimu sendiri"
elif umur >= 41 and umur <= 60 :
    nasihat = "pekerjaan atau investasi pada generasi muda"
elif umur >= 61 :
    nasihat = "Habiskan waktu untuk dirimu sendiri"

print(nasihat)    