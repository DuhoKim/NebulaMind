# Cloudflare Tunnel Setup

Cloudflare Tunnel lets you expose NebulaMind to the internet without opening ports on your router.

## Prerequisites

- A Cloudflare account with a domain
- `cloudflared` CLI installed: `brew install cloudflared` (macOS) or see [docs](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/)

## Setup

### 1. Authenticate

```bash
cloudflared tunnel login
```

### 2. Create a tunnel

```bash
cloudflared tunnel create nebulamind
```

### 3. Configure routes

Create `~/.cloudflared/config.yml`:

```yaml
tunnel: <TUNNEL_ID>
credentials-file: /Users/<you>/.cloudflared/<TUNNEL_ID>.json

ingress:
  - hostname: nebulamind.yourdomain.com
    service: http://localhost:3000
  - hostname: api.nebulamind.yourdomain.com
    service: http://localhost:8000
  - service: http_status:404
```

### 4. Add DNS records

```bash
cloudflared tunnel route dns nebulamind nebulamind.yourdomain.com
cloudflared tunnel route dns nebulamind api.nebulamind.yourdomain.com
```

### 5. Run the tunnel

```bash
cloudflared tunnel run nebulamind
```

The frontend will be available at `https://nebulamind.yourdomain.com` and the API at `https://api.nebulamind.yourdomain.com`.
