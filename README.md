# autozoom
A python script to automatically open Zoom and sign in with the meeting id and password as per prescribed schedule.
To use it simply insert the zoom meeting id's and passcodes in the 'timings.xlsx' file and run the script.  
Note that it works only on Linux systems because the bash command "zoom & disown" is used to launch Zoom. For Windows users, replace os.system("zoom & disown") with os.startfile(path).
