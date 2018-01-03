#evenprocesses
total = 0
processes={}
arrival_time=[]
burst_time=[]
waiting_queue=[]
aux=[]

def take_input():
	n = input("Number of processes:")
	for i in range (0,n):
		a_time=input("Arrival Time:")
		arrival_time.append(a_time)
		b_time=input("Burst Time:")
		burst_time.append(b_time)
		processes[arrival_time[i]] = [i+1 , burst_time[i]]
	return n
def input_time_slice():
	time_slice = input("Time slice:")
	return time_slice
def input_io():
	io = input("Input ouput Time:")
	return io
def output(n):
	print "Arrival Time \t\t\t\t Burst Time"
	for i in range (0,n):
		print arrival_time[i], "\t\t\t\t" , burst_time[i]
def sorting():
	arrival_time.sort()

def vrr(n, time_slice,io):
	count_the_terminated_processes  = 0
	total = 0 
	while (count_the_terminated_processes != n):
		for i in range (0,n):
			check = 0
			check = processes.get(arrival_time[i])[1] 
			if(check!=-1):
				check = check - time_slice
				if(check > 0):
					burst_time[i] = check
					processes[arrival_time[i]] = [i+1 , burst_time[i]]	
					total+=check
				if(check<=0):
					count_the_terminated_processes=+1
					total+=burst_time[i]
					burst_time[i] = -1
					processes[arrival_time[i]] = [i+1 , burst_time[i]]	
			print(total)

no_of_processes=take_input()
time=input_time_slice()
io=input_io()
output(no_of_processes,time,io)
sorting()
rr(no_of_processes,time)
