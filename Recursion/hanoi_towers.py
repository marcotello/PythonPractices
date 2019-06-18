def hanoi(disk, source, dest, aux):
    
    if disk == 1:
        print("{} {}".format(source, dest))
    else:
        hanoi(disk-1, source, aux, dest)
        print("{} {}".format(source, dest))
        hanoi(disk-1, aux, dest, source)



def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks
    TODO: print the steps required to move all disks from source to destination
    """
    source = "S"
    dest = "D"
    aux = "A"

    hanoi(num_disks, source, dest, aux)

print("Tower 1")
tower_of_Hanoi(2)

print("\n\nTower 2")
tower_of_Hanoi(3)

print("\n\nTower 3")
tower_of_Hanoi(4)