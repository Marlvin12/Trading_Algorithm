# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UzILuOte4iZ43W57Jt6q0D3mgHq-fm_-
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def identify_order_blocks(data, window=10, threshold=0.6):
    highs = data['High']
    lows = data['Low']
    blocks = []

    for i in range(window, len(data) - window):
        max_high = max(highs[i - window:i + window])
        min_low = min(lows[i - window:i + window])

        if highs[i] == max_high and lows[i] == min_low:
            block_range = max_high - min_low
            if block_range >= threshold * (data['High'].max() - data['Low'].min()):
                blocks.append({
                    'start_index': i - window,
                    'end_index': i + window,
                    'min_low': min_low,
                    'max_high': max_high,
                })

    return blocks

def plot_order_blocks(data, blocks):
    plt.figure(figsize=(14, 8))
    plt.plot(data['Close'], label='Close Price')

    for block in blocks:
        plt.axhline(block['min_low'], color='red', linestyle='--', alpha=0.5)
        plt.axhline(block['max_high'], color='green', linestyle='--', alpha=0.5)

    plt.legend()
    plt.show()

if __name__ == '__main__':
    file_path = 'path/to/your/price_data.csv'
    data = load_data(file_path)
    blocks = identify_order_blocks(data)
    plot_order_blocks(data, blocks)