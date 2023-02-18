from datetime import datetime
from num2words import num2words
string= input("")
time= datetime.strptime(string, "%I:%M%p")
time=time.strftime("%H:%M")
hours,minutes=[int(x)for x in time.split(":")]
output=""
if(hours<10):
    output="zero "+num2words(hours)
if (minutes==0):
    output+=" hundred hours"
elif (minutes<10):
    output+=" zero "+num2words(minutes)
print(output)



