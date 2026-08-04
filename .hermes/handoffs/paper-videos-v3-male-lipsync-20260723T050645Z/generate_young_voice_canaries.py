#!/usr/bin/env python3
from __future__ import annotations
import asyncio, hashlib, json, re, subprocess, sys, uuid
from pathlib import Path
HERMES_ROOT=Path('/Users/duhokim/.hermes/hermes-agent'); sys.path.insert(0,str(HERMES_ROOT))
from tools.tts_tool import _import_openai_client, _resolve_openai_audio_client_config
import edge_tts
BASE=Path(__file__).resolve().parent; OUT=BASE/'voice_canaries_v3_young'; OUT.mkdir(parents=True,exist_ok=True)
TEXT=("Metallicity is a way to track how much oxygen is in a galaxy’s star-forming gas. "
      "This paper looks at five unlensed galaxies from redshift nine point three to nine point nine. "
      "Their direct temperature measurements show only about one fifth the oxygen abundance of nearby galaxies at the same stellar mass. "
      "The direction is robust, but the exact size still depends on calibration.")
INSTRUCTIONS=("Sound like a friendly male science YouTuber in his early thirties: smooth, relaxed, curious, and conversational. "
              "Speak directly to one viewer with light energy and connected phrasing. No gravel, no announcer voice, no dramatic pauses, "
              "no classroom lecturing, and no exaggerated emphasis. Keep technical words crisp and make the numbers flow naturally.")

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def probe(p): return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration,size:stream=codec_name,sample_rate,channels','-of','json',str(p)],text=True))
def normalize(raw,review): subprocess.run(['ffmpeg','-y','-v','error','-i',str(raw),'-af','loudnorm=I=-16:TP=-2:LRA=7','-ar','48000','-ac','1','-c:a','pcm_s16le',str(review)],check=True)
async def edge(name,voice,rate):
    raw=OUT/f'{name}_raw.mp3'; await edge_tts.Communicate(TEXT,voice=voice,rate=rate).save(str(raw)); return raw
async def main():
    words=len(re.findall(r"\b[\w'-]+\b",TEXT)); items=[]
    api_key,base_url,_=_resolve_openai_audio_client_config(); Client=_import_openai_client(); client=Client(api_key=api_key,base_url=base_url)
    try:
        raw=OUT/'ash_young_raw.wav'; review=OUT/'ash_young_review_16lufs.wav'
        response=client.audio.speech.create(model='gpt-4o-mini-tts',voice='ash',input=TEXT,instructions=INSTRUCTIONS,response_format='wav',speed=0.82,extra_headers={'x-idempotency-key':str(uuid.uuid4())}); response.stream_to_file(raw); normalize(raw,review)
        configs=[('ash_young','OpenAI via Nous managed audio gateway','ash',raw,review,{'speed':0.82,'instructions':INSTRUCTIONS})]
    finally: client.close()
    for name,voice,rate in [('brian_young','en-US-BrianNeural','-25%'),('andrew_young','en-US-AndrewNeural','-20%')]:
        raw=await edge(name,voice,rate); review=OUT/f'{name}_review_16lufs.wav'; normalize(raw,review); configs.append((name,'Microsoft Edge neural TTS',voice,raw,review,{'rate':rate}))
    for name,provider,voice,raw,review,settings in configs:
        p=probe(review); dur=float(p['format']['duration']); item={'id':name,'provider':provider,'voice':voice,'voice_presentation':'explicit male conversational candidate','settings':settings,'word_count':words,'duration_seconds':round(dur,3),'words_per_minute':round(words/dur*60,1),'review_path':str(review),'review_sha256':sha(review),'probe':p}; items.append(item); print(json.dumps(item),flush=True)
    (OUT/'receipt.json').write_text(json.dumps({'marker':'NEBULAMIND_V3_YOUNG_SMOOTH_MALE_CANARIES_COMPLETE','persona':'younger, smooth, conversational, friendly science YouTuber','text':TEXT,'items':items,'global_config_changed':False},indent=2)+'\n')
if __name__=='__main__': asyncio.run(main())
