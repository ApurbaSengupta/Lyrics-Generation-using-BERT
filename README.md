# Lyrics-Generation-using-BERT

English Rock lyrics generation using pre-trained BERT model (Devlin, J. et al., 2018). 

Data is obtained from the Kaggle 380,000+ Lyrics dataset. Used 'langdetect' Python library to filter out songs in languages other than English. Used 'pronouncing' Python library to search for properties for words like phones, syllables and rhyming words.

Used pre-trained BERT MLM for mask prediction and pre-trained BERT NextSent for continuity prediction.

### Results:
* #### Only last word prediction in target lyric

  | Sr. no.   | Lyric        | Predicted word           | True word  |
  |---------- | ------------- |:-------------:| -----:|
  | 1         | I've gotta empty out the inside of my head
  |           | I'd like to turn this place into my [MASK]      | own | home |
  | 2         | Down here where everything's crazy
  |           | The whole world's falling [MASK]     | apart      |   apart |
  | 3         | The world was that way when I got hear
  |           | We all link hands when the crowd cheers [MASK] | again     |    loudly |
  
* #### Rhyming search for last word based on AABB rhyming and prediction for all prior words in target lyric

  | Sr. no.   | Context        | Predicted lyric           | True lyric  | 
  |---------- | ------------- |:-------------:| -----:|
  | 1         | Better to write than to have read
  |           | Better to cope than to complain
  |           | Better in your hands that in your head
  |           | [MASK] [MASK] ... [RHYME]
  |           | Like a dying flower that just don't give a damn | Better to have read | Easier done than said |
  
