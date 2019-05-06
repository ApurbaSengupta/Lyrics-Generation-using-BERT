1.  To use the evaluation script scoring.py, use:

    python scoring.py --goldfile <path to goldfile> --predfile <path to predfile>

2.  To run the simple baseline, use:

    python simple-baseline.py --datafile <path to test_rock.csv>

3.  To run BERT baselines, run the Jupyter notebook bert-baselines.ipynb and give the appropriate        path to test_rock.csv and save results in the appropriate goldfile and predfile

4.  To run BERT last word prediction, run the Jupyter notebook last-word-bert.ipynb and give the         appropriate path to test_rock.csv and save results in test_gold_file.txt and                         test_pred_file.txt in outputs/nextword

5.  To run BERT rhyming, run the Jupyter notebook rhymings.ipynb and give the appropriate path to        test_rock.csv and save results in test_gold_file.txt and test_pred_file.txt in outputs/rhymings

6.  To run reconstruction, run the Jupyter notebook reconstruction.ipynb and give the appropriate        path to test_rock.csv and save results in test_gold_file.txt and test_pred_file.txt in               outputs/reconstruction
