"""
# network_hash_gen

network_hash_gen provides functions for hashing passwords for network devices
like routers and switches.

Usually there are 3 kinds of functions for each type of hash.

- the `..._hash` function, which simply takes a password and returns a hash.
- the `..._hash_seeded` function with takes a hash and a seed for the random
  number generator that generates the salt.
  This always returns the same hash for the same password+seed combination.
  This is useful for generating configs that are diffed at some point to
  prevent changing hashes all the time.
  Usually a combination of the hostname and username is used as a seed.
- the `..._hash_salted` function which takes a salt directly.
  This function should only be used if you know what you are doing.
  If possible prefer one of the other functions.
  This function does not check whether that salt makes sense/is supported for
  that hash and may have undefined behaviour if a invalid salt is given.

## Example

```
>>> from network_hash_gen.cisco_ios.type_9 import type_9_hash, type_9_hash_seeded
>>> type_9_hash("foobar")
'$9$b52oqNlalWEBTi$f7ziTlkOvnMb.mXuXejYfjBGzQ5GZKNRGaFFYZlYecQ'
>>> type_9_hash_seeded("foobar", "$hostname-$username")
'$9$XpsDCh72ruxTQc$Cm80vIgCAQPhWrLJczX53Z7qVg0AxKui6t8.QbWfBsU'
```
"""

__version__ = "0.0.1"
