from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql.types import FloatType, StructType, StructField, StringType, StringType, IntegerType
from pyspark.sql import functions as F

schema = StructType([StructField("ORDEM", StringType()),
                     StructField("ANOMES", StringType()),
                     StructField("COD_NCM", StringType()),
                     StructField("DESC_NCM", StringType()),
                     StructField("PAIS_COD_O", StringType()),
                     StructField("PAIS_ORIGEM ", StringType()),
                     StructField("PAIS_COD_A", StringType()),
                     StructField("PAIS_AQUIS ", StringType()),
                     StructField("UND_ESTAT", StringType()),
                     StructField("UND_COMERC", StringType()),
                     StructField("UND_MEDIDA", StringType()),
                     StructField("PRODUTO", StringType()),
                     StructField("QTDE_ESTATISTICA", StringType()),
                     StructField("PESO_LIQUIDO", StringType()),
                     StructField("VMLE_DOLAR", StringType()),
                     StructField("VL_FRETE_DOLAR", StringType()),
                     StructField("VL_SEGURO_DOLAR", StringType()),
                     StructField("VALOR_UN_PROD_DOLAR", StringType()),
                     StructField("QTD_COMERCIAL", StringType()),
                     StructField("TOT_UN_PROD_DOLAR", StringType()),
                     StructField("UND_DESEMBARQUE", StringType()),
                     StructField("UND_DESEMBARACO ", StringType()),
                     StructField("INCOTERM", StringType()),
                     StructField("NAT_INFORMACAO", StringType()),
                     StructField("SITUACAO_DESPACHO", StringType()), ])


to_float = lambda x: float(0 if x == None else x.replace(',', ".").strip())


udf_to_float = F.udf(to_float, FloatType())


spark: SparkSession = SparkSession.builder \
    .master("spark://172.22.0.2:7077")\
    .appName("siscori_spark")\
    .getOrCreate()

df = spark.read.format("csv").option(
    "delimiter", "@").option("header", "true").load("/files/CAPI90*",)

df = df.withColumnRenamed("TOT.UN.PROD.DOLAR    ","TOT_UN_PROD_DOLAR")
df = df.withColumnRenamed("COD.NCM ","COD_NCM")

df = df.withColumn("TOT_UN_PROD_DOLAR", udf_to_float(df['TOT_UN_PROD_DOLAR']))
print(df.count())
df_groupby = df.groupBy("COD_NCM").agg({"TOT_UN_PROD_DOLAR": "sum"})

df_groupby.coalesce(4)\
   .write.format("csv")\
   .option("header", "true")\
   .save("mydata3.csv")
