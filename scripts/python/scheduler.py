    #! /usr/bin/python -tt
    import datetime
    import webbrowser
    import time
    def main():
        print ("Welcome Harvey !!!! :) \nThe Scheduler has Started and is ACTIVE"
        while(1):
            tempTime = str(datetime.datetime.now().time())
            listTime = tempTime.split(':',1)
            hour = int(listTime[0]) + 1
            hour = str(hour)
    #  extracting minutes out of the time
            tempMinute = str(listTime[1])
            minute = tempMinute[0:2]
    #  extracting seconds out of the time
            tempSecList = tempMinute.split(':')
            tempSecString = str(tempSecList[1])
            sec = tempSecString[0:2]
            if( minute == '24' and sec == '01'):
                if hour == '11':
                    with open('C:\Users\harvey\Desktop\Prod.txt','r+') as f:
                        f.write("Please send in the 11pm - 12am CST report")
                    webbrowser.open_new_tab('C:\Users\harvey\Desktop\Prod.txt')
                    time.sleep(1)
                elif hour == '12':
                    with open('C:\Users\harvey\Desktop\Prod.txt','r+') as f:
                        f.write("Please update the Client about the latest Web Server Report\n")
                    webbrowser.open('C:\Users\harvey\Desktop\Prod.txt')
                    time.sleep(1)
                elif hour == '13':
                    with open('C:\Users\harvey\Desktop\Prod.txt','r+') as f:
                        f.write("Please send in the 1am - 2am CST report and also update the TGT daily Stats report. The purge process starts at 1330hrs IST\n")
                    webbrowser.open_new_tab('C:\Users\harvey\Desktop\Prod.txt')
                    time.sleep(1)
                elif hour == '14':
                    with open('C:\Users\harvey\Desktop\Prod.txt','r+') as f:
                        f.write("Login via VPN and check the logs for any errors")
                    webbrowser.open_new_tab('C:\Users\harvey\Desktop\Prod.txt')
                    time.sleep(1)
                elif hour == '15':
                    with open('C:\Users\harvey\Desktop\Prod.txt','r+') as f:
                        f.write("Run the Test for testing Load")
                    webbrowser.open_new_tab('C:\Users\harvey\Desktop\Prod.txt')
                    time.sleep(1)
                elif hour == '16':
                    with open('C:\Users\harvey\Desktop\Prod.txt','r+') as f:
                        f.write("Configure DNS if not updated")
                    webbrowser.open_new_tab('C:\Users\harvey\Desktop\Prod.txt')
                    time.sleep(1)
                elif hour == '17':
                    with open('C:\Users\harvey\Desktop\Prod.txt','r+') as f:
                        f.write("Please send in the 5am - 6am CST report")
                    webbrowser.open_new_tab('C:\Users\harvey\Desktop\Prod.txt')
                    time.sleep(1)
                elif hour == '19':
                    with open('C:\Users\harvey\Desktop\Prod.txt','r+') as f:
                        f.write("Please send in the 7am - 8am CST report or ask Mr. X to take over the Report Work")
                    webbrowser.open_new_tab('C:\Users\harvey\Desktop\Prod.txt')
                    time.sleep(1)
                elif hour == '10':
                    with open('C:\Users\harvey\Desktop\Prod.txt','r+') as f:
                        f.write("Check Firewall settings")
                    webbrowser.open_new_tab('C:\Users\harvey\Desktop\Prod.txt')
                    time.sleep(1)
        print "My Scheduler stopped and is IN-ACTIVE"
    if __name__ == '__main__':
        main()
