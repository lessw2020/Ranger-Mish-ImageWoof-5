# Ranger-Mish-ImageWoof-5
Repo for letting users reproduce the new RangerMish combo (and now with Self Attention layer) on FastAI ImageWoof dataset 5 epochs.

Contributors to this effort - FastAI board names:
@LessW2020 / @muellerzr / @Seb / @grankin / @Redknight / @oguiza

Two variations - with and without self attention.  
Both setups set new records for 5 epoch training on ImageWoof (same day).

The highest scores are with @Sebs self attention layer - this is controlled by the --sa 1 param in the training script:
![RangerMish SelfAttention Results](imagewoof-5-epoch-selfa-75.jpg)

and current leaderboard:

![ImageWoof Leaderboard Aug 28 19](Imagewoof-5-epoch-record-552.jpg)


details of an exceptional peak score:
![RangerMish SelfAttention Results](Imagewoof-78-selfatt-5-epoch.jpg)


You can run the notebook with the Self Attention layer as follows:
![Self Attention Usage](Imagewoof-use-sa-param.jpg)

Below are the results without attention layer (--sa 0, which is default).

![Ranger Mish Results](RangerMish-ImageWoof-5-Record-74.jpg)



## How to use:  
Just launch the training script - the script references more optimizers, etc. than what is in this repro so stick with --opt ranger for the optimizer.  Here's an example:
![How to use](how-to-use.jpg)

and link to the leaderboards:
https://github.com/fastai/imagenette

and FastAI forum link:
https://forums.fast.ai/t/meet-mish-new-activation-function-possible-successor-to-relu/53299


