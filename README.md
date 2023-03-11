# Carikata

> Proyek ini dibuat untuk memenuhi Tugas Mandiri 1 pada mata kuliah Layanan dan Aplikasi Web (CSCE604271) yang diselenggarakan oleh Fakultas Ilmu Komputer, Universitas Indonesia pada Semester Genap, Tahun Ajaran 2022/2023.

## Templat

<https://github.com/Meta502/law-django-template>

## Sumber Data

- <https://github.com/Hidayathamir/kata-kbbi-github>
- <https://github.com/btrianurdin/new-kbbi-api>

Saya awalnya berpikiran untuk menggunakan [kbbi_dataset](https://github.com/fdciabdul/kbbi_dataset), namun bentuk datanya masih sangat kasar untuk penggunaan program ini.

## Daftar Layanan beserta Parameter

Carikata melayani pencarian kata berdasarkan panjang, prefiks, dan sufiks. Selain itu, Carikata dapat mencari definisi kata berdasarkan Kamus Besar Bahasa Indonesia (KBBI).

Pencarian definisi kata berdasarkan KBBI dilakukan dengan memanggil API eksternal. Namun, pencarian kata berdasarkan spesifikasi dilakukan di dalam server internal berdasarkan basis data kata yang telah diperoleh dari Internet dan dihimpun pada basis data server.

## Tingkat Kesulitan Pembuatan Layanan

## Keunikan Layanan

## Referensi

- [Url parameters, extra options & query strings](https://www.webforefront.com/django/accessurlparamstemplates.html)
- [Capturing URL parameters in request.GET](https://stackoverflow.com/a/50714430)
