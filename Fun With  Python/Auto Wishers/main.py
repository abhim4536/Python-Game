import pandas as pd
import datetime
import smtplib
import os

# os.chdir(r"your programm path")


# Enter Your Authentication Details Below(Enter Your Gmail Id And Password)

GMAIL_ID = ''
GMAIL_PWD = ''


def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()


if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    writeInd = []
    for index, item in df.iterrows():
        bday = item['Birthday'].strftime("%d-%m")
        if today == bday and yearNow not in str(item["Year"]):
            sendEmail(item['Email'], item['Sub'], item['Dialogue'])
            writeInd.append(index)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ',' + str(yearNow)
    df.to_excel('data.xlsx', index=False)

# Please Turn on Less Secure App access option from your Google Account Setting(Importent!)
# Or You Can Visit this site https://myaccount.google.com/lesssecureapps
