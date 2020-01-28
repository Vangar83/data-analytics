def clothes(shoes):
    if shoes == "Ted Baker":
      return 150
    elif shoes == "Clarks":
      return 80
def clothes(coat):
    if coat == "Howick":
      return 100
    elif coat == "Ted Baker":
        return 200
def clothes(jacket):
    if jacket == "Topman":
        return 50
    elif jacket == "Linea":
        return 60

    def clothes_cost(shoes, coat, jacket):
        return clothes(shoes) + clothes(coat) + clothes(jacket)

    print (clothes_cost('Ted Baker', 'Howick', 'Topman'))
