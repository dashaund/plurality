import sys

if len(sys.argv) > 10:
    print("You can only enter a maximum of 9 candidates")
    sys.exit()

num = len(sys.argv)
candidates = []
voters = 5

for i in range(1,num):
    candidates+=[sys.argv[i]]

vote = ""
votes = [0]*len(candidates)

for i in range(0,voters):
    vote = input("Enter candidate name\n$ ")
    for i in range(0,len(candidates)):
        if vote == candidates[i]:
            votes[i]+=1
            break

print(votes)

x=0
for i in range(0,len(votes)):
    if votes[i] > x:
        x = votes[i]

winners = []
for i in range(0,len(candidates)):
    if x == votes[i]:
        winners += [candidates[i]]

print("Winner(s):")
for i in winners:
    print(i)