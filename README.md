# revjobs
Program to keep track of available rev transcription jobs and send desktop notifications

# Considerations for use:
  - Program will only work with valid login credentials
  - A separate (not included) secrets.py file needs to be created locally with Rev login credentials using import names in rev.py
  - Local user directories are hardcoded and must be updated accordingly in code
  - Users are responsible for any alterations to code -- Rev contractors must use discretion not to save or transmit confidential information or personally identifiable information.
  - Libraries to run: ToastNotifier from win10toast (for desktop notifications), selenium (for web driving) and lxml (html parsing)  
