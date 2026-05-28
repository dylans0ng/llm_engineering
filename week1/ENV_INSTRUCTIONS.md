How to store and test your OpenRouter API key

1. Copy `.env.example` to `.env` at the repository root and replace the placeholder:

   OPENROUTER_API_KEY=sk-...your key...

2. Make sure `.env` is listed in `.gitignore` (it's already ignored in this repository).

3. From your activated virtualenv run the test script:

```powershell
python tools/openrouter_test.py
```

This will list available models from `https://openrouter.ai/api/v1/models` so you can pick the exact model id (e.g. `kimi-k2.6` if the provider exposes it).

Security: Never commit `.env` to source control. If the key is leaked, delete/rotate it from OpenRouter dashboard.
