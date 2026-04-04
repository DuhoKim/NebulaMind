# NebulaMind Scripts

## 서비스 관리

```bash
# 모든 서비스 시작
./scripts/start.sh

# 모든 서비스 중지
./scripts/stop.sh

# 서비스 상태 확인
./scripts/status.sh
```

## Mac Studio 재부팅 자동시작 설정

LaunchAgent를 설치하면 Mac Studio 로그인 시 자동으로 서비스가 시작됩니다.

```bash
# 1. plist 파일 복사
cp ~/NebulaMind/scripts/com.nebulamind.services.plist \
   ~/Library/LaunchAgents/

# 2. 등록
launchctl load ~/Library/LaunchAgents/com.nebulamind.services.plist

# 3. 확인
launchctl list | grep nebulamind
```

## LaunchAgent 제거

```bash
launchctl unload ~/Library/LaunchAgents/com.nebulamind.services.plist
rm ~/Library/LaunchAgents/com.nebulamind.services.plist
```

## 로그 확인

```bash
tail -f ~/NebulaMind/logs/backend.log
tail -f ~/NebulaMind/logs/celery_worker.log
tail -f ~/NebulaMind/logs/frontend.log
tail -f ~/NebulaMind/logs/cloudflared.log
```

## 전제조건 (Mac Studio)

- Docker Desktop (자동시작 설정 권장)
- Node.js + npm
- Python venv at `backend/.venv`
- `cloudflared` CLI (`brew install cloudflare/cloudflare/cloudflared`)
- Cloudflare Tunnel `nebulamind` configured
