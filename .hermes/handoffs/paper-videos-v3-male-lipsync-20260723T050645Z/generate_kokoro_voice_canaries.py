#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,re,subprocess
from pathlib import Path
import soundfile as sf
from kokoro_onnx import Kokoro
TOOL=Path('/Users/duhokim/HermesOps/tools/kokoro-onnx')
BASE=Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v3-male-lipsync-20260723T050645Z')
OUT=BASE/'voice_canaries_v5_kokoro';OUT.mkdir(parents=True,exist_ok=True)
TEXT=("Metallicity tracks how much oxygen is in a galaxy's star-forming gas. "
"This paper studies five unlensed galaxies between redshift nine point three and nine point nine. "
"Direct temperature measurements find only about one fifth the oxygen abundance of nearby galaxies with the same stellar mass. "
"That shortfall is robust, although its exact size still depends on calibration.")
VOICES=['am_michael','am_adam','am_onyx']
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def probe(p):return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration,size:stream=codec_name,sample_rate,channels,bits_per_sample','-of','json',str(p)],text=True))
def main():
 engine=Kokoro(str(TOOL/'kokoro-v1.0.onnx'),str(TOOL/'voices-v1.0.bin'))
 words=len(re.findall(r"\b[\w'-]+\b",TEXT));items=[]
 for voice in VOICES:
  samples,sr=engine.create(TEXT,voice=voice,speed=1.0,lang='en-us')
  raw=OUT/f'{voice}_native.wav';review=OUT/f'{voice}_review_16lufs.wav';sf.write(raw,samples,sr,subtype='PCM_24')
  subprocess.run(['ffmpeg','-y','-v','error','-i',str(raw),'-af','highpass=f=65,loudnorm=I=-16:TP=-2:LRA=7','-ar','48000','-ac','1','-c:a','pcm_s24le',str(review)],check=True)
  p=probe(review);dur=float(p['format']['duration']);item={'id':voice,'provider':'local Kokoro-82M v1.0 ONNX','voice':voice,'catalog_presentation':'American male','model_speed':1.0,'word_count':words,'duration_seconds':round(dur,3),'words_per_minute':round(words/dur*60,1),'native_path':str(raw),'native_sha256':sha(raw),'review_path':str(review),'review_sha256':sha(review),'probe':p};items.append(item);print(json.dumps(item),flush=True)
 (OUT/'receipt_native_speed.json').write_text(json.dumps({'marker':'NEBULAMIND_V3_KOKORO_MALE_NATIVE_SPEED_CANARIES','text':TEXT,'items':items,'source_codec_policy':'local float inference to native 24-bit PCM; no lossy intermediate','public_mutation':False},indent=2)+'\n')
if __name__=='__main__':main()
