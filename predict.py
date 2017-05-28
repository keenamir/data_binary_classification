
import tensorflow as tf
import func_ml
import sys


if __name__ == "__main__":

    if len(sys.argv) == 1:
        # predict_file = 'TRAIN_TEST.csv'
        predict_file = 'VALIDATE_OUTG.csv'
        run_mode = 0
    elif len(sys.argv) < 7:
        predict_file = sys.argv[1]
        run_mode = 0
    else:
        run_mode = 1

    learning_rate = 0.001


