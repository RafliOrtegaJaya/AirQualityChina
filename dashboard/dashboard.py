import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

data_kualitas_udara = pd.read_csv("https://raw.githubusercontent.com/RafliOrtegaJaya/AirQualityChina/refs/heads/main/dashboard/data_kualitas_udara.csv")


st.title('Air Quality in China :sparkles:')

# Pertanyaan 1

st.header('Tren kualitas udara masing-masing stasiun sesuai dengan parameter kualitas udara di setiap tahunnya (2013 - 2017)')
st.write('Data berikut merupakan hasil pengolahan parameter kualitas udara berdasarkan tahun. Parameter kualitas udara terdiri dari PM2.5, PM10, SO2, NO2, CO, O3')

## Parameter PM2.5

tren_pm25 = data_kualitas_udara.groupby(['station', 'year'])['PM2.5'].mean().unstack()
st.subheader('Tren Rata-Rata Parameter PM2.5 di Setiap Stasiun (2013-2017)')

# Membuat gambar chart
fig, ax = plt.subplots(figsize=(10, 6))

for station in tren_pm25.columns:
    ax.plot(tren_pm25.index, tren_pm25[station], label=station, marker='o', linewidth=2)

ax.set_xlabel('Stasiun')
ax.set_xticklabels(tren_pm25.index, rotation=45)
ax.set_ylabel('PM2.5 (μg/m³)')
ax.set_title('Tren Rata-Rata Parameter PM2.5 di Setiap Stasiun (2013-2017)')
ax.legend(title='Tahun', loc='upper left', bbox_to_anchor=(1, 1))

# Tampilkan di Streamlit
st.pyplot(fig)

### insight
st.markdown(""" 
**Insight:**
- Visualisasi yang ditampilkan merupakan rata-rata setiap tahun (2013-2017) dari masing-masing 12 stasiun untuk nilai PM2.5.
- Dari tahun 2013 s.d. 2017, konsentrasi PM2.5 di setiap stasiun menunjukkan fluktuasi yang cukup signifikan dari tahun ke tahun. Namun, konsentrasi PM2.5 sebagian besar mengalami peningkatan di setiap stasiunnya.
- Tahun 2017 cenderung menunjukkan konsentrasi PM2.5 yang lebih tinggi dibandingkan tahun-tahun sebelumnya di sebagian besar stasiun. Stasiun dengan nilai PM2.5 tertinggi adalah stasiun Wanshouxigong, sedangkan stasiun dengan nilai PM2.5 terendah adalah stasiun Huairou.
- Dari tahun 2013 s.d. 2017, stasiun Dongsi menjadi stasiun yang mengalami peningkatan yang paling tidak signifikan.
""")

## Parameter PM10
tren_pm10 = data_kualitas_udara.groupby(['station', 'year'])['PM10'].mean().unstack()
st.subheader('Tren Rata-Rata Parameter PM10 di Setiap Stasiun (2013-2017)')

# Membuat gambar chart
fig, ax = plt.subplots(figsize=(10, 6))

for station in tren_pm10.columns:
    ax.plot(tren_pm10.index, tren_pm10[station], label=station, marker='o', linewidth=2)

ax.set_xlabel('Stasiun')
ax.set_xticklabels(tren_pm10.index, rotation=45)
ax.set_ylabel('PM10 (μg/m³)')
ax.set_title('Tren Rata-Rata Parameter PM10 di Setiap Stasiun (2013-2017)')
ax.legend(title='Tahun', loc='upper left', bbox_to_anchor=(1, 1))

# Tampilkan di Streamlit
st.pyplot(fig)

### Insight
st.markdown("""
**Insight:**
- Visualisasi yang ditampilkan merupakan rata-rata setiap tahun (2013-2017) dari masing-masing 12 stasiun untuk nilai PM10.
- Dari tahun 2013 s.d. 2017, konsentrasi PM10 di setiap stasiun menunjukkan fluktuasi yang cukup signifikan dari tahun ke tahun. Namun, konsentrasi PM10 sebagian besar mengalami peningkatan di setiap stasiunnya.
- Tahun 2014 dan 2017 cenderung menunjukkan konsentrasi PM10 yang lebih tinggi dibandingkan tahun lain di sebagian besar stasiun. Stasiun dengan nilai PM10 tertinggi di 2014 adalah stasiun **Gucheng** dan di tahun 2017 adalah **Dongsi**, sedangkan stasiun dengan nilai PM10 terendah di tahun 2014 adalah stasiun **Dingling** dan di tahun 2017 adalah stasiun **Dingling**.
""")

