from rockstar import RockStar

from datetime import datetime

current_date = datetime.now()
epoch_date = datetime.fromtimestamp(0)
time_since_epoch = current_date - epoch_date

# https://github.com/bjtucker/varaq/blob/master/gettingstarted.txt
varaq_code = "~ nuqneH { \"nuqneH 'u'?\" cha' } pong"
rock_it_bro = RockStar(
    days=time_since_epoch.days, file_name="helloworld.vq", code=varaq_code
)
rock_it_bro.make_me_a_rockstar()
