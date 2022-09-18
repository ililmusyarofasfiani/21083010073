#!/bin/bash
echo "Rumah makan Gurami" 

echo "siapa namamu?"

read nama
printf "Hai kak $nama!\n"
printf "Selamat datang di Rumah makan kami $Gurami\n"
printf "Masukkan menu Gurami yang ingin anda pesan?\n"
printf "pedas manis ?\n"
printf "bakar ?\n"
printf "goreng?\n"
printf "asam manis?\n"

read menu

case "$menu" in
 "pedas manis")
   echo "pesanan sudah tercatat tunggu 10 menit"
   ;;
 "bakar")
   echo "pesanan sudah tercatat tunggu 15 menit"
   ;;
 "goreng")
   echo "pesanan sudah tercatat tunggu 5 menit"
   ;;
 "asam manis")
   echo "pesanan sudah tercatat tunggu 20 menit"
   ;;
   *)
   echo "maaf menu tersebut tidak terdapat di dalam rumah makan kami"
   ;;
esac