## Parameter SO2
tren_so2 = data_kualitas_udara.groupby(['station', 'year'])['SO2'].mean().unstack()
st.subheader('Tren Rata-Rata Parameter SO2 di Setiap Stasiun (2013-2017)')

# Membuat gambar chart
fig, ax = plt.subplots(figsize=(10, 6))

for station in tren_so2.columns:
    ax.plot(tren_so2.index, tren_so2[station], label=station, marker='o', linewidth=2)

ax.set_xlabel('Stasiun')
ax.set_xticklabels(tren_so2.index, rotation=45)
ax.set_ylabel('SO2 (μg/Nm³)')
ax.set_title('Tren Rata-Rata Parameter SO2 di Setiap Stasiun (2013-2017)')
ax.legend(title='Tahun', loc='upper left', bbox_to_anchor=(1, 1))

# Tampilkan di Streamlit
st.pyplot(fig)

### Insight
st.markdown("""
**Insight:**
- Visualisasi yang ditampilkan merupakan rata-rata setiap tahun (2013-2017) dari masing-masing 12 stasiun untuk nilai SO2.
- Dari tahun 2013 s.d. 2017, konsentrasi SO2 memiliki perbedaan yang cukup besar antara satu stasiun dengan stasiun lainnya. Hal ini mengindikasikan bahwa tingkat pencemaran udara oleh SO2 di berbagai lokasi memiliki karakteristik yang berbeda.
- Tahun 2013 dan 2014 cenderung menunjukkan konsentrasi SO2 yang lebih tinggi dibandingkan tahun lain di sebagian besar stasiun.
""")

## Parameter NO2
tren_no2 = data_kualitas_udara.groupby(['station', 'year'])['NO2'].mean().unstack()
st.subheader('Tren Rata-Rata Parameter NO2 di Setiap Stasiun (2013-2017)')

# Membuat gambar chart
fig, ax = plt.subplots(figsize=(10, 6))

for station in tren_no2.columns:
    ax.plot(tren_no2.index, tren_no2[station], label=station, marker='o', linewidth=2)

ax.set_xlabel('Stasiun')
ax.set_xticklabels(tren_no2.index, rotation=45)
ax.set_ylabel('NO2 (μg/Nm³)')
ax.set_title('Tren Rata-Rata Parameter NO2 di Setiap Stasiun (2013-2017)')
ax.legend(title='Tahun', loc='upper left', bbox_to_anchor=(1, 1))

# Tampilkan di Streamlit
st.pyplot(fig)

### Insight
st.markdown("""
**Insight:**
- Visualisasi yang ditampilkan merupakan rata-rata setiap tahun (2013-2017) dari masing-masing 12 stasiun untuk nilai NO2.
- Dari tahun 2013 s.d. 2017, konsentrasi NO2 menunjukkan fluktuasi yang minim di setiap stasiunnya. Hal ini dapat dilihat di grafik bahwa garis yang merepresentasikan nilai rata-rata NO2 cenderung berhimpitan.
""")

## Parameter CO
tren_co = data_kualitas_udara.groupby(['station', 'year'])['CO'].mean().unstack()
st.subheader('Tren Rata-Rata Parameter CO di Setiap Stasiun (2013-2017)')

# Membuat gambar chart
fig, ax = plt.subplots(figsize=(10, 6))

for station in tren_co.columns:
    ax.plot(tren_co.index, tren_co[station], label=station, marker='o', linewidth=2)

ax.set_xlabel('Stasiun')
ax.set_xticklabels(tren_co.index, rotation=45)
ax.set_ylabel('CO (μg/Nm³)')
ax.set_title('Tren Rata-Rata Parameter CO di Setiap Stasiun (2013-2017)')
ax.legend(title='Tahun', loc='upper left', bbox_to_anchor=(1, 1))

# Tampilkan di Streamlit
st.pyplot(fig)

