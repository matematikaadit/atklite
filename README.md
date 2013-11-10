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

Kedua, karena pada hari itu ada artikel yang membahas tentang XPath.
Akhirnya muncullah ide ini. Memanfaatkan XPath (dengan library lxml) untuk
memproses pengambilan data-data yang penting dari halaman di
[animetake.com][atk] dan menampilkan bagian-bagian yang penting saja dengan bantuan web framework Flask. Sehingga didapat website yang bersih dan
tentunya lebih ringan untuk dimuat. Serta lebih mobile-friendly.

Pustaka
=======

Bahasa pemrograman yang dipakai adalah bahasa **Python**. dengan
memanfaatkan beberapa modul berikut:
- **Flask**: framework untuk membuat aplikasi web.
- **lxml**: modul untuk mengolah file XML (dan tentunya HTML). Untuk proses
  scrapping halaman.

LICENSE
=======

The MIT License (MIT)

Detail silakan lihat di file [LICENSE](/LICENSE).

[atk]: http://www.animetake.com
[atklite]: http://atklite.herokuapp.com
[heroku]: http://www.heroku.com