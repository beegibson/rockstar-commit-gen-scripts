from rockstar import RockStar

from datetime import datetime

current_date = datetime.now()
epoch_date = datetime.fromtimestamp(0)
time_since_epoch = current_date - epoch_date

rockstar_code = "Rockstar is a big bad monster\nShout Rockstar"
rock_it_bro = RockStar(
    days=time_since_epoch.days, file_name="sample.rock", code=rockstar_code
)
rock_it_bro.make_me_a_rockstar()
