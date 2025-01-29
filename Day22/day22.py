data_path = './day22_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')
test_data = [1,10,100,2024]

def get_next_secret(secret):
    # step 1
    mixer = secret * 64
    secret = mix(mixer, secret)
    secret = prune(secret)

    # step 2
    mixer = secret // 32
    secret = mix(mixer, secret)
    secret = prune(secret)

    # step 3
    mixer = secret * 2048
    secret = mix(mixer, secret)
    secret = prune(secret)

    return secret


def mix(mixer, secret):
    return mixer ^ secret

def prune(secret):
    return secret % 16777216


def find_nth_secret(n, secret):
    for i in range(n):
        secret = get_next_secret(secret)
    return secret

total = 0

for val in data:
    total += find_nth_secret(2000, int(val))


print("Part 1 Solution: ", total)