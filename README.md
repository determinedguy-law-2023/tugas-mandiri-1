# Carikata

> Proyek ini dibuat oleh **Muhammad Athallah (2006527481)** untuk memenuhi **Tugas Mandiri 1** pada mata kuliah **Layanan dan Aplikasi Web (CSCE604271)** yang diselenggarakan oleh Fakultas Ilmu Komputer, Universitas Indonesia pada Semester Genap, Tahun Ajaran 2022/2023.

## Demonstrasi Situs Web

Demonstrasi layanan dapat dilihat melalui [video ini](https://univindonesia-my.sharepoint.com/:v:/g/personal/muhammad_athallah01_office_ui_ac_id/EZCiWrmpexhPn1E2b16l8kMBE-RwLyRdkNr7ZGn2P94Yew?e=PuwqLb).

## Daftar Layanan beserta Parameter

Carikata melayani pencarian kata berdasarkan panjang, prefiks, dan sufiks. Selain itu, Carikata dapat mencari definisi kata berdasarkan Kamus Besar Bahasa Indonesia (KBBI).

Pencarian definisi kata berdasarkan KBBI dilakukan dengan memanggil API eksternal. Namun, pencarian kata berdasarkan spesifikasi dilakukan di dalam server internal berdasarkan basis data kata yang telah diperoleh dari Internet dan dihimpun pada basis data server.

Berikut adalah *URL path* layanan yang dipanggil beserta fungsinya masing-masing.

1. `cari/panjang/`: URL ini berfungsi untuk memanggil fitur pencarian kata berdasarkan panjangnya. Terdapat satu parameter wajib berupa `panjang` dan satu parameter opsional berupa `batas` panjang, apabila pencarian ingin dilakukan dalam suatu rentang (bukan suatu nilai yang definit). Saat parameter dikirim ke server, server akan mencari kata dengan linear dan menampilkan hasil pencarian berdasarkan spesifikasi parameter yang diberikan.
2. `cari/prefiks/`: URL ini berfungsi untuk memanggil fitur pencarian kata berdasarkan prefiks. Terdapat satu parameter wajib berupa `prefiks` yang ingin dicari. Saat parameter dikirim ke server, server akan mencari kata dengan linear dan menampilkan hasil pencarian berdasarkan spesifikasi parameter yang diberikan.
3. `cari/sufiks/`: URL ini berfungsi untuk memanggil fitur pencarian kata berdasarkan prefiks. Terdapat satu parameter wajib berupa `sufiks` yang ingin dicari. Saat parameter dikirim ke server, server akan mencari kata dengan linear dan menampilkan hasil pencarian berdasarkan spesifikasi parameter yang diberikan.
4. `cari/`: URL ini berfungsi untuk memanggil fitur pencarian kata secara komprehensif. Semua parameter (`panjang`, `batas` (batas panjang), `prefiks`, dan `sufiks`) tidak wajib diisi. Apabila semua parameter tidak diisi, maka hasil pencarian yang ditampilkan tidak mengandung kata apapun. Namun apabila terdapat setidaknya satu parameter yang diisi, maka hasil pencarian yang ditampilkan akan memperlihatkan kata-kata yang sesuai dengan spesifikasi parameter yang diberikan.
5. `definisi/`: URL ini berfungsi untuk memanggil fitur pencarian definisi kata berdasarkan KBBI. URL ini hanya menampilkan form input kata yang ingin dicari definisinya.
6. `definisi/<kata>`: URL ini berfungsi untuk memanggil hasil pencarian definisi kata berdasarkan KBBI. URL ini menerima parameter `kata` yang ingin dicari definisinya. Saat URL ini dipanggil, layanan akan memanggil API eksternal untuk mendapatkan definisi kata dan mengolah hasil dari API untuk disajikan dalam bentuk HTML.

## Tingkat Kesulitan Pembuatan Layanan

Terdapat dua kesulitan utama (selain memikirkan ide layanan, tentunya) saat saya membuat layanan ini.

1. Tidak adanya *dataset* bersih dari daftar kosakata bahasa Indonesia yang terkini.

    Saya menemukan beberapa *dataset* di berbagai repositori, namun sayangnya *dataset* tersebut antara terlalu tua atau terlalu komprehensif (contohnya *dataset* KBBI secara penuh yang mengandung duplikat kata namun definisi yang berbeda). Saya akhirnya memilih *dataset* yang menurut saya cukup bersih namun tidak terlalu tua pula umurnya.

2. Masih awam terkait pencarian layanan API dan pengintegrasian dengan layanan sendiri.

    Saya masih sangat awam mengenai pencarian layanan API yang cocok untuk layanan saya. Saya akhirnya menemukan layanan API Kamus Besar Bahasa Indonesia yang cocok, namun saya tidak terlalu mengerti alur pengintegrasiannya. Setelah *trial-and-error*, saya akhirnya menemukan cara *parsing data* yang sesuai dengan keinginan saya sehingga datanya dapat ditampilkan di situs web layanan saya.

## Keunikan Layanan

Sejauh yang saya lihat, belum ada layanan pencarian kata berdasarkan panjang, prefiks, dan sufiks secara komprehensif. Selain itu, layanan ini berguna untuk pembuatan lirik lagu, pantun, ataupun karya seni bahasa lainnya yang memperhatikan spesifikasi tertentu, terutama sufiks.

> Layanan ini tentunya sangat berguna untuk pemain Katla (Wordle Bahasa Indonesia), ups!

## Templat

<https://github.com/Meta502/law-django-template>

## Sumber Data

- <https://github.com/Hidayathamir/kata-kbbi-github>
- <https://github.com/btrianurdin/new-kbbi-api>

Saya awalnya berpikiran untuk menggunakan [kbbi_dataset](https://github.com/fdciabdul/kbbi_dataset), namun bentuk datanya masih sangat kasar untuk penggunaan program ini.

## Referensi

- [Url parameters, extra options & query strings](https://www.webforefront.com/django/accessurlparamstemplates.html)
- [Capturing URL parameters in request.GET](https://stackoverflow.com/a/50714430)
