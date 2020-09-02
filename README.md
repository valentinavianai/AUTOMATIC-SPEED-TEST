# AUTOMATIC SPEED TEST
 Automatic speed meter powered by speed-test-cli.
 
## Main.py
Main program that test your internet connection continously using speed test servers.
The program output is a csv file allocated in the RESULTS folder.
The output parammeters saved on the csv file are:
### Date: 
DD/MM/YYYY : HH:MM:SS
### Sample:
sample number
### Download:
Download speed given on b/s
### Upload:
Upload speed on b/s
### Ping:
Ping time to the test server given on ms
### Server:
Host direction

## Redundancy.py
This is and optional python script to secure the data continously by copying the results files 
on to the backup folder.

## Results
Where the results csv is allocated

## Backup
Where the backup csv´s are allocated

## Server_List
Html file with some speed test servers

### How to select the server
In this early version in order to change the test server you have to edit the host server ID on the Main.py script.
#### <server url= ...  id="15019" .../>

## Dependencies 
This automatic test uses the speed-test cli API by sivel for carrying out the test´s and Pandas for data storage.
### links to install the dependencies
#### https://github.com/sivel/speedtest-cli
#### https://pandas.pydata.org/

## Additional References
#### https://www.speedtest.net/es/apps/cli
