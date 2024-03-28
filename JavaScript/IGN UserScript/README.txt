ABOUT:
	This is a "user script" written in JavaScript. User scripts allow you to locally modify your browsing experience, either through UI or/and UX enhancements.
	To run a user script you need an extension that manages scripts like this. One of them is Violentmonkey, a popular Open-Source extension with a big following of users,
	who contribute by publically sharing their custom-made user scripts. 

	This user script is specifically made for the gaming journalism website:
			ign.com
			
	
	What does it do?
		i. 	IGN has custom advertisements that they use on their website. Normal ad-blockers cannot deal with them since they're technically not spam (at least not in the classic sense).
			They're advertisements disguised as articles, which can be annoying and misleading. 
			
			In the script's code, the user may add to the pre-made list of keywords more unwanted terms. Simply add to `badOther` list new keywords you'd want blocked.
			For example:
				  const badOther = [
					"Amiibo",
					"VR",
					"Halloween Sale"
				  ];
				  
			will block any articles that contain the keywords "Amiibo", "VR" and "Halloween Sale" in their names.
			
		ii. On the main page of ign, the user is exposed to different types of articles. Some of them are reviews (of TV series, movies, games, etc).
			To save time when scrolling through articles, the script detects which articles are "reviews" (via keywords in their URLs),
			and then it adds a new UI element to the user - a red area that says "IGN SCORE: <SCORE>" and shows the final score that the review gave. 
			Then if the user hovers with their mouse over the red text, it will display the "final words" from the article's review that precede the actual score.
			This allows the user to quickly check the review score and get a short summary - then the user can decide if they want to actually open the article and read it.
		
-----------------------------	

PREQUISITES:
	1.
		Make sure you have Violentmonkey browser extension installed. 
		Go to the extensions store of your browser and search for its name and install it.
	2.
		Once installed, click on Violentmonkey's extension icon, then open the dashboard (gear icon). 
		In the dashboard, click on the + icon, select New. Then remove the boilerplate code, insert the content of `IGN UserScript.js`,
		and then select Save. Your userscript should now be installed.

-----------------------------		
	
NOTES:
	* The script is based on the English versions of IGN, so us.ign.com, uk.ign.com, etc should work the same.
	* Note that this script was written with a PC screen in mind, so using this on mobile could have unpredictable consequences
	* Make sure to check the script's list of "badGames" and remove/add whatever is relevant to you
	* If working, your Violentmonkey extension icon should be colored (as opposed to greyed-out) when you visit us.ign.com
	