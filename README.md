# Lyrics-Generation-using-BERT

English Rock lyrics generation using pre-trained BERT model (Devlin, J. et al., 2018). 

Data is obtained from the Kaggle 380,000+ Lyrics dataset. Used 'langdetect' Python library to filter out songs in languages other than English.

Results:
* Last word prediction for target lyric
  | Lyric        | Predicted word           | True word  |
  | ------------- |:-------------:| -----:|
  | I've gotta empty out the inside of my head
    I'd like to turn this place into my <To be predicted>      | own | home |
  | Down here where everything's crazy
    The whole world's falling <To be predicted>     | apart      |   apart |
  | The world was that way when I got hear
    We all link hands when the crowd cheers <To be predicted> | again     |    loudly |
