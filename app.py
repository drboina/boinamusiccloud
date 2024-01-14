import io
import os
import wave
import numpy as np
import streamlit as st

AUDIO_EXTENSIONS = ["mp3"]

st.image("logo_chico.png")

st.header("Mix Recordings")

def get_audio_files_in_dir(directory):
    out = []
    for item in os.listdir(directory):
        try:
            name, ext = item.split(".")
        except:
            continue
        if name and ext:
            if ext in AUDIO_EXTENSIONS:
                out.append(item)
    return out

avdir = os.path.expanduser("//Users/boinas/Documents/boinamusiccloud/boinas/")
audiofiles = get_audio_files_in_dir(avdir)

if len(audiofiles) == 0:
    st.write("No hay archivos")

else:
    filename = st.selectbox(
        "Play it!",
        audiofiles,
        0,
    )
    audiopath = os.path.join(avdir, filename)
    st.audio(audiopath)
