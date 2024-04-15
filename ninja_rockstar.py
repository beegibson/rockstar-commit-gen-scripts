from rockstar import RockStar

from datetime import datetime

current_date = datetime.now()
epoch_date = datetime.fromtimestamp(0)
time_since_epoch = current_date - epoch_date

# https://github.com/gravataLonga/ninja
ninja_code = """
var a = 1;
a = a + 1;  
puts(a); 
"""
rock_it_bro = RockStar(
    days=time_since_epoch.days, file_name="sample.njs", code=ninja_code
)
rock_it_bro.make_me_a_rockstar()
