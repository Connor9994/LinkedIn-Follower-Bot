from random import *
import time
import datetime

import nodriver as uc
from nodriver import *

browserPath='C:\\Users\\Administrator\\Desktop\\LinkedIn Follower Bot\\Chrome\\chrome.exe'
profilePath='C:\\Users\\Administrator\\Desktop\\LinkedIn Follower Bot\\Users\\LinkedIn\\'
LoggedIn = 1

async def main():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    total_accounts = 0
    Skip = 0
    with open("AccountLog.txt", 'r') as log_file:
        for line in log_file:
            # Split the line to extract accounts and date
            parts = line.strip().split(" on ")
            if len(parts) == 2:
                accounts_part = parts[0]
                date_part = parts[1]
                
                # Extract the number of accounts and the date
                accounts_count = int(accounts_part.split(": ")[1])  # Extract number of accounts
                log_date = datetime.datetime.strptime(date_part, '%Y-%m-%d')

                # Check if the log date is within the last 7 days
                if log_date >= datetime.datetime.now()-datetime.timedelta(days=7):
                    total_accounts += accounts_count
    
    # If More than 100 Accounts This Week, Skip
    if (total_accounts > 100):
        Skip = 1

     # If Already Ran today, Skip
    with open("AccountLog.txt", 'r') as log_file:
        for line in log_file:
            if current_date in line:
                Skip = 1
                print("Current date: " + current_date + " is already in the log file.")
                print("Total Accounts This Week: " + str(total_accounts))
    
    if (not Skip):
        x = 0
        y = 0
        try:
            driver = await uc.start(
            headless = False,
            browser_executable_path=browserPath,
            user_data_dir=profilePath,
            browser_args=[
            f"--window-size={randint(500, 1920)},{randint(500, 1080)}",
            ]
            )

            tab = await driver.get("https://www.linkedin.com/mynetwork/grow/")
            if (LoggedIn):
                await driver.wait(time=random()) # Wait
                bottomFrame = await tab.select("#humanThirdPartyIframe")
                while y < 10:
                    await bottomFrame.scroll_into_view()
                    time.sleep(1)
                    y += 1

                connectBars = await tab.find_all("to connect",timeout=25)
                for bar in connectBars:
                    if (x >= 25):
                        break
                    else:
                        await bar.scroll_into_view()
                        #await bar.click()
                        time.sleep(2+5*random())
                        x += 1
                    
                # Log this message into a text file
                with open('AccountLog.txt', 'a') as log_file:  # Append mode
                    log_file.write(f"Accounts ran: {x} on {current_date}\n")

                await tab.close()
            else:
                input("Press Enter to continue...")
                await tab.close()
        except Exception as e:
            print(e)
            # Log this message into a text file (Error encountered, still record followed Accounts)
            if (x>0):
                with open('AccountLog.txt', 'a') as log_file:  # Append mode
                    log_file.write(f"Accounts ran: {x} on {current_date}\n")
            await tab.close()

if __name__ == "__main__":
    uc.loop().run_until_complete(main())