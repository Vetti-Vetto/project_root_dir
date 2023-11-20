#the purpose of this script is to download the fasta file
import requests
def download_fasta(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'w') as file:
            file.write(response.text)
    else:
        print(f"Failed to download file: {response.status_code}")

def main():
    url = "https://python.sdv.univ-paris-diderot.fr/data-files/human-proteome.fasta"
    filename = "human-proteome.fasta"
    download_fasta(url, filename)

if __name__ == '__main__':
    main()