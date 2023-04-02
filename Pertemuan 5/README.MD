### **Nama**      : Raihan Hidayatullah Djunaedi
### **Kelas**     : TI -3B
### **Tugas**      : Pertemuan 5

# Screenshot dan Penjelasan
Kode 1 - Accumulator: sc, accumulator, parallelize, lambda, value 

- sc adalah objek yang bertanggung jawab untuk membuat koneksi ke cluster Spark dan mengatur konfigurasi yang diperlukan untuk menjalankan aplikasi Spark.

- accumulator adalah tipe variabel yang dapat digunakan untuk mengakumulasi nilai secara paralel pada cluster Spark. 

- parallelize adalah metode pada objek SparkContext yang digunakan untuk membuat RDD dari data yang ada di memori lokal. 

- lambda adalah sebuah fungsi anonim pada Python yang dapat digunakan untuk melakukan operasi sederhana pada setiap elemen RDD.

- value adalah atribut pada objek accumulator yang digunakan untuk mengakses nilai terakhir yang diakumulasi pada accumulator tersebut.

Kode 2 - Broadcast: broadcast, list, range

- Broadcast dalam Pyspark digunakan untuk mengirimkan variabel yang hanya perlu dibaca dan tidak diubah ke setiap node dalam cluster.

- List dapat digunakan untuk menyimpan dan mengakses sejumlah nilai yang berbeda secara bersamaan.

- Fungsi range pada Pyspark dapat digunakan untuk menghasilkan rentang nilai numerik dalam suatu list. 

Kode 3 - PairRDD: map, collect, len, keys, values

- Fungsi map digunakan untuk mengaplikasikan fungsi pada setiap elemen PairRDD dan mengembalikan RDD baru yang terdiri dari pasangan kunci dan nilai baru.

- Fungsi collect digunakan untuk mengumpulkan semua elemen RDD menjadi suatu koleksi pada driver program.

- Fungsi len digunakan untuk menghitung jumlah elemen dalam RDD.

- Fungsi keys digunakan untuk mengembalikan RDD baru yang hanya terdiri dari kunci dalam setiap pasangan kunci dan nilai di RDD.

- Fungsi values digunakan untuk mengembalikan RDD baru yang hanya terdiri dari nilai dalam setiap pasangan kunci dan nilai di RDD.

Kode 4 - WordCount: flatMap, reduceByKey, split

- Fungsi flatMap digunakan untuk memisahkan setiap baris dalam teks menjadi kata-kata terpisah.

- Fungsi reduceByKey digunakan untuk menghitung jumlah kemunculan kata pada RDD.

- Fungsi split digunakan untuk memecah setiap baris teks menjadi array kata-kata yang terpisah berdasarkan pemisah spasi atau karakter lain yang ditentukan.

Kode 7 - LogAnalytics: textFile, filter, cache, count

- Fungsi textFile digunakan untuk membaca file log dan mengembalikan RDD baru dengan satu baris teks sebagai elemen RDD.

- Fungsi filter digunakan untuk memfilter baris-baris teks yang mengandung pola tertentu dalam RDD.

- Fungsi cache digunakan untuk menyimpan RDD di memori untuk mengoptimalkan kinerja proses pengolahan data berulang.

- Fungsi count digunakan untuk menghitung jumlah elemen dalam RDD.

Kode 8 - UnderstandingRDD: defaultParallelism, getNumPartitions, mapPartitionsWithIndex, repartition, coalesce, toDebugString

- Fungsi defaultParallelism digunakan untuk mendapatkan jumlah partisi default yang digunakan oleh RDD. 

- Fungsi getNumPartitions digunakan untuk mendapatkan jumlah partisi yang digunakan oleh RDD saat ini.

- Fungsi mapPartitionsWithIndex digunakan untuk menerapkan fungsi pada setiap partisi RDD dengan indeks partisi sebagai parameter masukan.

- Fungsi repartition digunakan untuk memecah ulang RDD menjadi sejumlah partisi yang baru.

- Fungsi coalesce digunakan untuk menggabungkan beberapa partisi menjadi satu partisi. 

- Fungsi toDebugString digunakan untuk mendapatkan string yang mewakili struktur RDD saat ini.

