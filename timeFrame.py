import pandas as pd
import matplotlib.pyplot as plt

# 加载数据集
file_path = 'adjust_mpo_nafo_bottomtrawl_event_1970-2019.csv'
data = pd.read_csv(file_path)

if __name__ == "__main__":
    # 确保日期列是正确的日期格式
    data['date'] = pd.to_datetime(data[['year', 'month', 'day']])

    # 以日期进行分组并计算每天的事件数量
    daily_counts = data.groupby('year').size()

    # 绘制时间序列图
    plt.figure(figsize=(12, 6))
    daily_counts.plot()
    plt.title('Event Counts by year')
    plt.xlabel('Year')
    plt.ylabel('Number of Events')
    plt.grid(True)
    #plt.savefig('Event Counts by year.png')
    plt.show()

