class stations:
    def __init__(self, name, nxt):
        self.name = name
        self.nxt = nxt


top = 2
lst = [None] * 5
lst[0] = stations("osaka", -1)
lst[1] = stations("nagoya", 3)
lst[2] = stations("tokyo", 4)
lst[3] = stations("kyoto", 0)
lst[4] = stations("yokohama", 1)


def insStationlist(insIdx, insName, prevIdx):
    lst.append("None")
    lst[insIdx] = stations(insName, lst[prevIdx].nxt)
    lst[prevIdx].nxt = insIdx


def delStationList(delIdx, prevIdx):
    lst[prevIdx].nxt = lst[delIdx].nxt

def print_st():
    idx = top
    while idx != -1:
        print("[%s]⇨" % lst[idx].name, end="")
        idx = lst[idx].nxt
    print()


insStationlist(5, "sinagawa", 2)
print_st()
delStationList(5, 2)
print_st()
