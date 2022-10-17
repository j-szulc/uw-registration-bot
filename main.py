from datetime import datetime, timedelta
import subprocess as sp
from time import sleep
import json
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo
import dateutil.parser


def strike(**kwargs):
    return sp.Popen(cmd,shell=True,**kwargs)


delta = timedelta(seconds=1)
tz=zoneinfo.ZoneInfo("Europe/Warsaw")

# from Chrome DevTools
cmd = "curl https://api.ipify.org?format=json | jq"

if __name__ == "__main__":

    with strike(stdout=sp.PIPE) as child:
        output = child.stdout.read()
        print(output)
        obj = json.loads(output)
        localDate = datetime.now(tz=tz)
        remoteDateStr = obj["params"]["now"]
        remoteDate = dateutil.parser.parse(remoteDateStr).replace(tzinfo=tz)
        remoteGoalStr = obj["params"]["openDate"]
        remoteGoal = dateutil.parser.parse(remoteGoalStr).replace(tzinfo=tz)
        offset = remoteDate-localDate

    def getRemoteDate():
        return datetime.now(tz=tz)+offset

    while True:
        realDelta = remoteGoal - getRemoteDate()
        print(f"Strike in: {realDelta}")
        if realDelta > delta:
            sleep(delta.total_seconds())
        else:
            sleep(realDelta.total_seconds())
            break

    strike()
    sleep(0.1)
    strike()
    sleep(0.1)
    strike()
    sleep(0.2)
    strike()
    sleep(0.3)
    strike()
    sleep(1)
    strike()
