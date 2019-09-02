import time
import datetime
import sys
import optparse
import os


# arguements
parser = optparse.OptionParser()
parser.add_option("-t", "--time",
                  dest="TARGET_TIME", default='00:00:00',
                  help="Set the time to run the update or command (24 Hour format) Default is set to 12 AM . Ex; -t 00:01:00")
parser.add_option("-c", "--command",
                  dest="COMMAND", help="Used to set the command (Use quotations if command is multilined). Ex; -t 'apt-get upgrade'")

(options, arguements) = parser.parse_args()


# SET UPDATE FUNCTION , GETS TIME AND COMMAND AND EXECUTES WHEN TIME IS MET
def set_update(time_, command):
    while True:
        NOWTIME = datetime.datetime.now()
        DATE, FULL_TIME = str(NOWTIME).split(' ')
        REAL_TIME = FULL_TIME.split('.')
        # CHECK IF CURRENT TIME IS THE TARGET TIME
        if REAL_TIME[0] != time_:
            sys.stdout.write(f" \rCURRENT TIME : {REAL_TIME[0]}")
            sys.stdout.flush()
            time.sleep(1)
        else:
            print(
                "\n\n_____________________________________________________________\n")
            break

    try:
        # EXECUTES THE COMMAND
        output = os.system(command)
        if output == 0:
            print(f'\nCOMMAND EXECUTED SUCCESSFULLY')
    except Exception as e:
        print(f'\nCOMMAND EXECUTION FAILED\nERROR: {e}')
        pass


# MAIN FUNCTION, THIS IS WHERE ALL THE PARAMS ARE CHECKED AND PASSED FOR THE set_update() FUNC
def main():
    try:
        # GETS THE COMMAND AND TIME ENTERED AS PARAMETERS
        COMMAND = options.COMMAND
        time_S = options.TARGET_TIME.split(':')

        if len(time_S) == 1:
            TARGET_TIME = f'{time_S[0]}:00:00'
        elif len(time_S) == 2:
            TARGET_TIME = f'{time_S[0]}:{time_S[1]}:00'
        else:
            TARGET_TIME = options.TARGET_TIME

        print(f"\nCommand : {COMMAND}\nTime : {TARGET_TIME}\n")
        set_update(TARGET_TIME, COMMAND)
    except TypeError:
        print("ERROR : No parameters found")
        pass
    except KeyboardInterrupt:
        print("\n[-] Program stopped ")
        pass


if __name__ == "__main__":
    main()
