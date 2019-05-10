# Lyrics-Generation-using-BERT

English Rock lyrics generation using pre-trained BERT model (Devlin, J. et al., 2018). 

Data is obtained from the Kaggle 380,000+ Lyrics dataset. Used *langdetect* Python library to filter out songs in languages other than English. Used *pronouncing* Python library to search for properties for words like phones, syllables and rhyming words.

Used pre-trained **BERT MLM** for mask prediction and pre-trained **BERT NextSentence** for continuity prediction.

**Few Results**:
* **Only last word prediction in target lyric using BERT MLM** -

  | Sr. no.   | Lyric        | Predicted word           | True word  |
  |---------- | ------------- |:-------------|:-----|
  | 1         | *I've gotta empty out the inside of my head*
  |           | *I'd like to turn this place into my* **[MASK]**  | **_own_** | **_home_** |
  | 2         | *Down here where everything's crazy*
  |           | *The whole world's falling* **[MASK]**  | **_apart_** | **_apart_** |
  | 3         | *The world was that way when I got hear*
  |           | *We all link hands when the crowd cheers* **[MASK]** | **_again_**  | **_loudly_** |
  
* **Rhyming search for last word based on AABB rhyming and prediction for all prior words in target lyric using BERT MLM. Most likely occuring lyric obtained using BERT NextSentence** -

  | Sr. no.   | Context        | Predicted lyric           | True lyric  | 
  |---------- | ------------- |:-------------|:-----|
  | 1         | _Better to write than to have read_
  |           | _Better to cope than to complain_
  |           | _Better in your hands that in your head_
  |           | **[MASK] [MASK] ... [RHYME]** | **_Better to have read_** | **_Easier done than said_** |
  |           | _Like a dying flower that just don't give a damn_
  | 2        | _I’m not high on life_
  |           | _I’m not drunk on love_
  |           |_I’m broken down , not feeling right_
  |           | **[MASK] [MASK] ... [RHYME]** | **_I’m not drunk on my spite_** | **_I’m happy as I’m gonna be_** |
  |           | _And there’s nothing on the inside_ 
  | 3        | _Sorry, that's the last stop_
  |           | _I'll see you_
  |           |_I'll see you_
  |           | **[MASK] [MASK] ... [RHYME]** | **_Thanks, Miss Crewe_** |  **_On the way down_** |
  |           | _I'll see you_
  
* **Best sequence** -

  **20 choices** -
  
  | _You made me happy_ |
  | _Jimmy Carl Black (drums)_ |
  | _You tell me you don't love me over a cup of coffee_ |
  | _it's hot it's hot tonight_ |
  | _I prayed for a light_ |
  | _The saddest thing's to see him venerate that ball and chain_ |
  | _Yes the wonder of the Tundra_ |
  | _Time comes to a halt_ |
  | _he's fighting until he dies_ |
  | _Oh no, we won't give in, let's go living in the past._ |
  | _And it's a strange infatuation taking off across the nations_ |
  | _Beat is getting stronger_ |
  | _You apologize but I don't hear_ |
  | _You'll be sayin', you'll be saying_ |
  | _Sometimes big wave coming when I'm down_ |
  
  **50 choices** -
  
  _To condemn the man who dies_
  _I need someone_
  _Somewhere there's a place a soul can never go,_
  _Can't get no you know_
  _We're doin' a nu thang_
  _Is there life after talk 'cause there's talk on the road_
  _Changing rearranging every single day_
  _Care what these people say_
  _Won't you walk away_
  _fuck what the others have to say_

  
