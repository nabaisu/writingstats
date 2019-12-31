on run argv
	set defaultTime to 15
	
	try
		set myTime to item 1 of argv as number
	on error
		set myTime to defaultTime
	end try
	
	
	-- Quit Keychain Scripting if it's running, since opening this script may have implicitly launched it.	
	try
		tell application "System Events"
			set foundApp to first process whose name is "Keychain Scripting"
			set pid to id of foundApp -- this will exit the try block if the process isn't running
			quit foundApp -- we get here if the process is found
		end tell
	end try
	
	-- get Finder to launch Keychain Scripting
	tell application "Finder"
		open application file ((startup disk as string) & "Applications:Usable Keychain Scripting") as alias
	end tell
	
	tell application "Usable Keychain Scripting"
		tell current keychain
			set myPass to (password of first generic item whose name contains "SelfControl")
			
			-- eliminate invisible characters, or "gremlins," from password
			set x to quoted form of myPass
			set myPass to do shell script "echo " & x & " | perl -pe 's/[^[:print:]]//g'"
		end tell
	end tell
	
	tell application "SelfControl" to activate
	
	tell application "System Events"
		tell process "SelfControl"
			tell slider of window "SelfControl" to set value to myTime
			click button "Iniciar" of window "SelfControl"
		end tell
		
		tell process "SecurityAgent"
			with timeout of 15 seconds
				repeat
					set tryAgain to false
					try
						set value of text field 2 of window 1 to myPass
					on error
						delay 1
						set tryAgain to true
					end try
					if not tryAgain then exit repeat
				end repeat
				click button 2 of window 1
			end timeout
		end tell
	end tell
end run
