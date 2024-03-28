ABOUT:
	When it's used in any folder it "flattens" all sub-folders within it and extracts their content into a single folder called "loot", 
	which holds only the files that were contained within the "flattened" folders.

	USE THIS SCRIPT CAREFULLY. 
	Using it in the wrong place (for example system folders) can potentially cause damage where folder structure is important.
	The script doesn't delete any files, but it deletes all the folders that contain those files and instead moves these files to a new unified location.

	The script has an optional array of restricted paths (for example the desktop), which the user is encouraged to change to the appropriate path.
	It's meant to prevent the user accidentally flattening important folders.
	Simply edit this line:
			RESTRICTED_AREAS = [r"C:\Users\YourUserName\Downloads", r"C:\Users\YourUserName\Desktop\"]

	Insert your own restricted areas for safety. 

	If the script encounters a file collision issue (file with the same name), it will follow the windows copy files
	naming convention and add " ({number of copies})" to the file's name.

	Example:

		Before running the script:

			C:.
			│   flattener.py
			│
			└───fake_directory
				│   file1.pdf
				│   file2.txt
				│
				├───folder1
				│   │   file3.txt
				│   │
				│   └───subfolder1
				│           file4.png
				│           file5.txt
				│
				└───folder2
					└───folder3
							file6.jpg						
						
						
		After running the script in root (./) folder:

			C:.
			│   flattener.py
			│
			└───loot
					file1.pdf
					file2.txt
					file3.txt
					file4.png
					file5.txt
					file6.jpg
					
						
PREQUISITES:
	1. Python locally installed on the computer (with PATH enabled during installation): https://www.python.org/downloads/
	2. Placing the script and running it from a folder containing sub-folders needed to flatten