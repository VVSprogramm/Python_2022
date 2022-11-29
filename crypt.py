from cryptography.fernet import Fernet

atslega = Fernet.generate_key() #Atslēgas ģenerēšana
print(atslega)

a = Fernet(atslega) #Objekta izveide

teksts = b'Slepeni dati' #Teksts uz baitiem

sifDati = a.encrypt(teksts)  #Datu šifrēšana (encryption)
print(sifDati)

print(a.decrypt(sifDati)) #Datu atšifrēšana (decryption)