import hashlib

# 1 - Verify the algorithm available
print("-------------------")
print("Available algorithms")
print(hashlib.algorithms_available)

# 2 - Available algorithms for the current SO
print("-------------------")
print("Guaranteed algorithms")
print(hashlib.algorithms_guaranteed)

# 3 - Using sha256
print("-------------------")
print("Using sha256")
algorithm = hashlib.sha256()
message = 'Python is cool'.encode()
algorithm.update(message)
print(algorithm.hexdigest())


# 4 - Using md5
print("-------------------")
print("Using md5")
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())