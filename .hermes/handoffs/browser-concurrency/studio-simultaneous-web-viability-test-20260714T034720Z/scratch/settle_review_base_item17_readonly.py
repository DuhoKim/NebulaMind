import json,sys
from pathlib import Path
from playwright.sync_api import sync_playwright
sys.path.insert(0,'scratch')
import run_review_base_item17 as m

state=json.loads(m.STATE_PATH.read_text())
if state.get('status') not in {'BROKER_CUSTODY_HOLD_EXTERNAL_FLOW_FREEZE','BROKER_CUSTODY_HOLD_EXTERNAL_LANE','TECHNICAL_OR_CUSTODY_HOLD'}:
    raise SystemExit(f'unexpected state before read-only settlement: {state.get("status")}')
if m.RAW_PACKET_PATH.exists() or m.RAW_METADATA_PATH.exists():
    raise SystemExit('raw custody artifact already exists; refuse duplicate settlement')
identity=state.get('paper',{}).get('identity')
if not identity or identity.get('conversation_id')!='0d8667dfd0db044c' or identity.get('conversation_path')!='/app/0d8667dfd0db044c':
    raise SystemExit(f'exact-owned identity mismatch: {identity}')
if state.get('paper',{}).get('research_start_utc')!='2026-07-16T06:17:56.507441Z':
    raise SystemExit('one-Start custody mismatch')

spec=m.spec()
adapted=m.q.adapted_state(state)
with sync_playwright() as playwright:
    browser=playwright.chromium.connect_over_cdp(m.r.BASE)
    record=m.r.target_record()
    if not record or record.get('path')!=identity['conversation_path']:
        raise m.r.TargetDrift(f'exact-owned #17 route is not current: {record}')
    # poll_terminal acquires a new target lease in read mode and performs no
    # prompt, Start, navigation, account submission, or deletion action.
    snapshot,result_sha=m.r.poll_terminal(identity,spec,adapted,browser)
    m.q.sync_state(state,adapted)
    metadata=m.save_packet(snapshot,result_sha,identity,spec,state)
    browser.close()
print(json.dumps({'status':state['status'],'conversation_id':identity['conversation_id'],'raw_packet':str(m.RAW_PACKET_PATH),'raw_packet_sha256':metadata['packet_sha256'],'output_shape_pass':metadata['output_quality']['pass'],'result_chars':metadata['result_chars'],'one_prompt':True,'one_start':True,'prompt_resent':False,'second_start':False},sort_keys=True))
