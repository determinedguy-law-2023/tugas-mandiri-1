# Carikata

> Proyek ini dibuat oleh Muhammad Athallah (2006527481) untuk memenuhi Tugas Mandiri 1 pada mata kuliah Layanan dan Aplikasi Web (CSCE604271) yang diselenggarakan oleh Fakultas Ilmu Komputer, Universitas Indonesia pada Semester Genap, Tahun Ajaran 2022/2023.

## Daftar Layanan beserta Parameter

Carikata melayani pencarian kata berdasarkan panjang, prefiks, dan sufiks. Selain itu, Carikata dapat mencari definisi kata berdasarkan Kamus Besar Bahasa Indonesia (KBBI).

Pencarian definisi kata berdasarkan KBBI dilakukan dengan memanggil API eksternal. Namun, pencarian kata berdasarkan spesifikasi dilakukan di dalam server internal berdasarkan basis data kata yang telah diperoleh dari Internet dan dihimpun pada basis data server.

## Tingkat Kesulitan Pembuatan Layanan

Terdapat dua kesulitan utama (selain memikirkan ide layanan, tentunya) saat saya membuat layanan ini.

1. Tidak adanya *dataset* bersih dari daftar kosakata bahasa Indonesia yang terkini.

    Saya menemukan beberapa *dataset* di berbagai repositori, namun sayangnya *dataset* tersebut antara terlalu tua atau terlalu komprehensif (contohnya *dataset* KBBI secara penuh yang mengandung duplikat kata namun definisi yang berbeda). Saya akhirnya memilih *dataset* yang menurut saya cukup bersih namun tidak terlalu tua pula umurnya.

2. Masih awam terkait pencarian layanan API dan pengintegrasian dengan layanan sendiri.

    Saya masih sangat awam mengenai pencarian layanan API yang cocok untuk layanan saya. Saya akhirnya menemukan layanan API Kamus Besar Bahasa Indonesia yang cocok, namun saya tidak terlalu mengerti alur pengintegrasiannya. Setelah *trial-and-error*, saya akhirnya menemukan cara *parsing data* yang sesuai dengan keinginan saya sehingga datanya dapat ditampilkan di situs web layanan saya.

## Keunikan Layanan

Sejauh yang saya lihat, belum ada layanan pencarian kata berdasarkan panjang, prefiks, dan sufiks secara komprehensif.

## Templat

<https://github.com/Meta502/law-django-template>

## Sumber Data

- <https://github.com/Hidayathamir/kata-kbbi-github>
- <https://github.com/btrianurdin/new-kbbi-api>

Saya awalnya berpikiran untuk menggunakan [kbbi_dataset](https://github.com/fdciabdul/kbbi_dataset), namun bentuk datanya masih sangat kasar untuk penggunaan program ini.

## Referensi

- [Url parameters, extra options & query strings](https://www.webforefront.com/django/accessurlparamstemplates.html)
- [Capturing URL parameters in request.GET](https://stackoverflow.com/a/50714430)
