import shutil
import time
i=0
threshold_time=1800
while True:
    i=i+1
    print("Starting Backup copy #",i)
    path_original_brb=r"RESULTS\RESULTS_2nd.csv"
    path_backup_brb=r"BACKUP\RESULTS_2nd_"+(str(i))+"_.csv"
    path_original_usa=r"RESULTS\RESULTS_usa.csv"
    path_backup_usa=r"BACKUP\RESULTS_usa_"+(str(i))+"_.csv"
    shutil.copyfile(path_original_brb,path_backup_brb)
    shutil.copyfile(path_original_usa,path_backup_usa)
    print("Backup copy #",i)
    print("Done")
    time.sleep(threshold_time)
