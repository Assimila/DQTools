this is a rudimentary tool which for each combination of 
product x subproduct x tile
found in a config file passed as argument using -c (for instance all_combos.txt), checks that
for each month from a configurable start year to the present day, 
the number of time entries returned by DQTools query for the combinaion and month is the
same as the number of time bands in the file in /datacube

the start year, combo file, etc are configurable. 
Must also pass in the system config file with -f

for each such combination, print a line to stdout indicating either:
	'OK' - number of records match.
	or otherwise if not.

example output from .34:
===============================================================
OK:2024-1 db:26 - 26 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-01.tif
OK:2024-2 db:29 - 29 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-02.tif
OK:2024-3 db:30 - 30 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-03.tif
OK:2024-4 db:30 - 30 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-04.tif
OK:2024-5 db:31 - 31 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-05.tif
OK:2024-6 db:18 - 18 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-06.tif
OK:2024-7 db:16 - 16 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-07.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-8 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-08.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-9 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-09.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-10 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-10.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-11 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-11.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-12 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-12.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2025-1 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2025-01.tif
Can't find chirps_africa in ../../../datacube/src/datacube/dq_database/dq_DB_conf/tiles.yaml
Can't find chirps_colombia in ../../../datacube/src/datacube/dq_database/dq_DB_conf/tiles.yaml
     ecmwf_operational_archive                             skt                ecmwf_0p1_africa
===============================================================
OK:2024-1 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-01.tif
OK:2024-2 db:696 - 696 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-02.tif
OK:2024-3 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-03.tif
OK:2024-4 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-04.tif
OK:2024-5 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-05.tif
OK:2024-6 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-06.tif
OK:2024-7 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-07.tif
OK:2024-8 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-08.tif
OK:2024-9 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-09.tif
OK:2024-10 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-10.tif
OK:2024-11 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-11.tif
OK:2024-12 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-12.tif
OK:2025-1 db:465 - 465 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2025-01.tif
     ecmwf_operational_archive                             t2m                ecmwf_0p1_africa
===============================================================
===============================================================
OK:2024-1 db:26 - 26 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-01.tif
OK:2024-2 db:29 - 29 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-02.tif
OK:2024-3 db:30 - 30 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-03.tif
OK:2024-4 db:30 - 30 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-04.tif
OK:2024-5 db:31 - 31 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-05.tif
OK:2024-6 db:18 - 18 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-06.tif
OK:2024-7 db:16 - 16 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-07.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-8 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-08.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-9 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-09.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-10 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-10.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-11 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-11.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-12 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-12.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2025-1 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2025-01.tif
Can't find chirps_africa in ../../../datacube/src/datacube/dq_database/dq_DB_conf/tiles.yaml
Can't find chirps_colombia in ../../../datacube/src/datacube/dq_database/dq_DB_conf/tiles.yaml
     ecmwf_operational_archive                             skt                ecmwf_0p1_africa
===============================================================
OK:2024-1 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-01.tif
OK:2024-2 db:696 - 696 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-02.tif
OK:2024-3 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-03.tif
OK:2024-4 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-04.tif
OK:2024-5 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-05.tif
OK:2024-6 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-06.tif
OK:2024-7 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-07.tif
OK:2024-8 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-08.tif
OK:2024-9 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-09.tif
OK:2024-10 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-10.tif
OK:2024-11 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-11.tif
OK:2024-12 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-12.tif
OK:2025-1 db:465 - 465 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2025-01.tif
     ecmwf_operational_archive                             t2m                ecmwf_0p1_africa
===============================================================
===============================================================
OK:2024-1 db:26 - 26 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-01.tif
OK:2024-2 db:29 - 29 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-02.tif
OK:2024-3 db:30 - 30 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-03.tif
OK:2024-4 db:30 - 30 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-04.tif
OK:2024-5 db:31 - 31 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-05.tif
OK:2024-6 db:18 - 18 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-06.tif
OK:2024-7 db:16 - 16 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-07.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-8 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-08.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-9 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-09.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-10 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-10.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-11 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-11.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-12 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-12.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2025-1 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2025-01.tif
Can't find chirps_africa in ../../../datacube/src/datacube/dq_database/dq_DB_conf/tiles.yaml
Can't find chirps_colombia in ../../../datacube/src/datacube/dq_database/dq_DB_conf/tiles.yaml
     ecmwf_operational_archive                             skt                ecmwf_0p1_africa
===============================================================
OK:2024-1 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-01.tif
OK:2024-2 db:696 - 696 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-02.tif
OK:2024-3 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-03.tif
OK:2024-4 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-04.tif
OK:2024-5 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-05.tif
OK:2024-6 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-06.tif
OK:2024-7 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-07.tif
OK:2024-8 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-08.tif
OK:2024-9 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-09.tif
OK:2024-10 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-10.tif
OK:2024-11 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-11.tif
OK:2024-12 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-12.tif
OK:2025-1 db:465 - 465 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2025-01.tif
     ecmwf_operational_archive                             t2m                ecmwf_0p1_africa
===============================================================
===============================================================
OK:2024-1 db:26 - 26 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-01.tif
OK:2024-2 db:29 - 29 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-02.tif
OK:2024-3 db:30 - 30 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-03.tif
OK:2024-4 db:30 - 30 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-04.tif
OK:2024-5 db:31 - 31 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-05.tif
OK:2024-6 db:18 - 18 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-06.tif
OK:2024-7 db:16 - 16 in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-07.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-8 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-08.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-9 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-09.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-10 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-10.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-11 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-11.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2024-12 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2024-12.tif
('Failed to retrieve Dataset sub-product data,', 'please see logfile for details.')
OK:2025-1 db:None - None in //datacube/arc2/rfe/ecmwf_0p1_africa/arc2_rfe_ecmwf_0p1_africa_2025-01.tif
Can't find chirps_africa in ../../../datacube/src/datacube/dq_database/dq_DB_conf/tiles.yaml
Can't find chirps_colombia in ../../../datacube/src/datacube/dq_database/dq_DB_conf/tiles.yaml
     ecmwf_operational_archive                             skt                ecmwf_0p1_africa
===============================================================
OK:2024-1 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-01.tif
OK:2024-2 db:696 - 696 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-02.tif
OK:2024-3 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-03.tif
OK:2024-4 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-04.tif
OK:2024-5 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-05.tif
OK:2024-6 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-06.tif
OK:2024-7 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-07.tif
OK:2024-8 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-08.tif
OK:2024-9 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-09.tif
OK:2024-10 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-10.tif
OK:2024-11 db:720 - 720 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-11.tif
OK:2024-12 db:744 - 744 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2024-12.tif
OK:2025-1 db:465 - 465 in //datacube/ecmwf_operational_archive/skt/ecmwf_0p1_africa/ecmwf_operational_archive_skt_ecmwf_0p1_africa_2025-01.tif
     ecmwf_operational_archive                             t2m                ecmwf_0p1_africa
===============================================================
...

Note that arc2 downloader stopped working in July 2024 (Issue #212)
	
Caveats:
	it would have probably been better to retrieve product, subproduct and tile info
	from the datacube itself, but this is simple, easily controllable and works.