### Insight
st.markdown("""
**Insight:**
- Visualisasi yang ditampilkan merupakan rata-rata setiap tahun (2013-2017) dari masing-masing 12 stasiun untuk nilai CO.
- Dari tahun 2013 s.d. 2016, konsentrasi CO menunjukkan fluktuasi yang cukup minim di setiap stasiunnya. Hal ini dapat dilihat di grafik bahwa garis yang merepresentasikan nilai rata-rata CO cenderung berhimpitan. Namun, konsentrasi CO mengalami peningkatan di tahun 2017 untuk setiap stasiun.
""")

## Parameter O3
tren_o3 = data_kualitas_udara.groupby(['station', 'year'])['O3'].mean().unstack()
st.subheader('Tren Rata-Rata Parameter O3 di Setiap Stasiun (2013-2017)')

# Membuat gambar chart
fig, ax = plt.subplots(figsize=(10, 6))

for station in tren_o3.columns:
    ax.plot(tren_o3.index, tren_o3[station], label=station, marker='o', linewidth=2)

ax.set_xlabel('Stasiun')
ax.set_xticklabels(tren_o3.index, rotation=45)
ax.set_ylabel('O3 (μg/Nm³)')
ax.set_title('Tren Rata-Rata Parameter O3 di Setiap Stasiun (2013-2017)')
ax.legend(title='Tahun', loc='upper left', bbox_to_anchor=(1, 1))

# Tampilkan di Streamlit
st.pyplot(fig)

### Insight
st.markdown("""
**Insight:**
- Visualisasi yang ditampilkan merupakan rata-rata setiap tahun (2013-2017) dari masing-masing 12 stasiun untuk nilai O3.
- Dari tahun 2013 s.d. 2016, konsentrasi O3 memiliki perbedaan yang tidak terlalu signifikan. Namun, pada tahun 2017 seluruh stasiun mengalami penurunan kadar O3 yang signifikan dibanding tahun-tahun sebelumnya.
- Stasiun **Gucheng** menjadi stasiun yang memiliki kadar O3 terendah di tahun 2017.
""")

# Pertanyaan 2
st.header('Hubungan antara parameter kualitas udara terhadap parameter meteorologi')
st.write('Untuk menjawab pertanyaan di atas, dapat dilakukan analisis korelasi')

## Korelasi dengan Heatmap
st.subheader('Analisis Korelasi dengan Heatmap')
st.write('Heatmap ini akan menampilkan korelasi antara tiap parameter kualitas udara dan parameter meteorologi')

# Heatmap
corr_matrix = data_kualitas_udara[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'RAIN', 'PRES']].corr()

# Membuat gambar untuk heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.title('Korelasi Matrix Heatmap dari Parameter Kualitas Udara')

# Tampilkan di streamlit
st.pyplot(plt)

### Insight
st.markdown("""
**Insight:**

**Korelasi Positif**

- PM2.5 dan PM10 memiliki korelasi positif yang sangat kuat, yaitu memiliki koefisien relasi (r) sebesar **0.88**. Ini menunjukkan bahwa kedua jenis partikel ini seringkali berasal dari sumber yang sama, seperti asap, debu, dan partikel halus lainnya.
- SO2 dan NO2 terhadap PM2.5 dan PM10 juga memiliki korelasi positif yang cukup kuat. Hal ini menunjukkan bahwa keduanya ada kemungkinan dihasilkan dari proses pembakaran, seperti pembakaran bahan bakar fosil.
- Suhu terhadap O3 memiliki korelasi positif yang cukup kuat. Hal ini menunjukkan kecenderungan bahwa semakin suhu meningkat, bahwa nilai O3 juga meningkat

**Korelasi Negatif**

- O3 memiliki korelasi negatif dengan PM2.5, PM10, SO2, dan NO2. Hal ini menunjukkan bahwa peningkatan konsentrasi ozon seringkali diiringi dengan penurunan konsentrasi partikel dan gas-gas lain.
- Suhu juga memiliki korelasi negatif dengan partikel PM2.5 dan PM10, serta terhadap SO2 dan NO2.
- Curah hujan umumnya memiliki korelasi negatif dengan sebagian besar polutan, seperti PM2.5, PM10, SO2, dan NO2. Artinya, curah hujan yang relatif tinggi dapat menurunkan kadar polutan tersebut
""")

