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