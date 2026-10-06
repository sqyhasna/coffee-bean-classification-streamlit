import streamlit as st
from PIL import Image
from pathlib import Path

def run():
    st.title('Exploratory Data Analysis')

    st.write(
        'berikut merupakan sample gambar dari masing-masing class '
        'coffee bean yang digunakan pada dataset.'
    )

    BASE_DIR = Path(__file__).resolve().parent

    class_names = [
        'Dark',
        'Green',
        'Light',
        'Medium'
    ]

    image_paths = [
        BASE_DIR / 'dark.png',
        BASE_DIR / 'green.png',
        BASE_DIR / 'light.png',
        BASE_DIR / 'medium.png'
]
    columns = st.columns(4)

    for column, class_name, image_path in zip(
        columns,
        class_names,
        image_paths
    ):
        image = Image.open(image_path)

        with column:
            st.subheader(class_name)
            st.image(
                image,
                use_container_width=True
            )

    st.write(
        'berdasarkan sample gambar, masing-masing class memiliki '
        'perbedaan warna yang cukup terlihat. Green cenderung '
        'berwarna hijau pucat, Light berwarna coklat muda, '
        'Medium berwarna coklat, sedangkan Dark berwarna coklat gelap.'
    )