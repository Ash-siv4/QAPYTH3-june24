# 4.	We need to do some maintenance on a dictionary of machines:
machines = {'user100': 'yogi',
           'user1': 'booboo',
           'user2': 'rupert',
           'user3': 'teddy',
           'user4': 'care',
           'user5': 'winnie',
           'user6': 'sooty',
           'user7': 'padders',
           'user8': 'polar',
           'user9': 'grizzly',
           'user10': 'baloo',
           'user11': 'bungle',
           'user12': 'fozzie',
           'user13': 'huggy',
           'user14': 'barnaby',
           'user15': 'hair',
           'user16': 'greppy'}

# Don't type this in!
# It should be available for you to edit in Ex5_4.py in the labs' directory (or your home directory if on Linux).
# Without altering the initial definition of the dictionary, write code that will implement the following changes:
# a)	user14 no longer has a machine assigned. - remove user14's machine assignment (the value)
del machines['user14']
print(machines)
# b)	The name of user15's machine is changed to 'cinnamon'.
machines['user15'] = 'cinnamon'
print(machines)
# c)	user16 is leaving the company and a new user, user17 will be assigned his machine.
#       - the value stays the same, but the key is changing
# machines['user17'] = machines['user16'] # 'greppy'
# del machines['user16']
machines['user17'] = machines.pop('user16')
# pop() method removes 'user16' and returns its value
print(machines)
# d)	user4, user5, and user6 are all leaving at the same time,
#       but their machine names are to be stored in a list called unallocated. Hint: pop in a loop.
unallocated = []
for user in ['user4', 'user5', 'user6']:
    unallocated.append(machines.pop(user))
print(unallocated)
print(machines)
# e)	user8 gets another machine called 'kodiak' in addition to the one they already have.
machines['user8'] = [machines['user8'], 'kodiak']
print(machines)
# f)	Print a list of users with their machine in any order. Print each user/machine pair on a separate line.
for user, machine in machines.items():
    print(f'{user}:{machine}')
# g)	Print a list of unallocated machines, sorted alphabetically.
print("Unallocated machines:", sorted(unallocated))