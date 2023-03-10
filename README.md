# Tugas Mandiri 1

> Proyek ini dibuat untuk memenuhi Tugas Mandiri 1 pada mata kuliah Layanan dan Aplikasi Web (CSCE604271) yang diselenggarakan oleh Fakultas Ilmu Komputer, Universitas Indonesia pada Semester Genap, Tahun Ajaran 2022/2023.

## Templat

<https://github.com/Meta502/law-django-template>

## Cara Menjalankan

### Lokal

#### Persyaratan

- Python 3.10
- pipenv (gunakan `python -m pip install pipenv` untuk menginstal `pipenv`)

#### Instalasi

- Jalankan `pipenv install` di dalam direktori proyek
- Buatlah file `.env` yang baru, berdasarkan `.env.example`
- Jalankan `pipenv shell`
- Jalankan `python manage.py runserver`

### Docker (*Deployment* pada GCP)

#### Persyaratan

- Docker (versi terbaru)

#### Instalasi

- Jalankan `docker-compose up` di dalam direktori proyek
- Aplikasi akan men-*deploy* semua dependensi yang diperlukan secara otomatis
- Apabila terjadi kesalahan selama migrasi, jalankan kembali `docker-compose up`
