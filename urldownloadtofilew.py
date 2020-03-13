from ctypes import *

URL = 'https://bit.ly/2VNATVz'
OUTPUT = 'outfile.txt'

def test301():
    """
    ref: https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775123(v%3Dvs.85)

    URLDownloadToFile function
    URLDownloadToFileW (Unicode) and URLDownloadToFileA (ANSI)

    HRESULT URLDownloadToFile(
                 LPUNKNOWN            pCaller,
                 LPCTSTR              szURL,
                 LPCTSTR              szFileName,
      _Reserved_ DWORD                dwReserved,
                 LPBINDSTATUSCALLBACK lpfnCB
     ); 
    """

    urlmon = WinDLL('urlmon')
    urlmon.URLDownloadToFileW(None, URL, OUTPUT, 0, None)

def main():
    try:
        test301()

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
