import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, LSTM, Attention
from tensorflow.keras.models import Model

def build_rnn_attention_model(input_shape):
    inputs = Input(shape=input_shape)
    lstm_out = LSTM(64, return_sequences=True)(inputs)
    attention = Attention()([lstm_out, lstm_out])
    flat = tf.keras.layers.Flatten()(attention)
    dense = Dense(64, activation='relu')(flat)
    outputs = Dense(1)(dense)
    model = Model(inputs=inputs, outputs=outputs)
    return model