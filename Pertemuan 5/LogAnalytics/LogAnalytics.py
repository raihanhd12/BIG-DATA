# Get the lines from the textfile, create 4 partitions
access_log = sc.textFile("file:/home/cloudera/spark-2.0.0-bin-hadoop2.7/pendidikan.txt", 4)

#Filter Lines with ERROR only
error_log = access_log.filter(lambda x: "tinggi" in x)

# Cache error log in memory
cached_log = error_log.cache()

# Now perform an action -  count
print "Total number of error records are %s" % (cached_log.count())

# Now find the number of lines with 
print "Number of product pages visited that have Errors is %s" % (cached_log.filter(lambda x: "pendidikan" in x).count())

#Catatan
# 1. buat file pendidikan.txt dan masukkan kata dengan cara : sudo vi pendidikan.txt
# 2. cek status hadoop dengan cara : sudo service hadoop-hdfs-namenode status
# 3. jika failed maka hidupkan dengan cara : sudo service hadoop-hdfs-namenode start
