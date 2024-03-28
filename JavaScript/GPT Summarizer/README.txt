PREQUISITES:
	First, make sure you have `GPT Summarizer.zip` file on your computer. There's no need to extract its contents.
	
	1.
		Since this is not a publically published extension, it can only be run in two ways: 
		
			i. In your FireFox (can be any edition of FireFox for this solution) search bar insert and press the following -
					about:debugging#/runtime/this-firefox
			   then click "Load Temporary Add-On..." and select the `GPT Summarizer public.zip` file
			   
			The main downside of this solution is that it's only applicable for the duration of the current FireFox session, 
			meaning that if you closed your FireFox (the whole program, not any individual tab) then the extension won't work anymore
			and you'll have to load it temporarily again. 
			
			Every session of FireFox will require temporarily loading the script again, 
			but if you close your FireFox infrequently then this solution might still be worth it despite the hassle of manually loading it each time.
			
			ii. Using FireFox Developer Edition:
					This version (last tested version is (125.0)) of FireFox allows you to enable local scripts permenantly without having to re-load them each time,
					essentially making the experience same as if it was a normal public extension from the extension store.
					
					Open your FireFox Developer edition, and insert into searchbar:
							about:config
							
					and then press Enter. In the new page use the search function and look for:
							xpinstall.signatures.required
							
					It will be set to "true" by default. Press the toggle button to turn it to "false". 
					This allows you to add unsigned (unofficial/public) extensions to your FireFox.
					
					
					Now in your FireFox browser insert and press:
							about:addons
					click the gear icon and select "Install Add-on from a File...",
					then finally select the `GPT Summarizer public.zip` file, and select "Add" when prompted afterwards
					
					
    2.	
		Make sure you have an API key from one of the AI chatbots providers. 
		This version specifically works with OpenAI's chatGPT, however it can easily be altered and work with other chatbot providers like Claude, Perplexity, etc (this would require also changing the source permission in manifest.json)
		
		In the root folder go to scripts/background.js open it with notepad, 
		then find the line: 
				const API_KEY = "YOUR_API_KEY_HERE" 
		and replace YOUR_API_KEY_HERE with your own private key
		
		You may also toggle the following line of code in order to switch to GPT-4 instead of GPT-3.5 Turbo:
				const MODEL = "gpt-3.5-turbo"
				//const MODEL = "gpt-4-turbo-preview"
				
		Simply remove the `//` from the bottom one and add them to the line above instead
		
		
How TO USE:
	With the extension installed, you may simply click on the blue fox icon whenever you're in a page that you want summarized.
	
	Alternatively, it might be more convinient to use the keyboard shortcut: "Right-Alt + M"
	
	While it's processing the request and waiting for the response from the API provider you will see a blue fox sleeping screen.
	
	Once finished (usually it's a matter of about 10-15 seconds, however the amount and the nature of the page's content might affect performance) a window of the summary will pop-up.
		* You should know that because it's a browser pop-up, clicking on anything that's not the pop-up will close the pop-up.
	Within the pop-up, you'll have two buttons on the bottom: the left one will refresh the request (note that this will spend new tokens of your API), 
	and the second button will copy the content of the entire summary to your clipboard (allowing you to insert it with CTRL+V for convenience)