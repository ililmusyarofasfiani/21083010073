#!/bin/bash

# mendeklarasikan fungsi
panjang() {
	echo " Masukkan Panjang : "
	read p
}

lebar() {
	echo " Masukkan Lebar : "
	read l
}

luas() {
	echo " Program Menghitung Luas Bidang Persegi "
	panjang
	lebar
	let l=$p*$l
	echo "Luas persegi :
$l"
}

# memanggil fungsi l
luas
