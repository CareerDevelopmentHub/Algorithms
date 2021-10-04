def towerMovement(h,fp, tp, wp):
        if h>=1:
            towerMovement(h-1,fp,wp,tp)
            diskMovement(fp,tp)
            towerMovement(h-1,wp,tp,fp)

def diskMovement(fp,tp):
    print("Movement of disk from",fp,"to",tp)

towerMovement(5,"A","B","C")
