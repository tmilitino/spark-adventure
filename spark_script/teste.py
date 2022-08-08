from pyspark.sql import SparkSession
from pyspark import SparkContext

appName = "PySpark Example - List to Spark Data Frame"
master = "local"

spark = SparkSession.builder.getOrCreate()


simpleData = [("James", "Vendas", "SP", 30000, 34, 20000),
              ("Miguel", "Vendas", "RJ", 83000, 56, 20000),
              ("Roberto", "Marketing", "SP", 80000, 30, 23000),
              ("Maria", "Financeiro", "SP", 50000, 24, 23000),
              ("Jonas", "Financeiro", "PE", 95000, 40, 24000),
              ("Carla", "Financeiro", "PE", 86000, 36, 19000),
              ("Adriana", "Vendas", "PR", 29000, 53, 15000),
              ("Ana", "Marketing", "PR", 97000, 50, 22000)
              ]

schema = ["funcionario", "departmento", "estado", "salario", "idade", "bonus"]
df = spark.createDataFrame(data=simpleData, schema=schema)
df.groupBy("departmento").avg("salario").show(truncate=False)
