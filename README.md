# Tucil1_13522053

| NIM | Nama |
| :---: | :---: |
| 13522053 | Erdianti Wiga|

## About This Project
Cyberpunk 2077 Breach Protocol
Breach Protocol dalam Cyberpunk 2077 adalah sebuah minigame meretas yang mensimulasikan proses peretasan jaringan lokal dari ICE (Intrusion Countermeasures Electronics) dalam dunia permainan tersebut. Dalam minigame ini, pemain dihadapkan pada beberapa komponen kunci yaitu token, matriks, sekuens, dan buffer. Tujuan dari permainan ini adalah mencari jalan/path yang mengandung kombinasi dari beberapa sekuens yang memiliki poin terbanyak.

## Struktur Program
```bash
.
│   README.md
│
├───bin                                   
│
├───doc  
│   ├─── Laporan
│                      
├───src                             # Program
│   ├── saved                       # Folder untuk menyimpan result         
│   ├─── input.py 
│   ├─── main.py 
│   ├─── output.py 
│   ├─── solver.py                       
│  
└───test                            # Testing cases
│   ├── case.txt             
│   ├─── case1.txt.
│   ├─── case2.txt
│   ├─── case3.txt
```

## How to Run
1. Clone repository ini dengan mengetikkan `git clone https://github.com/wigaandini/Tucil1_13522053` pada terminal
2. Pindah ke direktori src dengan `cd src`
3. Run file dengan `python -u "d:\ITB\SEM 4\Stima\Tucil 1\Tucil1_13522053\src\main.py"`

## How to Use
1. Setelah Anda melakukan run file, perhatikan perintah yang muncul
2. Apabila ingin menginput dari file, maka ketik 1 (perlu diperhatikan bahwa file harus berada dalam folder test). Namun apabila ingin menginput lewat CLI, maka ketik 2
3. Bila menginput dari file, harap masukkan nama file lengkap dengan .txt
4. Apabila menginput dari CLI, ikuti perintah yang tertera pada terminal
5. Setelah melakukan seluruh rangkaian input, maka akan ditampilkan output/hasil dari program
6. Anda dapat menyimpan hasil dari program ke dalam berkas .txt