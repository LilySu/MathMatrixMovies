with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
       write(temp_audio.name, rate, click_sound.astype(np.float32))
       self.add_sound(temp_audio.name, gain=-10)