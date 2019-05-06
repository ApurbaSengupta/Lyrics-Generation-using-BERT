We use the 380,000+ lyrics from MetroLyrics dataset available at Kaggle (https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics/data) for this project. 

The dataset consists of songs from various genres and artists in different languages, but our primary focus is on English Rock genre. We therefore filter out the rest of the songs and only keep English Rock songs for our project. We achieve this by converting the entire data into a pandas DataFrame object and selecting the Rock songs out of it. We then use 'langdetect' Python library to filter out Rock songs in languages other than English. Finally, we remove redundant songs by removing duplicate lyrics. 

The filtered data consists of ~92k English Rock songs between 1968 and 2016 (both inclusive), from over 3400 artists, including Bob Dylan, Elton John, David Bowie, America, Elvis Presley, Beatles, Coldplay and many others. The data is available in comma-separated value (CSV) format in the file 'english_rock.csv'. A typical row from the CSV file looks as shown below. It consists of the index of the song, the song title, the year the song was produced, the artist name, the genre (which is Rock for all data points), the song lyrics and the language of the song (which is all 'en' representing English songs):

*50732,desolation-row,1990,bob-dylan,Rock,"They're selling postcards of the hanging, they're painting the passports brown*<br>
*The beauty parlor is filled with sailors, the circus is in town<br>
...",en*

For the purpose of this project, we split the data into training, validation and test sets in the ratio of 8:1:1. We first randomly shuffle the data and then perform the above split. The training, validation and test data are then available in CSV format in the files 'train_rock.csv', 'val_rock.csv' and 'test_rock.csv' respectively. The 'make_data.py' script performs the above split and creates the training, validation and test data files.
