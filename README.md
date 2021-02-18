# Q-DAS File Reader

This is a reader package to read Q-DAS ASCII files via Python. The package comes with data structures to cover the tranfer file format header elements such as parts (Teiledaten) and attributes (Merkmalsdaten). As the Q-DAS ASCII files might already come with measurements, the reader function reads these measurements (Werteteil) as well and stores them as part of the attributes described in the transfer file.

The package `qdasreader` is based on the official 
[Q-DAS ASCII](https://www.q-das.com/fileadmin/mediamanager/Datenformat_Dokumente/Q-DAS_ASCII-Transfer-Format_GER_V12_dc.pdf) tranfer format which is available from Q-DAS GmbH.
