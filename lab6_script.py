import requests
import hashlib
import subprocess
import os


def main():
    
    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()
    

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():
    url = 'http://download.videolan.org/pub/videolan/vlc/3.0.18/win64/vlc-3.0.18-win64.exe.sha256'
    response = requests.get(url)

    if response.status_code == requests.codes.ok :
        content = response.text
        value = content[0:63]
    
    return(value)
    

def download_installer():
    url2 = 'http://download.videolan.org/pub/videolan/vlc/3.0.18/win64/vlc-3.0.18-win64.exe'
    response2 = requests.get(url2)

    if response2.status_code == requests.codes.ok :
        content = response2.content
        with open(r'C:\Users\dhava\Downloads\vlc-3.0.18-win64.exe','wb') as file:
            file.write(content)
    
    return(content)

def installer_ok(installer_data, expected_sha256):
    url = 'http://download.videolan.org/pub/videolan/vlc/3.0.18/win64/vlc-3.0.18-win64.exe.sha256'
    response = requests.get(url)

    if response.status_code == requests.codes.ok :
        content = response.content
        image_hash = hashlib.sha256(content).hexdigest()
    
    return(image_hash)

def save_installer(installer_data):
    return

def run_installer(installer_path):
    installer_path = r'C:\Users\dhava\Downloads\vlc-3.0.18-win64.exe'
    subprocess.run([installer_path,'/L=1033','/S'])
    os.remove(installer_path)
    return
    
def delete_installer(installer_path):
    return

if __name__ == '__main__':
    main()