<table>
  <tr align="center">
    <td>
    Accumulator
    <td> <img src="https://user-images.githubusercontent.com/95725937/227154198-9bc0d6b6-d351-4df0-a201-d85b6f42fe16.png" width=70% height=70%><br>
        Kode tersebut membuat sebuah variabel accumulator yang dinamakan myaccum dengan nilai awal 0 menggunakan metode sc.accumulator yang disediakan oleh SparkContext sc. Kemudian membuat sebuah RDD (Resilient Distributed Dataset) yang dinamakan myrdd dengan memparallelkan kisaran angka dari 1 hingga 99 (tidak termasuk 100). Setelah itu menerapkan operasi foreach pada setiap elemen dari RDD myrdd. Fungsi lambda yang dilewatkan ke operasi foreach menambahkan nilai dari setiap elemen ke dalam accumulator myaccum. Akhirnya, Mencetak nilai dari accumulator menggunakan metode value. Output dari kode tersebut adalah jumlah dari semua elemen dalam RDD, yang bernilai 4950.
    </td>
    </td>
    </tr>
    <tr align="center">
    <td>    
    Broadcast
    <td><img src="https://user-images.githubusercontent.com/95725937/227154393-c896915a-a461-4193-bf72-1d5cf854e493.png" width=70% height=70%><br>
  Kode tersebut membuat variabel broadcastVar dengan daftar bilangan bulat dari 1 hingga 99 menggunakan metode sc.broadcast. Metode broadcastVar.value digunakan untuk mengambil nilai variabel tersebut. Variabel tersebut didistribusikan ke setiap executor di dalam cluster menggunakan metode sc.broadcast, sehingga mengurangi overhead jaringan. Output dari kode tersebut adalah daftar bilangan bulat dari 1 hingga 99 yang dicetak menggunakan metode value.
  </td>
    </td>
    </tr>
    <tr align="center">
    <td>
    PairRDD
    <td><img src="https://user-images.githubusercontent.com/95725937/227154401-7b816658-e21d-44ba-8156-ec19e3f97f41.png" width=70% height=70%><br>
      Kode tersebut membuat sebuah RDD bernama myRDD dengan tiga elemen menggunakan metode parallelize dari SparkContext sc. Selanjutnya, sebuah Pair RDD dengan nama myPairRDD dibuat dari myRDD dengan menggunakan metode map. Fungsi lambda yang dilewatkan ke metode map akan mengembalikan tuple yang terdiri dari elemen RDD dan panjangnya. Metode collect digunakan untuk mencetak tuple dari setiap elemen dalam RDD myPairRDD. Selain itu, metode keys digunakan untuk mengambil semua kunci dari setiap tuple dalam RDD myPairRDD, dan metode values digunakan untuk mengambil semua nilai dari setiap tuple dalam RDD myPairRDD. Output dari kode tersebut adalah sebuah tuple yang terdiri dari elemen RDD dan panjangnya, serta dua buah daftar yang masing-masing berisi kunci dan nilai dari setiap tuple dalam RDD myPairRDD.
  </td>
    </td>
    </tr>
    <tr align="center">
    <td>
    WordCount
    <td>
      <img src="https://user-images.githubusercontent.com/95725937/227154712-aae7c89b-8240-4850-b369-4407c315bb0b.png" width=70% height=70%>
      <img src="https://user-images.githubusercontent.com/95725937/227154745-a9869069-51da-48c7-aed3-b0dae5d12bc2.png" width=70% height=70%><br>
      Pertama, kode membaca file README.md menggunakan metode textFile dari SparkContext sc. Selanjutnya, teks dalam file tersebut dibagi menjadi kata-kata dengan menggunakan fungsi split pada setiap baris teks melalui metode flatMap. Setiap kata dalam RDD tersebut akan dibuat menjadi tuple dengan nilai awal 1 melalui fungsi map. Setiap tuple dengan kata yang sama akan dijumlahkan melalui metode reduceByKey dengan menggunakan fungsi add untuk menjumlahkan nilai. Hal ini dilakukan untuk melakukan penghitungan kata yang serupa dalam file. Hasil penghitungan jumlah kemunculan kata-kata disimpan dalam variabel output menggunakan metode collect, dan kemudian dicetak ke layar menggunakan for loop untuk mengiterasi setiap kata dan jumlah kemunculan dalam variabel output. Jumlah kemunculan kata dicetak dengan format "kata: jumlah".
  </td>
    </td>
        </tr>
    <tr align="center">
    <td>
    LogAnalytics
         <td>      
      <img src="https://user-images.githubusercontent.com/95725937/229344529-729a313b-8224-4c0e-8618-c8d309d40d13.png" width=70% height=70%><br>
           
  </td>
    </td>    
    </tr>
    <tr align="center">
    <td>
    SystemCommandsReturnCode
         <td>
      <img src="https://user-images.githubusercontent.com/95725937/227154750-cac14af7-38f3-4299-a129-af5fc647b84d.png" width=70% height=70%>
      <img src="https://user-images.githubusercontent.com/95725937/227154756-ac2e8841-1026-4fc9-92ea-dd7dbf2a0018.png" width=70% height=70%><br>
           Pada baris pertama, digunakan import sys.process._ untuk mengimport library sys.process. Selanjutnya, perintah ls /tmp dijalankan menggunakan ! operator dan disimpan dalam variabel res. Hasil dari perintah tersebut akan dicetak ke layar dengan menggunakan println. Jika perintah berhasil dijalankan, maka nilai variabel res akan sama dengan 0, jika tidak berhasil maka nilai variabel res akan bernilai non-zero.
  </td>
    </td>    
    </tr>
    <tr align="center">
    <td>
    SystemCommandsOutputCode
    <td><img src="https://user-images.githubusercontent.com/95725937/227155533-dab87547-c883-4fa5-a191-0cc1f191dc7c.png" width=70% height=70%> <br>
  Pada baris pertama, digunakan import sys.process._ untuk mengimport library sys.process. Selanjutnya, perintah hadoop fs -ls dijalankan menggunakan !! operator dan disimpan dalam variabel output. Hasil dari perintah tersebut akan dicetak ke layar dengan menggunakan println. Operator !! pada Scala akan menampilkan keluaran dari command shell dan mengembalikan hasil sebagai String dalam bentuk keluaran tersebut. Dalam hal ini, variabel output akan berisi output dari perintah hadoop fs -ls.
  </td>
   </tr>
 </table>
