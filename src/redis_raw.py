"""Test insert, update, select and delete with redis"""
import redis

redis_conn = redis.Redis(host="localhost", port=6379, db=0)

# para insert e update
redis_conn.set("chave_1", "trocando_o_meu_valor")

# select
meu_valor = redis_conn.get("chave_1").decode("utf-8")
# print(meu_valor)
# print(type(meu_valor))

# delete
redis_conn.delete("chave_1")


### comandos para hash
meu_hash = {    # chave de exemplo
    "nome": "joao", # field: values
    "idade": 30,
    "cidade": "sao paulo"
}
# insert and update
redis_conn.hset("meu_hash", "nome", "joao")
redis_conn.hset("meu_hash", "idade", "idade")
redis_conn.hset("meu_hash", "cidade", "curitiba")

# select
valor_1 = redis_conn.hget("meu_hash", "nome").decode("utf-8")
# print(valor_1)

redis_conn.hdel("meu_hash", "cidade")


### buscas por existencia
elem = redis_conn.exists("chave_1")
# print(elem)

elem_2 = redis_conn.hexists("meu_hash", "nome")
# print(elem_2)


### Expiracao de dados
# dados -> TTL -> Time to Live [segundos]
redis_conn.set("chave_del", "esse valor sera deletado", 12)
redis_conn.expire("meu_hash", 30)
