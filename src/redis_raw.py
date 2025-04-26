"""Test insert, update, select and delete with redis"""
import redis

redis_conn = redis.Redis(host="localhost", port=6379, db=0)

# para insert e update
redis_conn.set("chave_1", "trocando_o_meu_valor")

# select
meu_valor = redis_conn.get("chave_1").decode("utf-8")
print(meu_valor)
print(type(meu_valor))

# delete
redis_conn.delete("chave_1")
