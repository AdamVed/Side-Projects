ABOUT:
	A crawler that collects the lowest prices from https://travelist.co.il for a given period and destinations, and then creates graphs for analysis. TKINTER based GUI included.

PREQUISITES:
	1. Python locally installed on the computer (with PATH enabled during installation): https://www.python.org/downloads/
	2. The following Python libraries installed: Tkinter, BeautifulSoup, Selenium, Matplotlib
	3. geckodriver installed on the computer
	4. Running the script in a folder that will contain the newly generated PNG graphs


NOTES:
	i.
		The script only deals with 1-direction at a time. Meaning it doesn't support a "round-trip" option. 
		This is to minimize the final ticket price by choosing the best "dips" in the graphs. 
		Though the script can run again in the opposite direction 
		and can therefore create 2 graphs at once: one for direction A-B and another for direction B-A, with "Delay" dictating the delay between the two.

	ii.
		If "Delay" is set to 0, the script will only run in a single direction

	iii.
		If "Delay" is set to X (X != 0), then if "FROM" = A, "TO" = B, "START_DATE" = X, "END_DATE" = Y, the script will run two times:
			1. DIRECTION: A-B; DATES: X till Y
			2. DIRECTION: B-A; DATES: (X+DELAY) till (Y+DELAY)
	
	iv. All prices are displayed in ILS