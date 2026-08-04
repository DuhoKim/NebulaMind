#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,re,subprocess,sys,uuid
from pathlib import Path
ROOT=Path('/Users/duhokim/.hermes/hermes-agent');sys.path.insert(0,str(ROOT))
from tools.tts_tool import _import_openai_client,_resolve_openai_audio_client_config
BASE=Path(__file__).resolve().parent;OUT=BASE/'voice_canaries_v4_clear';OUT.mkdir(parents=True,exist_ok=True)
TEXT=("Metallicity is a way to track how much oxygen is in a galaxy’s star-forming gas. "
"This paper looks at five unlensed galaxies from redshift nine point three to nine point nine. "
"Their direct temperature measurements show only about one fifth the oxygen abundance of nearby galaxies at the same stellar mass. "
"The direction is robust, but the exact size still depends on calibration.")
INSTRUCTIONS=("You are a friendly male science creator in his late twenties recording in a professional quiet studio. "
"Use a clear, bright, smooth voice with clean consonants and natural conversational energy. Keep the microphone sound close and detailed. "
"Avoid grit, rasp, breathiness, low rumble, announcer bass, theatrical emphasis, and long dramatic pauses. "
"Speak to one curious viewer, connect phrases naturally, and pronounce every scientific term and number precisely.")
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def probe(p):return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration,size:stream=codec_name,sample_rate,channels,bits_per_sample','-of','json',str(p)],text=True))
def main():
 key,url,_=_resolve_openai_audio_client_config();Client=_import_openai_client();client=Client(api_key=key,base_url=url)
 raw=OUT/'ash_clear_native.wav';review=OUT/'ash_clear_review_16lufs.wav'
 try:
  r=client.audio.speech.create(model='gpt-4o-mini-tts',voice='ash',input=TEXT,instructions=INSTRUCTIONS,response_format='wav',speed=0.84,extra_headers={'x-idempotency-key':str(uuid.uuid4())});r.stream_to_file(raw)
 finally:client.close()
 subprocess.run(['ffmpeg','-y','-v','error','-i',str(raw),'-af','highpass=f=70,loudnorm=I=-16:TP=-2:LRA=7','-ar','48000','-ac','1','-c:a','pcm_s24le',str(review)],check=True)
 p=probe(review);dur=float(p['format']['duration']);words=len(re.findall(r"\b[\w'-]+\b",TEXT))
 receipt={'marker':'NEBULAMIND_V3_CLEAR_YOUNG_MALE_VOICE_CANARY','provider':'OpenAI via Nous managed audio gateway','model':'gpt-4o-mini-tts','voice':'ash','speed':0.84,'instructions':INSTRUCTIONS,'text':TEXT,'word_count':words,'duration_seconds':round(dur,3),'words_per_minute':round(words/dur*60,1),'native_path':str(raw),'native_sha256':sha(raw),'review_path':str(review),'review_sha256':sha(review),'probe':p,'source_codec_policy':'native model WAV to 24-bit PCM review master; no lossy intermediate'}
 (OUT/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
