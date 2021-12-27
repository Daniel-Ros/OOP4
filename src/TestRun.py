import time
from GraphAlgo import GraphAlgo

def main():
    file_l = "../test_data/g3.json"
    file_s = "../test_data/g1_saved.json"
    ga = GraphAlgo()
    tic = time.perf_counter()
    ga.load_from_json(file_l)
    toc = time.perf_counter()
    print(F"load took :{toc-tic:0.4f} sec")
    tic = time.perf_counter()
    res = ga.shortest_path(0, 99)
    toc = time.perf_counter()
    print(F"shortest path took :{toc - tic:0.4f} sec and the resualt is:{res}")
    tic = time.perf_counter()
    #res = ga.centerPoint()
    toc = time.perf_counter()
    print(F"center took :{toc - tic:0.4f} sec and the resualt is:{res}")
    tic = time.perf_counter()
    res = ga.TSP([0,1,25,50,75,80,99,42,87,13,57])
    toc = time.perf_counter()
    print(F"TSP took :{toc - tic:0.4f} sec and the resualt is:{res}")
    tic = time.perf_counter()
    ga.save_to_json(file_s)
    toc = time.perf_counter()
    print(F"save took :{toc - tic:0.4f} sec")



if __name__ == "__main__":
    main()
