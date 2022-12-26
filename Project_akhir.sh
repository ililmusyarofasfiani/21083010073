#!/bin/bash
echo "-----MENENTUKKAN CUACA DI KOTA PADA PROVINSI JAWA TIMUR-----"
echo -n "Masukkan Kota: ";
read kota;
echo " "
case "$kota" in
"Bangkalan")
curl https://wttr.in/Bangkalan
;;
"Banyuwangi")
curl https://wttr.in/Banyuwangi
;;
"Blitar")
curl https://wttr.in/Blitar
;;
"Bojonegoro")
curl https://wttr.in/Bojonegoro
;;
"Bondowoso")
curl https://wttr.in/Bondowoso
;;
"Gresik")
curl https://wttr.in/Gresik
;;
"Jember")
curl https://wttr.in/Jember
;;
"Jombang")
curl https://wttr.in/Jombang
;;
"Kediri")
curl https://wttr.in/Kediri
;;
"Lamongan")
curl https://wttr.in/Lamongan
;;
"Lumajang")
curl https://wttr.in/Lumajang
;;
"Madiun")
curl https://wttr.in/Madiun
;;
"Magetan")
curl https://wttr.in/Magetan
;;
"Mojokerto")
curl https://wttr.in/Mojokerto
;;
"Nganjuk")
curl https://wttr.in/Nganjuk
;;
"Ngawi")
curl https://wttr.in/Ngawi
;;
"Pacitan")
curl https://wttr.in/Pacitan
;;
"Pamekasan")
curl https://wttr.in/Pamekasan
;;
"Pasuruan")
curl https://wttr.in/Pasuruan
;;
"Ponorogo")
curl https://wttr.in/Ponorogo
;;
"Probolinggo")
curl https://wttr.in/Probolinggo
;;
"Sampang")
curl https://wttr.in/Sampang
;;
"Sidoarjo")
curl https://wttr.in/Sidoarjo
;;
"Situbondo")
curl https://wttr.in/Situbondo
;;
"Sumenep")
curl https://wttr.in/Sumenep
;;
"Trenggalek")
curl https://wttr.in/Trenggalek
;;
"Tuban")
curl https://wttr.in/Tuban
;;
"Tulungagung")
curl https://wttr.in/Tulungagung
;;
"Batu")
curl https://wttr.in/Batu
;;
"Blitar")
curl https://wttr.in/Blitar
;;
"Kediri")
curl https://wttr.in/Kediri
;;
"Madiun")
curl https://wttr.in/Madiun
;;
"Malang")
curl https://wttr.in/Malang
;;
"Pasuruan")
curl https://wttr.in/Pasuruan
;;
"Surabaya")
curl https://wttr.in/Surabaya
;;
*)
echo "Kota Tersebut Bukan Dari Wilayah Provinsi Jawa Timur. Penamaan
harus dimulai dengan huruf kapital, seperti Sidoarjo"
;;
esac
