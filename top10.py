import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 加载数据
file_path = 'occ by year.csv'
data = pd.read_csv(file_path)

# 清理数据，去掉不必要的列
data_cleaned = data.drop(columns=['Unnamed: 0'])

# 筛选出现频率最高的五种物种
top_10_species = data_cleaned['scientificName'].value_counts().head(10).index
data_top_5 = data_cleaned[data_cleaned['scientificName'].isin(top_10_species)]

# 按年份和物种分组，计算每年的出现次数
yearly_counts = data_top_5.groupby(['year', 'scientificName']).size().unstack(fill_value=0)

# 绘制数据图表
plt.figure(figsize=(15, 8))
sns.lineplot(data=yearly_counts)
plt.title('Yearly Occurrences of Top 5 Species')
plt.xlabel('Year')
plt.ylabel('Number of Occurrences')
plt.legend(title='Species', labels=top_10_species)
plt.grid(True)
#plt.savefig('top 10 occ.jpg')
plt.show()

"""
# Filter the dataset for the top 5 species
top_5_species = top_10_species.head(5).index
data_top_5 = data_cleaned[data_cleaned['scientificName'].isin(top_5_species)]

# Grouping the data by year and species
yearly_counts = data_top_5.groupby(['year', 'scientificName']).size().unstack(fill_value=0)

# Plotting the data
plt.figure(figsize=(15, 8))
sns.lineplot(data=yearly_counts)
plt.title('Yearly Occurrences of Top 5 Species')
plt.xlabel('Year')
plt.ylabel('Number of Occurrences')
plt.legend(title='Species', labels=top_5_species)
plt.grid(True)

plt.show()

"""