Animetake Lite Version
======================

Atklite atau Animetake Lite Version adalah versi ringan dari website
[animetake.com][atk] yang bisa kalian buka di
[atklite.herokuapp.com][atklite].

Kenapa?
=======

Alasan saya bikin ini karena website [animetake.com][atk] meskipun tidak
terlalu berat, tapi lumayan lama dibuka di laptop saya. Penyebabnya mungkin
karena banyak yang gambar, media, dan bagian-bagian halaman lain yang harus
dimuat. Tentu saja ini jadi masalah tersendiri ketika halaman tersebut
diakses melalui handphone. Apalagi handphone saya bukan smartphone. Halaman
tadi jadi lebih lama dimuat dan tampilannya juga agak berantakan.

Kedua, karena pada hari senin yang lalu (4/11/13) ada artikel yang
membahas tentang XPath. Akhirnya muncullah ide ini. Memanfaatkan XPath
(dengan library lxml) untuk memproses pengambilan data-data yang
penting dari halaman di [animetake.com][atk] dan menampilkan bagian-
bagian yang penting saja dengan bantuan web framework Flask. Sehingga
didapat website yang bersih dan tentunya lebih ringan untuk dimuat.
Serta lebih mobile-friendly.

Pustaka
=======

Bahasa pemrograman yang dipakai adalah bahasa **Python**. dengan
memanfaatkan beberapa modul/packages berikut:
- [**Flask**](http://flask.pocoo.org/): framework untuk membuat
  aplikasi web.
- [**lxml**](http://lxml.de/): modul untuk mengolah file XML (dan tentunya
  HTML). Untuk proses
  scrapping halaman.
- [**requests**](http://www.python-requests.org/en/latest/): HTTP for
  humans.

Instalasi di Heroku
===================

Pastikan kalian sudah memasang `heroku` di sistem kalian dan punya akun
di http://heroku.com/, buat baru jika belum punya. Setelah itu login lewat
terminal dengan menjalankan perintah berikut:

```console
$ heroku login
Enter your Heroku credentials.
Email: komachan@example.com
Password:
Could not find an existing public key.
Would you like to generate one? [Yn]
Generating new SSH public key.
Uploading ssh public key /Users/kenneth/.ssh/id_rsa.pub
```

Ganti komachan@example.com dengan email login anda di heroku.

Jika ada masalah dengan pengunggahan publik key kalian, coba eksekusi
perintah `heroku keys:add`. Artikel lengkap ada di 
[Heroku Quickstart](https://devcenter.heroku.com/articles/quickstart)

Setelah itu clone repo ini dengan menjalankan perintah `git` berikut.

```console
$ git clone https://github.com/matematikaadit/atklit.git
```

Langkah berikutnya buat `virtualenv` baru, dan install semua packages yang
diperlukan. Perintahnya sebagai berikut:

```console
$ cd atklite
$ virtualenv venv
$ . ./venv/bin/activate
$ pip install -r requirements.txt
```

Sekarang kalian bisa menjalankan perintah berikut untuk mengaktifkan server
untuk development:
```console
$ python atklite.py
```
Halaman Flask app kalian akan aktif di http://127.0.0.1:5000/

Untuk mengunggah repo ini ke heroku, buat repo baru di heroku lalu push
kode kita ke repo tersebut.
```console
$ heroku create
$ git push heroku master
```

Selamat, sekarang atklite baru anda sudah aktif dan langsung bisa dibuka.
Gunakan perintah `heroku open` untuk membukanya di browser default anda.

LICENSE
=======

The MIT License (MIT)

Detail lihat file [LICENSE](/LICENSE).

[atk]: http://www.animetake.com
[atklite]: http://atklite.herokuapp.com
[heroku]: http://www.heroku.com