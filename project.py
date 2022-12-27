import requests

def menu():
    print("Menu Pilihan")
    print("============")
    print("1. Menentukan Cuaca")
    print("2. Exit")
    
def Cuaca():
    print("Menentukan Cuaca Kota")
    kota =  str(input("masukkan kota:  "))

    print();
    if kota == "Surabaya":
        url = "https://wttr.in/Surabaya"
        resp = requests.get(url)
        print(resp.text)
    elif kota == "Mojokerto":
        url = "https://wttr.in/Mojokerto"
        resp = requests.get(url)
        print(resp.text)
    elif kota == "Batu":
        url = "https://wttr.in/Batu"
        resp = requests.get(url)
        print(resp.text)
    elif kota == "Banyuwangi":
        url = "https://wttr.in/Banyuwangi"
        resp = requests.get(url)
        print(resp.text)
    elif kota == "Sidoarjo":
        url = "https://wttr.in/Sidoarjo"
        resp = requests.get(url)
        print(resp.text)
    elif kota == "Sumenep":
        url = "https://wttr.in/Sumenep"
        resp = requests.get(url)
        print(resp.text)
    elif kota == "Situbondo":
        url = "https://wttr.in/Situbondo"
        resp = requests.get(url)
        print(resp.text)
    elif kota == "Trenggalek":
        url = "https://wttr.in/Trenggalek"
        resp = requests.get(url)
        print(resp.text)
    elif kota == "Tuban":
        url = "https://wttr.in/Tuban"
        resp = requests.get(url)
        print(resp.text) 
    elif kota == "Tulungagung":
        url = "https://wttr.in/Telungagung"
        resp = requests.get(url)
        print(resp.text)
    elif kota == "Batu":
        url = "https://wttr.in/Batu"
        resp = requests.get(url)
        print(resp.text) 
    else:
        print("Kota Tidak Di Temuka di Provinsi Jawa Timur atau penamaan kota tidak sesuai dengan huruf kapital, seperti Sidoarjo")

def Exit():
    print("Trimakasih sudah menggunjungi")

#program utama
print("==============================================")
print("_____Selamat Datang_____")
print("==============================================")
print("==============================================")
print("Menentukan Cuaca Di Kota Provinsi Jawa Timur")
print("==============================================")
menu()
pilih = input("masukkan pilihan: ")
print("==============")

if pilih == ("1"):
    Cuaca()
    
elif pilih == ("2"):
    Exit()
    
else:
    print("Menu Tidak ada")