# Analisis Lanjutan
st.header('Analisis Clustering')
st.write('Kali ini, digunakan teknik **binning** untuk analisis clustering dalam kaitannya dengan kualitas udara untuk membagi data menjadi interval atau kategori tertentu. Acuan yang digunakan adalah Air Quality Index (AQI). Berikut adalah cara nya:')

## Klasifikasi PM2.5
st.subheader('Klasifikasi PM2.5')

data_kualitas_udara = data_kualitas_udara
data_pm25 = data_kualitas_udara[['station', 'PM2.5', 'year']].dropna()

bins = [0, 51, 101, 151, 201, 301, 500]
labels = [
    'Sangat baik', 
    'Baik',
    'Sedikit tercemar',
    'Cukup tercemar',
    'Sangat tercemar',
    'Tercemar parah'
]

years = data_pm25['year'].unique()
selected_year = st.selectbox("Pilih Tahun:", years)
yearly_data = data_pm25[data_pm25['year'] == selected_year]
yearly_data['AQI_Class'] = pd.cut(yearly_data['PM2.5'], bins=bins, labels=labels)

binned_counts = yearly_data.groupby(['station', 'AQI_Class']).size().unstack(fill_value=0)

plt.figure(figsize=(12, 8))
binned_counts.plot(kind='bar', stacked=True, colormap='coolwarm')
plt.title("Distribusi Kualitas Udara Parameter PM2.5 berdasarkan AQI di Setiap Stasiun {}".format(selected_year))
plt.xlabel('Stasiun')
plt.ylabel('Jumlah Data')
plt.xticks(rotation=45)
plt.legend(title='Kelas AQI', loc='upper left', bbox_to_anchor=(1, 1), labels=labels)
plt.grid(axis='y')

st.pyplot(plt)

## Klasifikasi PM10
st.subheader('Klasifikasi PM10')

data_kualitas_udara = data_kualitas_udara
data_pm10 = data_kualitas_udara[['station', 'PM10', 'year']].dropna()

bins = [0, 51, 101, 151, 201, 301, 500]
labels = [
    'Sangat baik', 
    'Baik',
    'Sedikit tercemar',
    'Cukup tercemar',
    'Sangat tercemar',
    'Tercemar parah'
]

years = data_pm10['year'].unique()
selected_year = st.selectbox("Pilih Tahun:", years)
yearly_data = data_pm10[data_pm10['year'] == selected_year]
yearly_data['AQI_Class'] = pd.cut(yearly_data['PM10'], bins=bins, labels=labels)

binned_counts = yearly_data.groupby(['station', 'AQI_Class']).size().unstack(fill_value=0)

plt.figure(figsize=(12, 8))
binned_counts.plot(kind='bar', stacked=True, colormap='coolwarm')
plt.title("Distribusi Kualitas Udara Parameter PM10 berdasarkan AQI di Setiap Stasiun {}".format(selected_year))
plt.xlabel('Stasiun')
plt.ylabel('Jumlah Data')
plt.xticks(rotation=45)
plt.legend(title='Kelas AQI', loc='upper left', bbox_to_anchor=(1, 1), labels=labels)
plt.grid(axis='y')

st.pyplot(plt)

## Klasifikasi SO2
st.subheader('Klasifikasi SO2')

data_kualitas_udara = data_kualitas_udara
data_so2 = data_kualitas_udara[['station', 'SO2', 'year']].dropna()

bins = [0, 51, 101, 151, 201, 301, 500]
labels = [
    'Sangat baik', 
    'Baik',
    'Sedikit tercemar',
    'Cukup tercemar',
    'Sangat tercemar',
    'Tercemar parah'
]

years = data_so2['year'].unique()
selected_year = st.selectbox("Pilih Tahun:", years)
yearly_data = data_so2[data_so2['year'] == selected_year]
yearly_data['AQI_Class'] = pd.cut(yearly_data['SO2'], bins=bins, labels=labels)

binned_counts = yearly_data.groupby(['station', 'AQI_Class']).size().unstack(fill_value=0)

plt.figure(figsize=(12, 8))
binned_counts.plot(kind='bar', stacked=True, colormap='coolwarm')
plt.title("Distribusi Kualitas Udara Parameter SO2 berdasarkan AQI di Setiap Stasiun {}".format(selected_year))
plt.xlabel('Stasiun')
plt.ylabel('Jumlah Data')
plt.xticks(rotation=45)
plt.legend(title='Kelas AQI', loc='upper left', bbox_to_anchor=(1, 1), labels=labels)
plt.grid(axis='y')

