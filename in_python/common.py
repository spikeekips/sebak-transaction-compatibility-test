import argon2


def argon2_hash(s):
    return argon2.low_level.hash_secret_raw(
        s,
        b"sebaknetwork",
        time_cost=3,
        memory_cost=32 * 1024,
        parallelism=4,
        hash_len=32,
        type=argon2.low_level.Type.I,
    )
