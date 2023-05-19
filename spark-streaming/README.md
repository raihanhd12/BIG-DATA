<a name="readme-top"></a>
## Tugas Praktikum

1. Silakan selesaikan praktikum tersebut sesuai langkah-langkah sebelumnya, lalu laporkan hasilnya berupa link repository GitHub dengan nama **spark-streaming** disertai dengan screenshot hasilnya.
2. Jelaskan perbedaan spark streaming dengan metode stateless dan stateful stream processing ?
3. Jelaskan masing-masing maksud kode berikut sesuai nomor kodenya pada laporan praktikum Anda!

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Daftar Isi</summary>
  <ol>
    <li>
      <a href="#pertanyaan">Pertanyaan</a>
      <ul>
        <li><a href="#jawaban">Jawaban</a></li>
      </ul>
    </li>
    <li>
      <a href="#screenshot-hasil">Screenshoot Hasil</a>
    </li>
  </ol>
</details>

## Pertanyaan
<img src = 'https://user-images.githubusercontent.com/95725937/232274361-4045e4c8-9e8c-409d-810e-a31324045822.png' width=40% height=30%>

## Jawaban
  ```sh
  1. Mendefinisikan variabel mylist dan myschema
  ```
  ```sh
  2. Membuat DataFrame baru menggunakan spark.createDataFrame.
  ```
  ```sh
  3. Membuat RDD dari data yang sudah di-parallelisasi dan mengubahnya menjadi DataFrame dengan menggunakan toDF.
  ```
  ```sh
  4. Mengirim file ke sistem file hadoop.
  ```
  ```sh
  5. Membuat objek SQLContext dan membuat temporary view menggunakan createOrReplaceTempView, kemudian menampilkan data menggunakan show.
  ```
  ```sh
  6. Membaca file teks menggunakan textFile, melakukan pemetaan menggunakan map, melakukan operasi lambda, menghilangkan karakter whitespace dengan strip, mendefinisikan StructField, dan mengubah data menjadi StringType.
  ```
  ```sh
  7. Membaca data dari JDBC data source menggunakan spark.read.format, kemudian menentukan opsi dan memuat data menggunakan load.
  ```
  ```sh
  8. Menampilkan data menggunakan show.
  ```
  ```sh
  9. Mengumpulkan data menggunakan collect, mengambil sejumlah data dari RDD menggunakan take.
  ```
  ```sh
  10. Membuat RDD baru menggunakan makeRDD dan membuat Dataset baru menggunakan createDataset.
  ```
  ```sh
  11. Melakukan filter pada DataFrame.
  ```
  ```sh
  12. Mengubah kolom menjadi DataFrame, mengubah DataFrame menjadi tabel menggunakan as dan toDF, dan mengambil nilai pertama menggunakan first.
  ```
  ```sh
  13. Menampilkan daftar database, tabel, dan fungsi, mengecek apakah data di-cache menggunakan isCached, dan memilih kolom menggunakan select.
  ```
  ```sh
  14. Membaca file teks menggunakan read.text.
  ```
  ```sh
  15. Membaca file json menggunakan load, kemudian mencetak skema data menggunakan printSchema.
  ```
  ```sh
  16. Menulis data ke file sistem menggunakan write, kemudian menyimpan data menggunakan save.
  ```
  ```sh
  17. Menulis data ke format parquet.
  ```
  ```sh
  18. Menentukan opsi untuk pembacaan file csv dan menentukan header dan codec.
  ```

## Screenshot Hasil
<table>
  <tr align="center">
    <td>
    Analitik DataFrame
    <td> 
      <img src="https://user-images.githubusercontent.com/95725937/232275028-2a2ffa18-241f-4a67-b3a6-98ba25b0bbbd.png"><br><br>
      <img src="https://user-images.githubusercontent.com/95725937/232275030-62c5ac82-acb8-4336-b360-f697923d2244.png">
    </td>
    </td>
    </tr>
    <tr align="center">
    <td>    
    Bekerja dengan berkas teks
    <td><img src="https://user-images.githubusercontent.com/95725937/232275032-f66fd95d-c623-4054-89c8-68c16910c93c.png">
  
  </td>
    </td>
    </tr>
    <tr align="center">
    <td>
        Bekerja dengan CSV
    <td><img src="https://user-images.githubusercontent.com/95725937/232275033-28bb12ed-d68c-4dc7-b407-37bafa5e3710.png">      
  </td>
    </td>
    </tr>
    <tr align="center">
    <td>      
    Bekerja dengan JSON
    <td>
      <img src="https://user-images.githubusercontent.com/95725937/232275034-602a79dc-947b-49f7-be11-d6343aca7ae4.png">
  </td>
    </td>
        </tr>
    <tr align="center">
    <td>
    Mengonversi DataFrames ke RDDs
         <td>      
      <img src="https://user-images.githubusercontent.com/95725937/232275612-7cf7def8-e75a-4d22-98b5-62fde7be97a6.png">           
  </td>
    </td>    
    </tr>
        <tr align="center">
    <td>      
    Membuat DataFrame dari Database Eksternal
         <td>      
      <img src="https://user-images.githubusercontent.com/95725937/232275038-d3578019-4f93-42bc-bfd4-5b40ccf61291.png">           
  </td>
    </td>    
    </tr>
    <tr align="center">
    <td>      
    Membuat Datasets
         <td>
      <img src="https://user-images.githubusercontent.com/95725937/232275652-b0382b00-c48f-49e9-acf0-c9ba6f1d913f.png">
  </td>
    </td>    
    </tr>
    <tr align="center">
    <td>
    Mengakses Metadata menggunakan Catalog
    <td><img src="https://user-images.githubusercontent.com/95725937/232275655-56318603-5401-40f3-a076-e4786aadf0ce.png"><br><br>
      <img src="https://user-images.githubusercontent.com/95725937/232275659-43f018ec-a5c8-40ac-b9d1-aef590be65e3.png">
       </td>
   </tr>
       <tr align="center">
    <td>
    Mengonversi DataFrame ke Datasets dan sebaliknya
    <td><img src="https://user-images.githubusercontent.com/95725937/232275663-38fb1df6-1dd0-4a60-86d3-1535a3ff4266.png">
       </td>
   </tr>
 </table>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
