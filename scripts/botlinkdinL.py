#!/usr/bin/env python3
import datetime
import os
import sys
import time
from random import *
from random import randint, random

import nodriver as uc
from nodriver import *

if len(sys.argv) > 3:
    browserPath = sys.argv[1]
    profilePath = sys.argv[2]
    LoggedIn = int(sys.argv[3])
else:
    browserPath = "/usr/bin/chromium"
    profilePath = "/home/capi/Documents/botdata/"
    LoggedIn = 1


async def main():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    total_accounts = 0
    Skip = 0

    if not os.path.exists("AccountLog.txt"):
        open("AccountLog.txt", "w").close()

    with open("AccountLog.txt", "r") as log_file:
        for line in log_file:
            if " on " not in line:
                continue
            parts = line.strip().split(" on ")
            if len(parts) < 2:
                continue
            accounts_part = parts[0]
            date_part = parts[1]

            try:
                accounts_count = int(accounts_part.split(": ")[1])
            except (IndexError, ValueError):
                continue

            try:
                log_date = datetime.datetime.strptime(date_part, "%Y-%m-%d")
            except ValueError:
                continue

            if log_date >= datetime.datetime.now() - datetime.timedelta(days=7):
                total_accounts += accounts_count

    if total_accounts >= 100:
        Skip = 1
        print("Total de cuentas esta semana: " + str(total_accounts))

    with open("AccountLog.txt", "r") as log_file:
        for line in log_file:
            if current_date in line:
                Skip = 1
                print(
                    "La fecha actual ("
                    + current_date
                    + ") ya está en el archivo de log."
                )
                print("Total de cuentas esta semana: " + str(total_accounts))

    if not Skip:
        x = 0
        y = 0
        try:
            driver = await uc.start(
                headless=False,
                browser_executable_path=browserPath,
                user_data_dir=profilePath,
                browser_args=[
                    f"--window-size={randint(500, 1920)},{randint(500, 1080)}",
                ],
            )

            tab = await driver.get("https://www.linkedin.com/mynetwork/grow/")
            if LoggedIn:
                await driver.wait(time=random())  # Pausa aleatoria
                bottomFrame = await tab.find("People you may know", timeout=25)
                while y < 10:
                    await bottomFrame.scroll_into_view()
                    time.sleep(1)
                    y += 1

                connectBars = await tab.find_all("to connect", timeout=25)
                for bar in connectBars:
                    if x >= 25:
                        break
                    else:
                        await bar.scroll_into_view()
                        await bar.click()
                        time.sleep(2 + 5 * random())
                        x += 1

                with open("AccountLog.txt", "a") as log_file:
                    log_file.write(f"Accounts ran: {x} on {current_date}\n")

                await tab.close()
            else:
                input("Presiona Enter para continuar...")
                await tab.close()
        except Exception as e:
            print(e)
            if x > 0:
                with open("AccountLog.txt", "a") as log_file:
                    log_file.write(f"Accounts ran: {x} on {current_date}\n")
            await tab.close()


if __name__ == "__main__":
    uc.loop().run_until_complete(main())
