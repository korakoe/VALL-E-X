from vallex.utils.generation import SAMPLE_RATE, generate_audio, preload_models
from vallex.utils.prompt_making import make_prompt
from scipy.io.wavfile import write as write_wav

# download and load all models
model, codec, vocos = preload_models(download=True) # checkpoint_path=Whatever you want (CUSTOM MODEL GALORE)

make_prompt(name="paimon", audio_prompt_path="paimon_prompt.wav",
            transcript="Just, what was that? Paimon thought we were gonna get eaten.")

while True:
    audio_array = generate_audio(model, codec, vocos, input("what to say: "), prompt="paimon")
    write_wav("test1.wav", SAMPLE_RATE, audio_array)