st.pyplot(plt)

## Klasifikasi NO2
st.subheader('Klasifikasi NO2')

data_kualitas_udara = data_kualitas_udara
data_no2 = data_kualitas_udara[['station', 'NO2', 'year']].dropna()

bins = [0, 51, 101, 151, 201, 301, 500]
labels = [
    'Sangat baik', 
    'Baik',
    'Sedikit tercemar',
    'Cukup tercemar',
    'Sangat tercemar',
    'Tercemar parah'
]

years = data_no2['year'].unique()
selected_year = st.selectbox("Pilih Tahun:", years)
yearly_data = data_no2[data_no2['year'] == selected_year]
yearly_data['AQI_Class'] = pd.cut(yearly_data['NO2'], bins=bins, labels=labels)

binned_counts = yearly_data.groupby(['station', 'AQI_Class']).size().unstack(fill_value=0)

plt.figure(figsize=(12, 8))
binned_counts.plot(kind='bar', stacked=True, colormap='coolwarm')
plt.title("Distribusi Kualitas Udara Parameter NO2 berdasarkan AQI di Setiap Stasiun {}".format(selected_year))
plt.xlabel('Stasiun')
plt.ylabel('Jumlah Data')
plt.xticks(rotation=45)
plt.legend(title='Kelas AQI', loc='upper left', bbox_to_anchor=(1, 1), labels=labels)
plt.grid(axis='y')

st.pyplot(plt)

## Klasifikasi CO
st.subheader('Klasifikasi CO')

data_kualitas_udara = data_kualitas_udara
data_co = data_kualitas_udara[['station', 'CO', 'year']].dropna()

bins = [0, 51, 101, 151, 201, 301, 500]
labels = [
    'Sangat baik', 
    'Baik',
    'Sedikit tercemar',
    'Cukup tercemar',
    'Sangat tercemar',
    'Tercemar parah'
]

years = data_co['year'].unique()
selected_year = st.selectbox("Pilih Tahun:", years)
yearly_data = data_co[data_co['year'] == selected_year]
yearly_data['AQI_Class'] = pd.cut(yearly_data['CO'], bins=bins, labels=labels)

binned_counts = yearly_data.groupby(['station', 'AQI_Class']).size().unstack(fill_value=0)

plt.figure(figsize=(12, 8))
binned_counts.plot(kind='bar', stacked=True, colormap='coolwarm')
plt.title("Distribusi Kualitas Udara Parameter CO berdasarkan AQI di Setiap Stasiun {}".format(selected_year))
plt.xlabel('Stasiun')
plt.ylabel('Jumlah Data')
plt.xticks(rotation=45)
plt.legend(title='Kelas AQI', loc='upper left', bbox_to_anchor=(1, 1), labels=labels)
plt.grid(axis='y')

st.pyplot(plt)

## Klasifikasi O3
st.subheader('Klasifikasi O3')

data_kualitas_udara = data_kualitas_udara
data_o3 = data_kualitas_udara[['station', 'O3', 'year']].dropna()

bins = [0, 51, 101, 151, 201, 301, 500]
labels = [
    'Sangat baik', 
    'Baik',
    'Sedikit tercemar',
    'Cukup tercemar',
    'Sangat tercemar',
    'Tercemar parah'
]

years = data_o3['year'].unique()
selected_year = st.selectbox("Pilih Tahun:", years)
yearly_data = data_o3[data_o3['year'] == selected_year]
yearly_data['AQI_Class'] = pd.cut(yearly_data['O3'], bins=bins, labels=labels)

binned_counts = yearly_data.groupby(['station', 'AQI_Class']).size().unstack(fill_value=0)

plt.figure(figsize=(12, 8))
binned_counts.plot(kind='bar', stacked=True, colormap='coolwarm')
plt.title("Distribusi Kualitas Udara Parameter O3 berdasarkan AQI di Setiap Stasiun {}".format(selected_year))
plt.xlabel('Stasiun')
plt.ylabel('Jumlah Data')
plt.xticks(rotation=45)
plt.legend(title='Kelas AQI', loc='upper left', bbox_to_anchor=(1, 1), labels=labels)
plt.grid(axis='y')

st.pyplot(plt)
