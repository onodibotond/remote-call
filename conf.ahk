^j::
backup = %clipboard%                                    ; copy the clipboard to a temp variable
Send, {CTRLDOWN}c{CTRLUP}                               ; copy selected text
xyz = %clipboard%                                       ; here is the selected text to xyz
run, "C:/Program Files/remote-call/run.bat" "%xyz%"     ; do what you need here
clipboard = %backup%                                    ; return clipboard to normal
return
