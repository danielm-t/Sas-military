from num2words import num2words
time_str= input("")
tz=time_str[-2:]
hours, minutes = map(int, time_str[:-2].split(':'))
output=""
if(tz=="PM"):
    hours=hours+12
    output+=num2words(hours)+" "
else:
    if(hours==12):
        hours=0
        output+=num2words(hours)+" "
    else:
        if(hours<10):
            output+=num2words(0)+" "+ num2words(hours)+ " "
        else:
            output+=num2words(hours)+" "
    

if minutes == 0:
    output+="hundred hours"
elif minutes < 10:
    output+="zero "+num2words(minutes)
else:
    output+=num2words(minutes)
print(output.replace("-"," "))


