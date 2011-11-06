-- set t to "awesome"

on readFile(unixPath)
	return (do shell script "cat '" & unixPath & "'")
end readFile


on run argv
	set t to readFile("/Users/skrum/derp.txt")

	tell application "Stickies" to activate
	tell application "System Events"
		tell process "Stickies"
			tell window 1
				delay 0.5
				keystroke "n" using command down
				tell scroll area 1
					set value of text area 1 to item 1 of argv
					delay 0.5
				end tell
			end tell
		end tell
	end tell
end run
