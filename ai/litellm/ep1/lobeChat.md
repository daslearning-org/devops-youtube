# Sample ChatBot using LobeChat
You may visit their [official website](https://lobehub.com/docs/self-hosting/start)

## Docker Run
```bash
docker run -d -p 3210:3210 -e OLLAMA_PROXY_URL=http://localhost:11434 --name lobechat lobehub/lobe-chat
```