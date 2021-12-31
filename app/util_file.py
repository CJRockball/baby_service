# df = pd.read_csv(SOURCE_DATA_FILE)
# del_cols = ["L", "M", "S"]
# df = df.drop(columns=del_cols)
# xx = df.Week.values
# x_J = [i for i in range(len(df.Jennifer.to_list()))]
# plt.figure()
# plt.fill_between(xx, df.SD0.values, df.SD1.values, color="green", alpha=0.4)
# plt.fill_between(xx, df.SD1.values, df.SD2.values, color="yellow", alpha=0.4)
# plt.fill_between(xx, df.SD2.values, df.SD3.values, color="red", alpha=0.4)
# plt.plot(xx, df.SD0.values, color="black")
# plt.fill_between(xx, df.SD1neg.values, df.SD0.values, color="green", alpha=0.4)
# plt.fill_between(xx, df.SD2neg.values, df.SD1neg.values, color="yellow", alpha=0.4)
# plt.fill_between(xx, df.SD3neg.values, df.SD2neg.values, color="red", alpha=0.4)
# plt.scatter(x_J, df.Jennifer.values)
# plt.grid()
# plt.show()
