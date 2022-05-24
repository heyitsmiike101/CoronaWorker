# CoronaWorker
This program moves the mouse, presses shift and runs computation to simulate an active machine.
## Use Cases
* Keep virtual machines awake for testing.
* Run malware that looks for user interaction to avoid sandboxes.
* Keep computer awake for various reasons.

## How to Install
1. Install Python 3.10
2. `pip install pyautogui`
3. `pip install pynput=1.6.8`
4. Run `python CoronaWorker.py` 

The first run will creat a config file with the default settings below
``` 
{
  "startTime": "8:00",
  "endTime": "17:00",
  "moveInterval": 45,
  "mouseMovement": false,
  "maxPixelsToMove": 40,
  "keyPress": true,
  "HardwareSleepProcesses": 4
} 
```
* **startTime and endTime**: The start and end time to run the program. To never stop running, put the startTime 5 seconds after the endTime. This needs to be in 24h time  
* **moveInterval**: The amount of seconds between the specifed actions are performed. If the computer still sleeps, consider reducing this number.
* **mouseMovement**: where or not the mouse is moved.
* **maxPixelsToMove**: The program moves the mouse down and to the right and returns to the orginal place. The amount is randomly chosen but this number chooses the maximum.  
* **keyPress**: Whether or not the shift key is pressed.  
* **HardwareSleepProcesses**: How many processes are generated to show computation on the machine. If everything else is on but the computer still sleeps. this number may need to be increases until the computations take about 5 seconds to complete.

