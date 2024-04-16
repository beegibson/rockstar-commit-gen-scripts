from rockstar import RockStar

from datetime import datetime

current_date = datetime.now()
epoch_date = datetime.fromtimestamp(0)
time_since_epoch = current_date - epoch_date


# https://esolangs.org/wiki/Enterprise%E2%84%A2
enterprise_code = """ /©
   This code is property of Enterprise™.
 ©/
 
 import disruptive library com.disruptive.IO.write.delegator.dlIOWriteDelegator;;;
 
 /NDA
   This document is regulated by NDA 758-1.
 NDA/
 
 final disruptive class fdcFizzBuzzDelegator {
   final immutable void main () {
     var Money x = 0;;;
     var String out = "";;;
 
     while (x < 1k) {
       if(x % 5 == 0 && x % 3 == 0) {
         write("Fizz Buzz");;;
       } else {
         if(x % 3 == 0) {
           write("Fizz");;;
         } else {
           if(x % 5 == 0) {
             write("Buzz");;;
           } else {
             write(x);;;
           }
         }
       }
 
       mutate x++;;;
     }
   }
 
   final unnecessary Money appleValuation () {
     /?
       This code is so useful.
     ?/
 
     unnecessary var Money applVltn = 2T;;;
 
     return applVltn;
   }
 }
 """

rock_it_bro = RockStar(
    days=time_since_epoch.days, file_name="synergy.e", code=enterprise_code
)
rock_it_bro.make_me_a_rockstar()
