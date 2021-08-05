import requests
import smtplib
import datetime

d=datetime.datetime.today().strftime('%d-%m-%Y')

# 18 or 45
age=18    

# No of people                                                  
tot=3 

# Type of vaccination : COVISHIELD, COVAXIN ...                                                
vacc="COVISHIELD"

# Pincodes list 
pincodes=['560056','560059','560060', '560074', '560098']

FromEmail=""    # From Email ID inside double quote
FromEmailPass=""         # From Email ID password inside double quote
ToEmail=""  # To Email ID inside double quote


message = """From: {FromEmail}
To: {ToEmail}
Subject: Vaccine Available

"""
c=0
for k in range(len(pincodes)):
  response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+str(pincodes[k])+"&date="+str(d))
  for i in range(len(response.json()["centers"])):
    for j in range(len(response.json()["centers"][i-1]["sessions"])):
      if (response.json()["centers"][i-1]["sessions"][j-1]["min_age_limit"]==age and response.json()["centers"][i-1]["sessions"][j-1]["vaccine"]==vacc and response.json()["centers"][i-1]["sessions"][j-1]["available_capacity"] >=tot):
        print(response.json()["centers"][i-1]["name"])
        print(response.json()["centers"][i-1]["sessions"][j-1]["session_id"])
        print(response.json()["centers"][i-1]["sessions"][j-1]["available_capacity"])
        print(response.json()["centers"][i-1]["sessions"][j-1]["min_age_limit"])
        print(response.json()["centers"][i-1]["sessions"][j-1]["vaccine"])
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(FromEmail, FromEmailPass)
        str1=response.json()["centers"][i-1]["name"]
        str2=response.json()["centers"][i-1]["sessions"][j-1]["available_capacity"]
        message= (message+ "\n" +	"Center name : " + str1 + "\n"+"Available :" + str(str2) + "\n")
        c=1

if (c==1):
  s.sendmail(FromEmail, ToEmail, message)
  print('Email sent to '+ToEmail+' From '+FromEmail)
  s.quit()
