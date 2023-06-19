<a name="readme-top"></a>
## MLlib
## Screenshot Hasil & Penjelasan
<table>
  <tr align="center">
    <td>
    ml_recommender_scala
    <td> 
      <img src="https://github.com/raihanhd12/BIG-DATA/assets/95725937/23d64ba8-704f-4dee-a7ac-64c97475d76b"><br><br>
      Kode di atas menggunakan Apache Spark untuk membangun model rekomendasi dengan menggunakan algoritma Alternating Least Squares (ALS) dari modul `pyspark.ml.recommendation`. Data rating film dalam format "userId::movieId::rating::timestamp" dibaca dan diparsing menggunakan fungsi `parseRating`. Data tersebut kemudian diubah menjadi DataFrame. Selanjutnya, data dibagi menjadi set pelatihan dan pengujian. Model rekomendasi ALS dengan konfigurasi tertentu dibangun menggunakan objek ALS. Model tersebut disimpan dan digunakan untuk menghasilkan prediksi pada set pengujian. Menggunakan prediksi tersebut, dilakukan perhitungan root mean square error (RMSE) untuk mengevaluasi performa model. Hasil prediksi juga disimpan dalam format CSV.
    </td>
    </td>
    </tr>
    <tr align="center">
    <td>    
    movie_recommendations_py
    <td>
      <img src="https://github.com/raihanhd12/BIG-DATA/assets/95725937/50c42a44-5224-4ba0-a88d-500bbb1c80f9"><br><br>
      Kode di atas menggunakan Apache Spark untuk membangun model rekomendasi menggunakan algoritma Alternating Least Squares (ALS) dari modul `pyspark.ml.recommendation`. Data rating film dalam format "userId::movieId::rating::timestamp" dibaca dan diproses menjadi DataFrame. Data tersebut kemudian dibagi menjadi set pelatihan dan pengujian. Model ALS dengan konfigurasi tertentu dibangun menggunakan objek ALS. Model tersebut dievaluasi dengan menghitung Root Mean Square Error (RMSE) dan Mean Square Error (MSE) pada set pengujian. Prediksi dari model juga ditampilkan.
  </td>
    </td>
    </tr>
    <tr align="center">
    <td>
     Slide 48
    <td>
      <img src="https://github.com/raihanhd12/BIG-DATA/assets/95725937/356bea9a-7e35-418c-9113-423bfe2728a7"><br><br>
      Kode tersebut mengimplementasikan algoritma ALS (Alternating Least Squares) Collaborative Filtering untuk memberikan rekomendasi produk kepada pengguna. Ia membaca data rating dari file, memproses data tersebut, melatih model ALS menggunakan data rating yang diproses, dan menghasilkan daftar rekomendasi produk untuk pengguna tertentu. Hasil rekomendasi tersebut ditampilkan dalam bentuk tabel yang berisi informasi tentang ID film, judul, dan rating.
  </td>
    </td>
    </tr>
      <tr align="center">
    <td>
     Slide 49
    <td>
      <img src="https://github.com/raihanhd12/BIG-DATA/assets/95725937/c91d38c1-c0c6-4a7b-bea2-20db2e2f109c"><br><br>
      Kode di atas menggunakan Apache Spark untuk menghitung statistik ringkasan kolom dari sebuah RDD berisi vektor-vektor numerik. Kode ini pertama-tama membuat sebuah SparkSession dan SparkContext. Kemudian, RDD dibuat dengan menggunakan metode parallelize() untuk memuat vektor-vektor numerik. Setelah itu, fungsi colStats() dari modul Statistics digunakan untuk menghitung statistik ringkasan kolom dari RDD tersebut, seperti rata-rata, varians, dan jumlah non-nol. Hasil statistik tersebut kemudian dicetak ke layar.
  </td>
    </td>
    </tr>
      <tr align="center">
    <td>
     Slide 52
    <td>
      <img src="https://github.com/raihanhd12/BIG-DATA/assets/95725937/a040bf23-0ec9-4f24-a061-8065e0c4160d"><br><br>
      Kode di atas menggunakan Apache Spark untuk melakukan pengelompokan data menggunakan algoritma K-Means. Kode ini pertama-tama membuat sebuah SparkSession untuk menginisialisasi sesi Spark. Kemudian, data dibaca dari file menggunakan `spark.read.text()` dan diubah menjadi RDD. Data yang sudah di-parse kemudian diubah menjadi DataFrame. Selanjutnya, algoritma K-Means dengan jumlah klaster dan iterasi yang ditentukan dijalankan dengan menggunakan `fit()` pada objek KMeans. Evaluasi pengelompokan dilakukan dengan menghitung Within Set Sum of Squared Errors (WSSSE). Hasil evaluasi ini dicetak ke layar. Terakhir, model yang telah dilatih disimpan dan dapat di-load kembali untuk digunakan pada data baru.
  </td>
    </td>
    </tr>
      <tr align="center">
    <td>
     Slide 53
    <td>
      <img src="https://github.com/raihanhd12/BIG-DATA/assets/95725937/88e8472e-d671-49f8-aab6-6dfedf7b6d53"><br><br>
    Kode di atas menggunakan Apache Spark untuk melakukan pengelompokan data menggunakan algoritma K-Means. Pertama, SparkSession dibuat untuk menginisialisasi sesi Spark. Data kemudian dibaca dari file menggunakan `spark.read.text()` dan diubah menjadi RDD. Data tersebut kemudian diubah menjadi DataFrame. Selanjutnya, model K-Means dengan jumlah klaster 2 dan maksimum iterasi 10 dibangun menggunakan `fit()` pada objek KMeans. Evaluasi pengelompokan dilakukan dengan menghitung Within Set Sum of Squared Errors (WSSSE) dari model yang telah dibangun. Hasil evaluasi ini dicetak ke layar. Terakhir, model yang telah dilatih disimpan dan dapat di-load kembali untuk digunakan pada data baru.
  </td>
    </td>
    </tr>
      <tr align="center">
    <td>
     Slide 54
    <td>
      <img src="https://github.com/raihanhd12/BIG-DATA/assets/95725937/b2b90bd6-485e-405e-a7f6-1ac3f1f20850"><br><br>
      Kode di atas menggunakan Apache Spark untuk melakukan pengelompokan data dengan algoritma K-Means menggunakan modul `pyspark.mllib.clustering`. Pertama, SparkContext dibuat menggunakan `SparkContext.getOrCreate()`. Data kemudian dibaca dari file menggunakan `sc.textFile()` dan diubah menjadi RDD. Selanjutnya, model K-Means dengan jumlah klaster 2, maksimum iterasi 10, dan mode inisialisasi acak dibangun menggunakan metode `train()` pada objek KMeans. Evaluasi pengelompokan dilakukan dengan menghitung Within Set Sum of Squared Errors (WSSSE) menggunakan fungsi `error()`. Hasil evaluasi ini dicetak ke layar. Terakhir, model yang telah dilatih disimpan dan dapat di-load kembali untuk digunakan pada data baru menggunakan metode `save()` dan `load()` pada objek KMeansModel.
  </td>
    </td>
    </tr>
 </table>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
