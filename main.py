#Written by Ramiro Mendez

#prints menu choices for user to select from
def get_menu_choice():
    print()
    print('Artists and Songs')
    print('---------------------------')
    print('1. Display all Artists and Songs')
    print('2. Display # of Artists in dictionary')
    print('3. Display Songs of Artists only')
    print('4. Display Artists names only')
    print('5. Look up a Song by name')
    print('6. Locate Artist in dictionary')
    print('7. Add Artist and song')
    print('8. Change Artist song')
    print('9. remove Artist and Song')
    print('10. clear dictionary')
    print('11. Exit menu')
    print()

    choice = int(input('Enter your choice: '))

    while choice < 0 or choice > 11:
        choice = int(input('Enter a valid choice: '))

    return choice

#displays artist names and songs in sorted order
def displayNamesSongs(artistSongDictionary):
    print("\nList of Artists and Songs in Dictionary:")
    print("-----------------------------------------------------------")
    for artist, song in artistSongDictionary.items():
        print(artist + ": " + song)

#prints number of artists/songs in the dictionary
def numberSongs(artistSongDictionary):
    numSongs = len(artistSongDictionary)
    print('There are', numSongs, 'Songs')

#prints the artists names in sorted order
def nameList(artistSongDictionary):
    sortedartists= sorted(artistSongDictionary.keys(), key=lambda x:x.lower())
    print("\nArtists names in sorted order:")
    print("----------------------------------------------------------")
    for artists in sortedartists:
        print(artists)

#prints the song names in sorted order
def songList(artistSongDictionary):
    sortedsongs = sorted(artistSongDictionary.values(), key=lambda x: x.lower())
    print("\nSong Titles in sorted order:")
    print("----------------------------------------------------------")
    for songs in sortedsongs:
        print(songs)

#checks if a users song title input is in the dictionary
def lookUpSong(artistSongDictionary):
    key = input('Enter a Song Title to find: ')

    if key in artistSongDictionary.values():
        print("Song found in dictionary.")
    else:
        print("Song Title not found.")

#checks if a users artist name is in the dictionary
def locateArtist(artistSongDictionary):
    name = input('Enter a Artist to find: ')

    if name in artistSongDictionary.keys():
        print('The Artist is in the dictionary.')
    else:
        print('That Artist is not found.')

#adds artist and song title to the dictionary
def addArtist(artistSongDictionary):
    name = input('Enter an Artist name: ')
    song = input('Enter a Song Title: ')

    #asks user to confirm their input
    confirm = input("Please confirm you want to add: " + name + ": " + song + " into the distionary? Please select yes or no [y,n]: ")
    #if confirmed then add artist and song if both of them arent in the dictionary already
    if (confirm == 'y'):
        if name not in artistSongDictionary:
            artistSongDictionary[name] = song
            displayNamesSongs(artistSongDictionary)
        else:
            if song not in artistSongDictionary.values():
                artistSongDictionary[name] = song
                displayNamesSongs(artistSongDictionary)
            else:
                print('That Artist and Song already exists.')
    else:
        print("Your input was cancelled, thank you.")

#updates the artists song title in the dictionary
def changeSong(artistSongDictionary):
    name = input('Enter an Artist name: ')

    if name in artistSongDictionary:
        song = input('Enter the new Song: ')
        #asks user to confirm update
        confirm = input("Please confirm you want to change: " + name + ": " + song + " into the distionary? Please select yes or no [y,n]: ")
        #updates song if confirmed
        if(confirm == 'y'):
            artistSongDictionary[name] = song
            displayNamesSongs(artistSongDictionary)
        else:
            print("Your change request was cancelled, thank you.")
    else:
        print('That Artist was not found.')

#removes artist and song from dictionary
def removeArtist(artistSongDictionary):
    name = input('Enter the Artist name to remove: ')

    if name in artistSongDictionary:
        confirm = input("Please confirm you want to remove: " + name + " from the distionary? Please select yes or no [y,n]: ")
        if(confirm == 'y'):
            del artistSongDictionary[name]
            displayNamesSongs(artistSongDictionary)
    else:
        print('That Artist was not found.')

#deletes all dictionary key value pairs
def clearDictionary(artistSongDictionary):
    artistSongDictionary.clear()
    displayNamesSongs(artistSongDictionary)
    print('\n\nAll Artists removed')

#main function to run selection menu
def main():
    #dictionary definition
    artistSongDictionary = {"Olivia Rodrigo": "Drivers License", "Silk Sonic":"Leave the Door Open",
                            "The Weeknd & Ariana Grande": "Save Your Tears",
                            "Dua Lipa feat. DaBaby": "Levitating", "Kali Uchis": "Telepatia",
                            "Pooh Shiesty feat. Lil Durk": "Back in Blood", "SZA": "Good Days",
                            "Justin Bieber feat. Daniel Caesar & Giveon": "Peaches", "Lil Nas X": "Montero"}
    #selection loop
    choice = 0
    while choice != 11:
        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == 1:
            displayNamesSongs(artistSongDictionary)
        elif choice == 2:
            numberSongs(artistSongDictionary)
        elif choice == 3:
            songList(artistSongDictionary)
        elif choice == 4:
            nameList(artistSongDictionary)
        elif choice == 5:
            lookUpSong(artistSongDictionary)
        elif choice == 6:
            locateArtist(artistSongDictionary)
        elif choice == 7:
            addArtist(artistSongDictionary)
        elif choice == 8:
            changeSong(artistSongDictionary)
        elif choice == 9:
            removeArtist(artistSongDictionary)
        elif choice == 10:
            clearDictionary(artistSongDictionary)
        elif choice == 11:
            print("you chose to quit. goodbye")

main()