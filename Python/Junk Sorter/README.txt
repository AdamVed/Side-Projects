ABOUT:
	After placing it in a folder and running it, the script sorts all files within the folder into appropriate subfolders named after the extensions of the files.

	Use case:
		1. put script in the folder that you want to use for organizing files (i.e, junkyard)
		2. each file gets put into a folder named after the extension of the file (or creates it if there's none) (file.pdf -> pdf/file.pdf)

PREQUISITES:
	1. Python locally installed on the computer (with PATH enabled during installation): https://www.python.org/downloads/
	2. Running the script inside a folder that needs organizing
	
	
NOTES: 
	You may want to create a folder that will have a copy of the script that the Windows Scheduler will trigger occassionally. 
	This allows you to essentially create an inbox folder where you can drag and drop various files, and with the scheduler it will sort all the items into appropriate folders - keeping your files organized and easily searchable.
	
	Windows Scheduler -> Create Task -> Triggers (when to run the script) -> Actions:
		in "Program/script" put the directory of python - with cmd run "python where" - if this doesn't work then PATH wasn't properly set up during installation)
		in "Add arguments" put the full path to the actual script: "C:\YourPath\junk_sorter.pyw"
		in "Start in" put the full path to the folder where the script is: "C:\YourPath\"