import csv
import pandas as pd
import statistics

df = pd.read_csv("data_HeightWeight.csv")
height = df["Height(Inches)"].tolist()
weight = df["Weight(Pounds)"].tolist()
mean = statistics.mean(height)
median = statistics.median(height)
mode = statistics.mode(height)

mean_w = statistics.mean(weight)
median_w = statistics.median(weight)
mode_w = statistics.mode(weight)
print("height:-")
print("mean", mean,"median", median, "mode", mode)
print("weight:-")
print("mean", mean_w,"median", median_w, "mode", mode_w)