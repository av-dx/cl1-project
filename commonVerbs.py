AIverbs = []
FMFSverbs = []
common = []


AI = open('AIVerbs.txt', 'r')
FMFS = open('FMFSVerbs.txt', 'r')
Common = open('commonVerbs.txt', 'w')
Unique = open('uniqueVerbs.txt', 'w')

AIverbs = AI.readlines()
FMFSverbs = FMFS.readlines()

# print(AIverbs)
# print(FMFSverbs)

for a in AIverbs:
    if a in FMFSverbs:
        common.append(a)

for c in common:
    Common.write(c)
