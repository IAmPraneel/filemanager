def selection_sort():
    print("How many numbers? ")
    n = int(input())
    arr = []

    for i in range(n):
        print("Enter number: ")
        num = int(input())
        arr.append(num)

    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx = j
        temp = arr[i]
        arr[i]=arr[min_idx]
        arr[min_idx]=temp

    print("sorted array: ",arr)

def job_scheduling():
    n = int(input("Enter number of jobs: "))
    jobs = []

    for i in range(n):
        print("Job ",i)
        s = int(input("Start time: "))
        f = int(input("Finish time: "))
        jobs.append([s,f])

    for i in range(n):
        for j in range(0,n-i-1):
            if jobs[j][1] > jobs[j+1][1]:
                temp = jobs[j]
                jobs[j] = jobs[j + 1]
                jobs[j + 1] = temp
    selected = []
    last_end = -1

    for i in range(n):
        s = jobs[i][0]
        f = jobs[i][1]

        if s >=last_end:
            selected.append(jobs[i])
            last_end = f
    print("Selected jobs: ")
    for i in range(len(selected)):
        print("start: ",selected[i][0]," finish: ",selected[i][1])

print("Would you like selection sort (1) or job scheduling (2)")
option = int(input())
if option == 1:
    selection_sort()
if option == 2:
    job_scheduling()
if option != 1 or option != 2:
    print("No")