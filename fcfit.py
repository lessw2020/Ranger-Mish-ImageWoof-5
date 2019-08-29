#flat and cosine annealer - @mgrankin invented
#let's make it fast and easy - @lessw2020

def fcfit(learn, num_epoch=2, lr=4e-3, start_pct=.72, f_show_curve=True):
    if num_epoch<1:
        raiseValueError("num_epoch must be 1 or higher")
    n = len(learn.data.train_dl)
    anneal_start = int(n*num_epoch*start_pct) #compute what batch to start
    batch_finish = (n*num_epoch - anneal_start)
    phase0 = TrainingPhase(anneal_start).schedule_hp('lr', lr)
    phase1 = TrainingPhase(n*5 - anneal_start).schedule_hp('lr', lr, anneal=annealing_cos)
    phases = [phase0, phase1]
    sched = GeneralScheduler(learn, phases)
    #save the setup
    learn.callbacks.append(sched)
    #start the training
    print(f"fcfit: num_epochs: {num_epoch}, lr = {lr}") 
    print(f"Flat for {anneal_start} epochs, then cosine anneal for {batch_finish}")
    learn.fit(num_epoch)
    #bonus -show lr curve?
    if f_show_curve:    
        learn.recorder.plot_lr()    
    