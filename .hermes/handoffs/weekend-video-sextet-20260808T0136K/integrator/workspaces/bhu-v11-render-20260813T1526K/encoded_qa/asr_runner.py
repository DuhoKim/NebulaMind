from faster_whisper import WhisperModel
import json
import sys

model = WhisperModel(sys.argv[1], device="cpu", compute_type="int8")
out = []
for path in sys.argv[2:]:
    segments, info = model.transcribe(
        path,
        language="en",
        beam_size=5,
        vad_filter=True,
        condition_on_previous_text=False,
    )
    segments = list(segments)
    out.append({
        "path": path,
        "language": info.language,
        "probability": info.language_probability,
        "text": " ".join(segment.text.strip() for segment in segments).strip(),
        "segments": [
            {
                "start": segment.start,
                "end": segment.end,
                "text": segment.text.strip(),
                "avg_logprob": segment.avg_logprob,
                "no_speech_prob": segment.no_speech_prob,
            }
            for segment in segments
        ],
    })
print(json.dumps(out, ensure_ascii=False))
