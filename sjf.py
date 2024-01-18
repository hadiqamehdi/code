def bubble_sort(arrivaltime, bursttime, n):
    for i in range(n):
        for j in range(0, n - i - 1):
            if arrivaltime[j] > arrivaltime[j + 1]:
                arrivaltime[j], arrivaltime[j + 1] = arrivaltime[j + 1], arrivaltime[j]
                bursttime[j], bursttime[j + 1] = bursttime[j + 1], bursttime[j]
            elif arrivaltime[j]==arrivaltime[j+1] and bursttime[j]>bursttime[j+1]:
                arrivaltime[j], arrivaltime[j + 1] = arrivaltime[j + 1], arrivaltime[j]
                bursttime[j], bursttime[j + 1] = bursttime[j + 1], bursttime[j]



  
   

def sjf(arrivaltime, bursttime, n):
    ct = [0] * n
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    for i in range(n):
        if i == 0:
            ct[i] = bursttime[i] + arrivaltime[i]
        else:
            ct[i] = ct[i - 1] + bursttime[i]

        tat[i] = ct[i] - arrivaltime[i]
        wt[i] = tat[i] - bursttime[i]
        total_wt += wt[i]
        total_tat += tat[i]

    print("PROCESS\t ARRIVALTIME\t BURSTTIME \t COMPLETIONTIME\t WAITINGTIME\t TURNAROUNDTIME")
    for i in range(n):
        print("P[{}]\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(i + 1, arrivaltime[i], bursttime[i], ct[i], wt[i], tat[i]))

    avg_wt = total_wt / n
    avg_tat = total_tat / n
    print("average waiting time:", avg_wt)
    print("average turnaround time:", avg_tat)


n = int(input("Enter total number of processes:"))
arrivaltime = [0] * n
bursttime = [0] * n

for i in range(n):
    arrivaltime[i] = int(input(f"Enter process arrival time P[{i + 1}]: "))
    bursttime[i] = int(input(f"Enter process burst time P[{i + 1}]: "))
bubble_sort(arrivaltime, bursttime, n)
sjf(arrivaltime, bursttime, n)

