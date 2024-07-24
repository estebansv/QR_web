import streamlit as st
import pyqrcode
import tempfile

def generate_qr(text, output_format="png", show_image=False):
    """Generates a QR code from the provided text and saves it in the specified format.

    Args:
        text (str): The text to encode in the QR code.
        output_format (str, optional): The desired output format (png, svg, etc.). Defaults to "png".
        show_image (bool, optional): Whether to show the generated image. Defaults to False.
    """
    try:
        qr = pyqrcode.create(text)

        # Crear un archivo temporal con un nombre único para evitar conflictos
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f".{output_format}")

        # Save the QR code in the specified format
        if output_format == "png":
            qr.png(temp_file.name, scale=8)
        elif output_format == "svg":
            qr.svg(temp_file.name, scale=8)
        else:
            st.error(f"Unsupported output format: {output_format}")
            return None

        if show_image:
            # Mostrar el código QR en la página web
            st.image(temp_file.name)

        return temp_file.name
    except Exception as e:
        st.error(f"Error generating QR code: {e}")
        return None

def main():
    # Título de la aplicación
    st.title("📉 Generador de Códigos QR TT 📜")

    # Campo de entrada de texto
    text = st.text_input("Ingrese el texto para el código QR:")

    # Selector de formato de salida
    output_format = st.selectbox("Seleccione el formato de salida:", ["PNG", "SVG"])

    # Botón para generar y mostrar el QR
    if st.button("Generar QR"):
        generated_qr = generate_qr(text, output_format.lower(), show_image=True)
        if generated_qr:
            # Mostrar el código QR en un cuadro
            with st.container():
                st.success("QR generado con éxito!")

            # Botón para descargar el QR
            with open(generated_qr, "rb") as file:
                st.download_button(label="Descargar QR", data=file, file_name=generated_qr.split("/")[-1])
            
        else:
            st.error("Error al generar el QR")

if __name__ == "__main__":
    main()
