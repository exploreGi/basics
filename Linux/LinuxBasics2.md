### Hard link Vs Soft link
- A hard link is a duplicate of the original file. 
The difference between a hard link and a soft link is that deleting the source file has no effect on a hard link, however it makes a soft link unusable.
- Syntax of Hard Link is “ln” command. On the other hand, the command for a soft link is “ln -s”
- Hard links refer to the same inode, hence they cannot cross filesystems. Soft links are simply references to a file, whether on the same disc or different disc.
- Hard links are comparatively faster.	Soft links are comparatively slower.
- Files that are hard linked take the same inode number.	Files that are soft linked take a different inode number.
- Hard links are not allowed for directories. (Only a superuser* can do it)	Soft links can be used for linking directories.
- It cannot be used across file systems.	It can be used across file systems.
- Data present in the original file will still be available in the hard links.	Soft links only point to the file name, it does not retain data of the file.
-  If the original file is removed, the link will still work as it accesses the data the original was having access to.
If the original file is removed, the link will not work as it doesn’t access the original file’s data.

### Crontab,Crond,Cron job
- Crontab stands for Cron Table. This is a Linux system file that creates a table-like structure
where fields are separated by white space. Users can populate the table by assigning values to each field (asterisk).
- Each complete row can be thought of as an individual job, often referred to as “cron jobs”.
- The Cron Daemon :A system process called a Daemon runs in the background of our Linux machine.
There are Daemons for many different services. These are commonly named by suffixing a ‘d’ to a service name.
No action is required on our part to execute that daemon, but if you don’t think the command is working properly, you can use: 
ps aux | grep crond

`* * * * * script or command`\
Minute	Hour	Date 	Month	DayName\
	0-59	0 -23	1-31	 1-12	 0-6\
DayNames 0-6 begin with Sunday.

### grep : searches for a particular pattern in a file or standard input
grep -o "s" <<<"mississipi"  | wc -l

### wc -> word count
no.of lines, no.of words, no.of characters(including new line /n) and file name
