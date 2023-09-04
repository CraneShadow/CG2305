import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('1-sepshock_MIMIC_allfeatures.csv')
# print(df.columns) # length = 128 → 每一行有128个字段


## -- admission_age
print(df['admission_age'].describe())
print(df['admission_age'].isnull().sum()) # 0

# filename = '1-sepshock_MIMIC_allfeatures.csv'
# total = sum(1 for line in open(filename))
# print('The total lines is ',total) # 11949 → 文件共11949行，除去表头的一行，剩下11948行，每一行对应一个患者，一个患者只有一行

# num_subject = df.loc[:,'subject_id'].value_counts()
# print(num_subject) # Length = 11948 → 总共有11948个患者
#
# num_hadm = df.loc[:,'hadm_id'].value_counts()
# print(num_hadm) # Length = 11948 → 总共有11948个住院时间
#
# num_stay = df.loc[:,'stay_id'].value_counts()
# print(num_stay) # Length = 11948 → 总共有11948个患者住院部门

# print(df['suspected_infection_time'].isnull().sum()) # 0 → 每一个患者都有标记“疑似感染时间”
# print(df['sep_shock_t'].isnull().sum()) # 0 → 每一个患者都有标记“感染性休克病发时间”
# print(df['sur_time'].isnull().sum()) # 9472 → 刚好和存活患者的数量一致
# print(df['los_hospital'].isnull().sum()) # 0 → 每一个患者都有记录“住院时长”
# print(df['los_icu'].isnull().sum()) # 0 → 每一个患者都有记录“住ICU时长”

# print((df['los_hospital'] >= df['los_icu']).sum()) # 10491 → 10491个患者住院时长比住ICU时长更长（这才比较正常）
# print((df['los_hospital'] < df['los_icu']).sum()) # 1457 → 1457个患者住院时长短于住ICU时长（为什么会出现这种情况？）
# print(((df['los_icu'] - df['los_hospital'] > 0) & (df['los_icu'] - df['los_hospital'] < 15.8)).sum())
## 观察住icu时间能比住院时间长多少（即使我认为这种情况的存在是不合理的）
# df['hospital_subtract_icu'] = df['los_hospital'].sub(df['los_icu'])
# # print(df['hospital_subtract_icu'].min()) # -15.709861111 → 住ICU时间最多比住院时间长约15.7天
# df_2 = df[df['hospital_subtract_icu'] < 0]
# # print(df_2)
# print(df_2['hospital_subtract_icu'].describe())
# df_2['hospital_subtract_icu'].hist()
# plt.show()

# num_dead = df.loc[:, 'dead'].value_counts()
# print(num_dead) # survive(0): 9472, dead(1): 2476
#
# num_HL = df.loc[:, 'H-L'].value_counts()
# print(num_HL) # low-risk(0): 9675(入住ICU后28天内死亡), high-risk(1): 2273(入住28天后死亡或者存活)

# print(((df['dead'] == 0) & (df['H-L'] == 0)).sum()) # 9472 （存活患者全为低危，但低危患者未必存活）
# print(((df['dead'] == 0) & (df['H-L'] == 1)).sum()) # 0 （存活患者全为低危）
# print(((df['dead'] == 1) & (df['H-L'] == 0)).sum()) # 203 （死亡的2476个患者中，203个患者低危）
# print(((df['dead'] == 1) & (df['H-L'] == 1)).sum()) # 2273 （死亡的2476个患者中，2273个患者高危）

"""
2-sepshock_vitalsign.csv
"""
# filename = '2-sepshock_vitalsign.csv'
# total = sum(1 for line in open(filename))
# print('The total lines is ',total) # 3066164 → 这个文件总共有3066164行，除了表头，就是3066163行数据

# df = pd.read_csv('2-sepshock_vitalsign.csv')

# num_subject = df.loc[:,'subject_id'].value_counts()
# print(num_subject) # Length = 11948 → 总共有11948个患者，11488234号患者行数最多，有5786行；15434313号患者行数最少，有8行（不统一，有点难搞，需要处理）

# num_stay = df.loc[:,'stay_id'].value_counts()
# print(num_stay) # Length = 11948 → 总共有11948个患者，每个患者的行数统计情况跟num_subject的行数统计情况是一样的