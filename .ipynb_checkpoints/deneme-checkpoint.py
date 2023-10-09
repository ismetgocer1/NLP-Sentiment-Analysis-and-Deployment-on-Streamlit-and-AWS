import streamlit as st

# text message
st.title ("Streamlit deneme")
st.text ("Hello deneme")


st.markdown("**Kalın Metin**")
st.latex(r'E = mc^2')  #LaTeX formatında matematiksel ifadeler ekler.

#st.audio()

#st.line_chart(df)
#st.bar_chart()
#st.area_chart()
#st.pyplot()
#st.altair_chart()
#st.map()
st.slider("Kaydır", 0, 100, 50)
st.selectbox('Seçiniz:', ['A', 'B', 'C'])
#st.multiselect()
st.text_input('Adınızı Girin:')
st.number_input('Bir sayı girin:', min_value=1, max_value=10)
#st.date_input()
#st.time_input()
#st.file_uploader()

#st.button()
if st.button('Tıkla'): st.write('Butona tıklandı!')

#st.checkbox()
if st.checkbox('Onayla'): st.write('Onaylandı!')


#st.beta_columns()

#st.beta_expander()
with st.expander('Detaylar'): st.write('İçerik')

#st.progress()
#for i in range(100): st.progress(i)

# st.sidebar.title()   yan panel başlığı ekler
#st.sidebar.title('Yan Panel Başlığı')

#st.code()
import pandas as pd

# Veri çerçevesini görüntüler
df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
st.code(
    df.to_markdown(),
    #lang="markdown",
    #linenumbers=True,
)

## --------------------------------------------

## Dosya Yükleme
import pandas as pd

# Dosya yükleme widget'ını ekleyin
#uploaded_file = st.file_uploader("Advertising.csv", type=["csv"])

# Eğer bir dosya yüklendiyse, bu dosyayı pandas ile okuyun
#if uploaded_file is not None:
    #data = pd.read_csv(uploaded_file)
    #st.write(data)  # DataFrame'i ekrana yazdır

    
## --------------------------------------------

# Dosyayı doğrudan pandas ile okuyun..dpsya aynı dizinde olmalı
data = pd.read_csv('Advertising.csv')

# DataFrame'i ekrana yazdır
st.write(data)
# st.dataframe(data)   aynı şeyi yapar (df i ekrana yazdırır

## --------------------------------------------
# Plotly ile bir scatter plot oluşturalım. rneğin, TV reklam bütçesi ile satışları karşılaştıralım.

import plotly.express as px

fig = px.scatter(data, x='TV', y='sales', title='TV Reklamları vs. Satışlar')
st.plotly_chart(fig)

## --------------------------------------------
#Vega-Lite ile bir bar chart oluşturalım.Örneğin, radyo reklam bütçesinin ortalamasını gösterelim.

bar_chart = {
    "mark": "bar",
    "encoding": {
        "x": {"field": "radio", "bin": True, "type": "quantitative"},
        "y": {"aggregate": "average", "field": "sales", "type": "quantitative"}
    }
}
st.vega_lite_chart(data, bar_chart)

## --------------------------------------------
#Bu fonksiyon, Graphviz ile grafikler oluşturmak için kullanılır. Advertising.csv bu tür bir görselleştirme için uygun değil, ancak genel bir örnek vermek gerekirse:

graph_code = """
    digraph {
        a -> b;
        b -> c;
        c -> d;
        d -> a;
    }
"""
st.graphviz_chart(graph_code)


## --------------------------------------------

#st.pyplot(): Bu fonksiyon, Matplotlib ile oluşturulan grafikleri göstermek için kullanılır. Örneğin, TV reklam bütçesi ile satışları bir scatter plot ile gösterelim:

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(data['TV'], data['sales'], color='blue')
plt.title('TV Reklamları vs. Satışlar')
plt.xlabel('TV Reklam Bütçesi')
plt.ylabel('Satışlar')
st.pyplot(plt)

## --------------------------------------------
#st.altair_chart():Altair ile bir bar chart oluşturalım. Örneğin, radyo reklam bütçesi ile satışları karşılaştıralım:
import altair as alt

chart = alt.Chart(data).mark_bar().encode(
    x='radio',
    y='sales',
    color='sales'
).properties(
    title='Radyo Reklamları vs. Satışlar'
)
st.altair_chart(chart, use_container_width=True)



## --------------------------------------------
#st.map():Bu fonksiyon, coğrafi veri görselleştirmesi için kullanılır. Advertising.csv bu tür verilere sahip olmadığı için bu fonksiyonun kullanımı bu veri seti için uygun değil. Ancak, genel bir örnek vermek gerekirse:

# Örnek veri
map_data = pd.DataFrame({
    'lat': [37.76, 37.77, 37.78],
    'lon': [-122.4, -122.5, -122.6]
})

st.map(map_data)

## --------------------------------------------
# st.line_chart():Bu fonksiyon, çizgi grafikleri göstermek için kullanılır. Örneğin, veri setindeki satışları bir çizgi grafiği ile gösterelim:

st.line_chart(data['sales'])
## --------------------------------------------


## --------------------------------------------