import time
from multiprocessing import Pool, cpu_count

# Defining factorize function
def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def main():
    numbers = [128, 255, 99999, 10651060]
    
    # Synch version
    start_time = time.time()
    results = [factorize(number) for number in numbers]
    end_time = time.time()
    print("Synch version done in: ", end_time - start_time, "seconds")
    print(results)

    # Multiprocessing version
    start_time = time.time()
    with Pool(cpu_count()) as pool:
        results = pool.map(factorize, numbers)
    end_time = time.time()
    print("Multiprocessing version is done in: ", end_time - start_time, "seconds")
    print(results)

if __name__ == "__main__":
    main()