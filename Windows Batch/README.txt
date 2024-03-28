ABOUT:
	This is a simple Windows Batch script that allows the user to change or remove part of the name of all the files in a folder.
	For example, if you have a folder with the following files:
		my-photo1-iphone, my-photo2-iphone, my-photo3-iphone, my-photo4-iphone, my-photo5-iphone, my-photo6-iphone
		
	Then you can run the script, insert "iphone", press enter, then insert "mobile" and all the files will modify their names and you'll have:
		my-photo1-mobile, my-photo2-mobile, my-photo3-mobile, my-photo4-mobile, my-photo5-mobile, my-photo6-mobile
	
	Alternatively, you can give the input "-iphone" and then replace that with simply "" (by pressing Enter and not typing anything) you can remove it entirely and get:
		my-photo1, my-photo2, my-photo3, my-photo4, my-photo5, my-photo6
	
	
PREQUISITES:
	On a Windows computer, run `rename_files.bat` in the folder where you want to change the file names. In some cases Admin permission might be required.
	

NOTE:
	To make tools such as this more useful, I personally reccommend editing the registry (specifically HKEY_CLASSES_ROOT) and adding the script to your shell.
	It involves adding a command such as:	
		cmd.exe /s /k "pushd "%V" && "C:\Users\YourUserName\YourPathToTheScript>\rename_files.bat""

	This will allow you to right click anywhere on your computer and simply select (for example) "Filenames Renamer" and it will run the script in the current folder 
	as if the .bat file was there.
	It's simple to do, but editing the registry is always risky because it's easy to fuck up some system-level stuff, 
	So if you do decide to add it to shell, make sure to first save a backup of the registry and to follow a good guide that explains how to do it step-by-step.