# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    laiki = []
    for i in range(n):
        laiki.append(0)

    for i in range(m):
        etime = min(laiki)
        thread = laiki.index(etime)
        laiki[thread] = laiki[thread] + data[i]  
        output.append((thread, etime))

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count

    n = 0
    m = 0

    mas = list(map(int,input().split()))
    n = mas[0]
    m = mas[1]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int,input().split()))


    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for v, d in result:
        print(v, d)



if __name__ == "__main__":
    main()
