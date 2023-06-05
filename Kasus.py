daya = int(input("Masukan daya : "))
BebanBulanIni = int(input("Masukan BebanBulanIni : "))
BebanBulanLalu = int(input("Masukan BebanBulanLalu : "))
harga = 500
pakai = BebanBulanIni - BebanBulanLalu

if daya == 450:
    biayaBeban = 10000
elif daya == 900:
    biayaBeban = 15000
elif daya == 1200:
    biayaBeban = 20000

pembayaran = pakai * harga + biayaBeban 
print(pembayaran)