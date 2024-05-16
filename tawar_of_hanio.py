#  Python program to find solution for Tower of Hanoi puzzle


def towers_of_hanio(n, source, target, auxiliary):
    if n>0:
        towers_of_hanio(n-1 , source , auxiliary , target)

        print(f"move disk {n} from {source} to {target}")

        towers_of_hanio(n-1 , auxiliary , target , source)

num_disks=3
towers_of_hanio(num_disks, "source" , "aux" , "target")