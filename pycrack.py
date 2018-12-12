import hashlib

from sys import argv
from time import time
from itertools import product
from string import ascii_lowercase, ascii_uppercase, digits

colors = {"red":"\033[91m", 
          "green":"\033[92m", 
          "none":"\033[00m"
         }

def get_charset(arg_charset):
    charset = ""
    charsets = {"L":ascii_lowercase,
                "U":ascii_uppercase,
                "D":digits
               }

    for key in arg_charset:     
        charset += charsets[key]
    return charset


def get_algorithm(arg_algo):
    algorithms = {"md5":hashlib.md5,
                  "sha1":hashlib.sha1,
                  "sha224":hashlib.sha224,
                  "sha256":hashlib.sha256,
                  "sha384":hashlib.sha384,
                  "sha512":hashlib.sha512,
                  "sha3_224":hashlib.sha3_224,
                  "sha3_256":hashlib.sha3_256,
                  "sha3_384":hashlib.sha3_384,
                  "sha3_512":hashlib.sha3_512,
                 }
    return algorithms[arg_algo]


def timer(func):
    def wrapper(*args, **kwargs):
        timer_start = time()
        timer_return = func(*args, **kwargs)
        timer_diff = int(time()-timer_start)

        print(f"{colors['green']}Bruteforce done{colors['none']}")
        print("Statistics")
        print("_________________________________________")
        print("Calculation time: {}{}{} seconds".format(
        colors['green'],
        timer_diff,
        colors['none']))
        print("_________________________________________")

        return timer_return
    return wrapper


@timer
def bruteforce(hash_, charset, min_length, max_length, algo, debug):
   
    for length in range(int(min_length), int(max_length) + 1):
        for attempt in product(charset, repeat=length):
            hashed = "".join(attempt).encode("utf-8") 
            hashed = algo(b'wgmy{h3r3_1s_y0ur_'+hashed+b'_br0!}').hexdigest()

            if hashed != hash_:
                if debug:
                    print(f"{'wgmy{h3r3_1s_y0ur_'}{''.join(attempt)}{'_br0!}'}")
            else:
                if debug:
                    print(f"{''.join(hashed)}")
                return "".join(attempt)


def main():
    hash__, charset_, min_length_, max_length_, algo_, debug_ = argv[1:7]
    charset = get_charset(charset_)
    algo = get_algorithm(algo_)
    res = bruteforce(hash__, charset, min_length_, max_length_, algo, debug_)

    if res is None:
        print(f"{colors['red']}No matches found.{colors['none']}")
    print(colors['none'])


if __name__ == "__main__":
    print("\n"*90)
    main()