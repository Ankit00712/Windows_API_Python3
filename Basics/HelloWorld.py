# Import the required module to handle Windows API Calls
import ctypes

# Grab a handle to User32.dll & kernel32.dll
dll_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")

# Win API Call
# int MessageBoxA(
# HWND hWnd,
# LPCTSTR lpText,
# LPCTSTR lpCaption,
# UINT, uType
# );

# Setting Up The Params
hWnd = None
lpText = 'Hello World'
lpCaption = 'Hello Students!'
uType = 0x00000001

# Calling the Windows API Call
response = dll_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)

# Check For Errors                       #Anything above 0 means something went wrong. 
error = k_handle.GetLastError()          #can check this at each step if wanna debug the program .
if error != 0:                           #https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--0-499-
	print("Error Code: {0}".format(error))
	exit(1)

# Check What The User Clicked
if response == 1:
	print("Clicked OK!")
elif response == 2:
	print("User Exited!")
