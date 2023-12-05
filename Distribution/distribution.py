import scipy.stats as scst
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.write("""
# Приложение для построение распределений
""")

st.sidebar.header('Выбери тип распределения')
distr = st.sidebar.selectbox('Распределение',('Нормальное','Экспоненциальное','Пуассона'))

if distr == 'Нормальное':
    m = st.sidebar.slider('Среднее E[X]', 1.0,20.0,6.0)
    s = st.sidebar.slider('Стандартное отклонение', 0.1,10.0,1.0)
    # Создаем массив значений для построения графика
    x = np.linspace(-m-s*3, m+s*3, 50)
    y = scst.norm(m,s).pdf(x)
elif distr == 'Экспоненциальное':
    s = st.sidebar.slider('Scale=', 0.1,20.0,1.0)
    # Создаем массив значений для построения графика
    x = np.linspace(0, s*10, 40)
    y = scst.expon(scale=s).pdf(x)
else:
    l = st.sidebar.slider('Частота lambda=', 2,30,6)
    # Создаем массив значений для построения графика
    x = np.arange(-10, l*3, 1)
    y = scst.poisson(l).pmf(x)

# Displays the user input features
st.subheader(f'График распределения {distr}')

# Строим график нормального распределения
plt.plot(x,y, '--o')
plt.xticks(rotation=90)
plt.grid()
st.pyplot(plt.gcf())

# import scipy.stats as scst
# import numpy as np
# import streamlit as st

# st.write("""
# # Приложение для построение распределений
# """)

# st.sidebar.header('Выбери тип распределения')
# distr = st.sidebar.selectbox('Распределение',('Нормальное','Экспоненциальное','Пуассона'))

# if distr == 'Нормальное':
#     def user_input_features():
#         m = st.sidebar.slider('Среднее E[X]', -100.0,100.0,6.0)
#         s = st.sidebar.slider('Стандартное отклонение', 0.1,20.0,1.0)
#         # Создаем массив значений для построения графика
#         x = np.linspace(m - s*4, m + s*4, 1000)
#         y = scst.norm(m,s).pdf(x)
#         return y
#     input_df = user_input_features()
# elif distr == 'Экспоненциальное':
#     def user_input_features():
#         s1 = st.sidebar.slider('Scale=', 0.1,20.0,1.0)
#         # Создаем массив значений для построения графика
#         x1 = np.linspace(0, s*10, 1000)
#         y1 = scst.expon(scale=s).pdf(x1)
#         return y1
#     input_df = user_input_features()
# else:
#     def user_input_features():
#         l = st.sidebar.slider('Частота lambda=', 1.0,20.0,1.0)
#         # Создаем массив значений для построения графика
#         x2 = np.linspace(0, l*2, 100)
#         y2 = scst.poisson(l).pmf(x2)
#         return y2
#     input_df = user_input_features()


# # Displays the user input features
# st.subheader(f'График распределения {distr}')

# # Строим график нормального распределения
# st.area_chart()
