import datetime

date_start = datetime.datetime(2021, 4, 1)
date_end = datetime.datetime(2021, 5, 15)

table_name = "tbl_mo_log"
partition_name = "tbl_mo_log_p"

while date_start < date_end:
	gen_partition = "ALTER TABLE tbl_mo_log ADD PARTITION "+partition_name+str(date_start.strftime('%Y%m%d'))+" VALUES LESS THAN (TO_DATE(' "+str(date_start+datetime.timedelta(1))+"', 'SYYYY-MM-DD HH24:MI:SS', 'NLS_CALENDAR=GREGORIAN'));"
	print (gen_partition)
	date_start = date_start + datetime.timedelta(1)
print("Done")