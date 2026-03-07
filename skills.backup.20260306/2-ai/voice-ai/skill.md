---
name: voice-ai
description: Consolidated master domain for voice ai.
---

# VOICE-AI



## voice / SKILL.md

---
name: voice-ai-development
description: "Expert in building voice AI applications - from real-time voice agents to voice-enabled apps. Covers OpenAI Realtime API, Vapi for voice agents, Deepgram for transcription, ElevenLabs for synthesis, LiveKit for real-time infrastructure, and WebRTC fundamentals. Knows how to build low-latency, production-ready voice experiences. Use when: voice ai, voice agent, speech to text, text to speech, realtime voice."
source: vibeship-spawner-skills (Apache 2.0)
---

# Voice AI Development

**Role**: Voice AI Architect

You are an expert in building real-time voice applications. You think in terms of
latency budgets, audio quality, and user experience. You know that voice apps feel
magical when fast and broken when slow. You choose the right combination of providers
for each use case and optimize relentlessly for perceived responsiveness.

## Capabilities

- OpenAI Realtime API
- Vapi voice agents
- Deepgram STT/TTS
- ElevenLabs voice synthesis
- LiveKit real-time infrastructure
- WebRTC audio handling
- Voice agent design
- Latency optimization

## Requirements

- Python or Node.js
- API keys for providers
- Audio handling knowledge

## Patterns

### OpenAI Realtime API

Native voice-to-voice with GPT-4o

**When to use**: When you want integrated voice AI without separate STT/TTS

```python
import asyncio
import websockets
import json
import base64

OPENAI_API_KEY = "sk-..."

async def voice_session():
    url = "wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "OpenAI-Beta": "realtime=v1"
    }

    async with websockets.connect(url, extra_headers=headers) as ws:
        # Configure session
        await ws.send(json.dumps({
            "type": "session.update",
            "session": {
                "modalities": ["text", "audio"],
                "voice": "alloy",  # alloy, echo, fable, onyx, nova, shimmer
                "input_audio_format": "pcm16",
                "output_audio_format": "pcm16",
                "input_audio_transcription": {
                    "model": "whisper-1"
                },
                "turn_detection": {
                    "type": "server_vad",  # Voice activity detection
                    "threshold": 0.5,
                    "prefix_padding_ms": 300,
                    "silence_duration_ms": 500
                },
                "tools": [
                    {
                        "type": "function",
                        "name": "get_weather",
                        "description": "Get weather for a location",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {"type": "string"}
                            }
                        }
                    }
                ]
            }
        }))

        # Send audio (PCM16, 24kHz, mono)
        async def send_audio(audio_bytes):
            await ws.send(json.dumps({
                "type": "input_audio_buffer.append",
                "audio": base64.b64encode(audio_bytes).decode()
            }))

        # Receive events
        async for message in ws:
            event = json.loads(message)

            if event["type"] == "resp
```

### Vapi Voice Agent

Build voice agents with Vapi platform

**When to use**: Phone-based agents, quick deployment

```python
# Vapi provides hosted voice agents with webhooks

from flask import Flask, request, jsonify
import vapi

app = Flask(__name__)
client = vapi.Vapi(api_key="...")

# Create an assistant
assistant = client.assistants.create(
    name="Support Agent",
    model={
        "provider": "openai",
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful support agent..."
            }
        ]
    },
    voice={
        "provider": "11labs",
        "voiceId": "21m00Tcm4TlvDq8ikWAM"  # Rachel
    },
    firstMessage="Hi! How can I help you today?",
    transcriber={
        "provider": "deepgram",
        "model": "nova-2"
    }
)

# Webhook for conversation events
@app.route("/vapi/webhook", methods=["POST"])
def vapi_webhook():
    event = request.json

    if event["type"] == "function-call":
        # Handle tool call
        name = event["functionCall"]["name"]
        args = event["functionCall"]["parameters"]

        if name == "check_order":
            result = check_order(args["order_id"])
            return jsonify({"result": result})

    elif event["type"] == "end-of-call-report":
        # Call ended - save transcript
        transcript = event["transcript"]
        save_transcript(event["call"]["id"], transcript)

    return jsonify({"ok": True})

# Start outbound call
call = client.calls.create(
    assistant_id=assistant.id,
    customer={
        "number": "+1234567890"
    },
    phoneNumber={
        "twilioPhoneNumber": "+0987654321"
    }
)

# Or create web call
web_call = client.calls.create(
    assistant_id=assistant.id,
    type="web"
)
# Returns URL for WebRTC connection
```

### Deepgram STT + ElevenLabs TTS

Best-in-class transcription and synthesis

**When to use**: High quality voice, custom pipeline

```python
import asyncio
from deepgram import DeepgramClient, LiveTranscriptionEvents
from elevenlabs import ElevenLabs

# Deepgram real-time transcription
deepgram = DeepgramClient(api_key="...")

async def transcribe_stream(audio_stream):
    connection = deepgram.listen.live.v("1")

    async def on_transcript(result):
        transcript = result.channel.alternatives[0].transcript
        if transcript:
            print(f"Heard: {transcript}")
            if result.is_final:
                # Process final transcript
                await handle_user_input(transcript)

    connection.on(LiveTranscriptionEvents.Transcript, on_transcript)

    await connection.start({
        "model": "nova-2",  # Best quality
        "language": "en",
        "smart_format": True,
        "interim_results": True,  # Get partial results
        "utterance_end_ms": 1000,
        "vad_events": True,  # Voice activity detection
        "encoding": "linear16",
        "sample_rate": 16000
    })

    # Stream audio
    async for chunk in audio_stream:
        await connection.send(chunk)

    await connection.finish()

# ElevenLabs streaming synthesis
eleven = ElevenLabs(api_key="...")

def text_to_speech_stream(text: str):
    """Stream TTS audio chunks."""
    audio_stream = eleven.text_to_speech.convert_as_stream(
        voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel
        model_id="eleven_turbo_v2_5",  # Fastest
        text=text,
        output_format="pcm_24000"  # Raw PCM for low latency
    )

    for chunk in audio_stream:
        yield chunk

# Or with WebSocket for lowest latency
async def tts_websocket(text_stream):
    async with eleven.text_to_speech.stream_async(
        voice_id="21m00Tcm4TlvDq8ikWAM",
        model_id="eleven_turbo_v2_5"
    ) as tts:
        async for text_chunk in text_stream:
            audio = await tts.send(text_chunk)
            yield audio

        # Flush remaining audio
        final_audio = await tts.flush()
        yield final_audio
```

## Anti-Patterns

### ❌ Non-streaming Pipeline

**Why bad**: Adds seconds of latency.
User perceives as slow.
Loses conversation flow.

**Instead**: Stream everything:
- STT: interim results
- LLM: token streaming
- TTS: chunk streaming
Start TTS before LLM finishes.

### ❌ Ignoring Interruptions

**Why bad**: Frustrating user experience.
Feels like talking to a machine.
Wastes time.

**Instead**: Implement barge-in detection.
Use VAD to detect user speech.
Stop TTS immediately.
Clear audio queue.

### ❌ Single Provider Lock-in

**Why bad**: May not be best quality.
Single point of failure.
Harder to optimize.

**Instead**: Mix best providers:
- Deepgram for STT (speed + accuracy)
- ElevenLabs for TTS (voice quality)
- OpenAI/Anthropic for LLM

## Limitations

- Latency varies by provider
- Cost per minute adds up
- Quality depends on network
- Complex debugging

## Related Skills

Works well with: `langgraph`, `structured-output`, `langfuse`


## voice / SKILL.md

---
name: voice-agents
description: "Voice agents represent the frontier of AI interaction - humans speaking naturally with AI systems. The challenge isn't just speech recognition and synthesis, it's achieving natural conversation flow with sub-800ms latency while handling interruptions, background noise, and emotional nuance.  This skill covers two architectures: speech-to-speech (OpenAI Realtime API, lowest latency, most natural) and pipeline (STT→LLM→TTS, more control, easier to debug). Key insight: latency is the constraint. Hu"
source: vibeship-spawner-skills (Apache 2.0)
---

# Voice Agents

You are a voice AI architect who has shipped production voice agents handling
millions of calls. You understand the physics of latency - every component
adds milliseconds, and the sum determines whether conversations feel natural
or awkward.

Your core insight: Two architectures exist. Speech-to-speech (S2S) models like
OpenAI Realtime API preserve emotion and achieve lowest latency but are less
controllable. Pipeline architectures (STT→LLM→TTS) give you control at each
step but add latency. Mos

## Capabilities

- voice-agents
- speech-to-speech
- speech-to-text
- text-to-speech
- conversational-ai
- voice-activity-detection
- turn-taking
- barge-in-detection
- voice-interfaces

## Patterns

### Speech-to-Speech Architecture

Direct audio-to-audio processing for lowest latency

### Pipeline Architecture

Separate STT → LLM → TTS for maximum control

### Voice Activity Detection Pattern

Detect when user starts/stops speaking

## Anti-Patterns

### ❌ Ignoring Latency Budget

### ❌ Silence-Only Turn Detection

### ❌ Long Responses

## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Issue | critical | # Measure and budget latency for each component: |
| Issue | high | # Target jitter metrics: |
| Issue | high | # Use semantic VAD: |
| Issue | high | # Implement barge-in detection: |
| Issue | medium | # Constrain response length in prompts: |
| Issue | medium | # Prompt for spoken format: |
| Issue | medium | # Implement noise handling: |
| Issue | medium | # Mitigate STT errors: |

## Related Skills

Works well with: `agent-tool-builder`, `multi-agent-orchestration`, `llm-architect`, `backend`


## voice-agents / SKILL.md

---
name: voice-agents
description: "Voice agents represent the frontier of AI interaction - humans speaking naturally with AI systems. The challenge isn't just speech recognition and synthesis, it's achieving natural conversation flow with sub-800ms latency while handling interruptions, background noise, and emotional nuance.  This skill covers two architectures: speech-to-speech (OpenAI Realtime API, lowest latency, most natural) and pipeline (STT→LLM→TTS, more control, easier to debug). Key insight: latency is the constraint. Hu"
source: vibeship-spawner-skills (Apache 2.0)
---

# Voice Agents

You are a voice AI architect who has shipped production voice agents handling
millions of calls. You understand the physics of latency - every component
adds milliseconds, and the sum determines whether conversations feel natural
or awkward.

Your core insight: Two architectures exist. Speech-to-speech (S2S) models like
OpenAI Realtime API preserve emotion and achieve lowest latency but are less
controllable. Pipeline architectures (STT→LLM→TTS) give you control at each
step but add latency. Mos

## Capabilities

- voice-agents
- speech-to-speech
- speech-to-text
- text-to-speech
- conversational-ai
- voice-activity-detection
- turn-taking
- barge-in-detection
- voice-interfaces

## Patterns

### Speech-to-Speech Architecture

Direct audio-to-audio processing for lowest latency

### Pipeline Architecture

Separate STT → LLM → TTS for maximum control

### Voice Activity Detection Pattern

Detect when user starts/stops speaking

## Anti-Patterns

### ❌ Ignoring Latency Budget

### ❌ Silence-Only Turn Detection

### ❌ Long Responses

## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Issue | critical | # Measure and budget latency for each component: |
| Issue | high | # Target jitter metrics: |
| Issue | high | # Use semantic VAD: |
| Issue | high | # Implement barge-in detection: |
| Issue | medium | # Constrain response length in prompts: |
| Issue | medium | # Prompt for spoken format: |
| Issue | medium | # Implement noise handling: |
| Issue | medium | # Mitigate STT errors: |

## Related Skills

Works well with: `agent-tool-builder`, `multi-agent-orchestration`, `llm-architect`, `backend`


## voice-ai-dev / SKILL.md

---
name: voice-ai-dev
description: "Expert in building voice AI applications - from real-time voice agents to voice-enabled apps. Covers OpenAI Realtime API, Vapi for voice agents, Deepgram for transcription, ElevenLabs for synthesis, LiveKit for real-time infrastructure, and WebRTC fundamentals. Knows how to build low-latency, production-ready voice experiences. Use when: voice ai, voice agent, speech to text, text to speech, realtime voice."
source: vibeship-spawner-skills (Apache 2.0)
---

# Voice AI Development

**Role**: Voice AI Architect

You are an expert in building real-time voice applications. You think in terms of
latency budgets, audio quality, and user experience. You know that voice apps feel
magical when fast and broken when slow. You choose the right combination of providers
for each use case and optimize relentlessly for perceived responsiveness.

## Capabilities

- OpenAI Realtime API
- Vapi voice agents
- Deepgram STT/TTS
- ElevenLabs voice synthesis
- LiveKit real-time infrastructure
- WebRTC audio handling
- Voice agent design
- Latency optimization

## Requirements

- Python or Node.js
- API keys for providers
- Audio handling knowledge

## Patterns

### OpenAI Realtime API

Native voice-to-voice with GPT-4o

**When to use**: When you want integrated voice AI without separate STT/TTS

```python
import asyncio
import websockets
import json
import base64

OPENAI_API_KEY = "sk-..."

async def voice_session():
    url = "wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "OpenAI-Beta": "realtime=v1"
    }

    async with websockets.connect(url, extra_headers=headers) as ws:
        # Configure session
        await ws.send(json.dumps({
            "type": "session.update",
            "session": {
                "modalities": ["text", "audio"],
                "voice": "alloy",  # alloy, echo, fable, onyx, nova, shimmer
                "input_audio_format": "pcm16",
                "output_audio_format": "pcm16",
                "input_audio_transcription": {
                    "model": "whisper-1"
                },
                "turn_detection": {
                    "type": "server_vad",  # Voice activity detection
                    "threshold": 0.5,
                    "prefix_padding_ms": 300,
                    "silence_duration_ms": 500
                },
                "tools": [
                    {
                        "type": "function",
                        "name": "get_weather",
                        "description": "Get weather for a location",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {"type": "string"}
                            }
                        }
                    }
                ]
            }
        }))

        # Send audio (PCM16, 24kHz, mono)
        async def send_audio(audio_bytes):
            await ws.send(json.dumps({
                "type": "input_audio_buffer.append",
                "audio": base64.b64encode(audio_bytes).decode()
            }))

        # Receive events
        async for message in ws:
            event = json.loads(message)

            if event["type"] == "resp
```

### Vapi Voice Agent

Build voice agents with Vapi platform

**When to use**: Phone-based agents, quick deployment

```python
# Vapi provides hosted voice agents with webhooks

from flask import Flask, request, jsonify
import vapi

app = Flask(__name__)
client = vapi.Vapi(api_key="...")

# Create an assistant
assistant = client.assistants.create(
    name="Support Agent",
    model={
        "provider": "openai",
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful support agent..."
            }
        ]
    },
    voice={
        "provider": "11labs",
        "voiceId": "21m00Tcm4TlvDq8ikWAM"  # Rachel
    },
    firstMessage="Hi! How can I help you today?",
    transcriber={
        "provider": "deepgram",
        "model": "nova-2"
    }
)

# Webhook for conversation events
@app.route("/vapi/webhook", methods=["POST"])
def vapi_webhook():
    event = request.json

    if event["type"] == "function-call":
        # Handle tool call
        name = event["functionCall"]["name"]
        args = event["functionCall"]["parameters"]

        if name == "check_order":
            result = check_order(args["order_id"])
            return jsonify({"result": result})

    elif event["type"] == "end-of-call-report":
        # Call ended - save transcript
        transcript = event["transcript"]
        save_transcript(event["call"]["id"], transcript)

    return jsonify({"ok": True})

# Start outbound call
call = client.calls.create(
    assistant_id=assistant.id,
    customer={
        "number": "+1234567890"
    },
    phoneNumber={
        "twilioPhoneNumber": "+0987654321"
    }
)

# Or create web call
web_call = client.calls.create(
    assistant_id=assistant.id,
    type="web"
)
# Returns URL for WebRTC connection
```

### Deepgram STT + ElevenLabs TTS

Best-in-class transcription and synthesis

**When to use**: High quality voice, custom pipeline

```python
import asyncio
from deepgram import DeepgramClient, LiveTranscriptionEvents
from elevenlabs import ElevenLabs

# Deepgram real-time transcription
deepgram = DeepgramClient(api_key="...")

async def transcribe_stream(audio_stream):
    connection = deepgram.listen.live.v("1")

    async def on_transcript(result):
        transcript = result.channel.alternatives[0].transcript
        if transcript:
            print(f"Heard: {transcript}")
            if result.is_final:
                # Process final transcript
                await handle_user_input(transcript)

    connection.on(LiveTranscriptionEvents.Transcript, on_transcript)

    await connection.start({
        "model": "nova-2",  # Best quality
        "language": "en",
        "smart_format": True,
        "interim_results": True,  # Get partial results
        "utterance_end_ms": 1000,
        "vad_events": True,  # Voice activity detection
        "encoding": "linear16",
        "sample_rate": 16000
    })

    # Stream audio
    async for chunk in audio_stream:
        await connection.send(chunk)

    await connection.finish()

# ElevenLabs streaming synthesis
eleven = ElevenLabs(api_key="...")

def text_to_speech_stream(text: str):
    """Stream TTS audio chunks."""
    audio_stream = eleven.text_to_speech.convert_as_stream(
        voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel
        model_id="eleven_turbo_v2_5",  # Fastest
        text=text,
        output_format="pcm_24000"  # Raw PCM for low latency
    )

    for chunk in audio_stream:
        yield chunk

# Or with WebSocket for lowest latency
async def tts_websocket(text_stream):
    async with eleven.text_to_speech.stream_async(
        voice_id="21m00Tcm4TlvDq8ikWAM",
        model_id="eleven_turbo_v2_5"
    ) as tts:
        async for text_chunk in text_stream:
            audio = await tts.send(text_chunk)
            yield audio

        # Flush remaining audio
        final_audio = await tts.flush()
        yield final_audio
```

## Anti-Patterns

### ❌ Non-streaming Pipeline

**Why bad**: Adds seconds of latency.
User perceives as slow.
Loses conversation flow.

**Instead**: Stream everything:
- STT: interim results
- LLM: token streaming
- TTS: chunk streaming
Start TTS before LLM finishes.

### ❌ Ignoring Interruptions

**Why bad**: Frustrating user experience.
Feels like talking to a machine.
Wastes time.

**Instead**: Implement barge-in detection.
Use VAD to detect user speech.
Stop TTS immediately.
Clear audio queue.

### ❌ Single Provider Lock-in

**Why bad**: May not be best quality.
Single point of failure.
Harder to optimize.

**Instead**: Mix best providers:
- Deepgram for STT (speed + accuracy)
- ElevenLabs for TTS (voice quality)
- OpenAI/Anthropic for LLM

## Limitations

- Latency varies by provider
- Cost per minute adds up
- Quality depends on network
- Complex debugging

## Related Skills

Works well with: `langgraph`, `structured-output`, `langfuse`


## voice-engine / README.md

# Voice AI Engine Development Skill

Build production-ready real-time conversational AI voice engines with async worker pipelines, streaming transcription, LLM agents, and TTS synthesis.

## Overview

This skill provides comprehensive guidance for building voice AI engines that enable natural, bidirectional conversations between users and AI agents. It covers the complete architecture from audio input to audio output, including:

- **Async Worker Pipeline Pattern** - Concurrent processing with queue-based communication
- **Streaming Transcription** - Real-time speech-to-text conversion
- **LLM-Powered Agents** - Conversational AI with context awareness
- **Text-to-Speech Synthesis** - Natural voice generation
- **Interrupt Handling** - Users can interrupt the bot mid-sentence
- **Multi-Provider Support** - Swap between different service providers easily

## Quick Start

```python
# Use the skill in your AI assistant
@voice-ai-engine-development I need to build a voice assistant that can handle real-time conversations with interrupts
```

## What's Included

### Main Skill File
- `SKILL.md` - Comprehensive guide to voice AI engine development

### Examples
- `complete_voice_engine.py` - Full working implementation
- `gemini_agent_example.py` - LLM agent with proper response buffering
- `interrupt_system_example.py` - Interrupt handling demonstration

### Templates
- `base_worker_template.py` - Template for creating new workers
- `multi_provider_factory_template.py` - Multi-provider factory pattern

### References
- `common_pitfalls.md` - Common issues and solutions
- `provider_comparison.md` - Comparison of transcription, LLM, and TTS providers

## Key Concepts

### The Worker Pipeline Pattern

Every voice AI engine follows this pipeline:

```
Audio In → Transcriber → Agent → Synthesizer → Audio Out
           (Worker 1)   (Worker 2)  (Worker 3)
```

Each worker:
- Runs independently via asyncio
- Communicates through asyncio.Queue objects
- Can be stopped mid-stream for interrupts
- Handles errors gracefully

### Critical Implementation Details

1. **Buffer LLM Responses** - Always buffer the entire LLM response before sending to synthesizer to prevent audio jumping
2. **Mute Transcriber** - Mute the transcriber when bot speaks to prevent echo/feedback loops
3. **Rate-Limit Audio** - Send audio chunks at real-time speed to enable interrupts
4. **Proper Cleanup** - Always cleanup resources in finally blocks to prevent memory leaks

## Supported Providers

### Transcription
- Deepgram (fastest, best for real-time)
- AssemblyAI (highest accuracy)
- Azure Speech (enterprise-grade)
- Google Cloud Speech (multi-language)

### LLM
- OpenAI GPT-4 (highest quality)
- Google Gemini (cost-effective)
- Anthropic Claude (safety-focused)

### TTS
- ElevenLabs (most natural voices)
- Azure TTS (enterprise-grade)
- Google Cloud TTS (cost-effective)
- Amazon Polly (AWS integration)
- Play.ht (voice cloning)

## Common Use Cases

- Customer service voice bots
- Voice assistants
- Phone automation systems
- Voice-enabled applications
- Interactive voice response (IVR) systems
- Voice-based tutoring systems

## Architecture Highlights

### Async Worker Pattern
```python
class BaseWorker:
    async def _run_loop(self):
        while self.active:
            item = await self.input_queue.get()
            await self.process(item)
```

### Interrupt System
```python
# User interrupts bot mid-sentence
if stop_event.is_set():
    partial_message = get_message_up_to(seconds_spoken)
    return partial_message, True  # cut_off = True
```

### Multi-Provider Factory
```python
factory = VoiceComponentFactory()
transcriber = factory.create_transcriber(config)  # Deepgram, AssemblyAI, etc.
agent = factory.create_agent(config)              # OpenAI, Gemini, etc.
synthesizer = factory.create_synthesizer(config)  # ElevenLabs, Azure, etc.
```

## Testing

The skill includes examples for:
- Unit testing workers in isolation
- Integration testing the full pipeline
- Testing interrupt functionality
- Testing with different providers

## Best Practices

1. ✅ Always stream at every stage (transcription, LLM, synthesis)
2. ✅ Buffer entire LLM responses before synthesis
3. ✅ Mute transcriber during bot speech
4. ✅ Rate-limit audio chunks for interrupts
5. ✅ Maintain conversation history for context
6. ✅ Use proper error handling in worker loops
7. ✅ Cleanup resources in finally blocks
8. ✅ Use LINEAR16 PCM at 16kHz for audio

## Common Pitfalls

See `references/common_pitfalls.md` for detailed solutions to:
- Audio jumping/cutting off
- Echo/feedback loops
- Interrupts not working
- Memory leaks
- Lost conversation context
- High latency
- Poor audio quality

## Contributing

This skill is part of the  repository. Contributions are welcome!

## Related Skills

- `@websocket-patterns` - WebSocket implementation
- `@async-python` - Asyncio patterns
- `@streaming-apis` - Streaming API integration
- `@audio-processing` - Audio format conversion

## License

MIT License - See repository LICENSE file

## Resources

- [Vocode Documentation](https://docs.vocode.dev/)
- [Deepgram API](https://developers.deepgram.com/)
- [OpenAI API](https://platform.openai.com/docs/)
- [ElevenLabs API](https://elevenlabs.io/docs/)

---

**Built with ❤️ for the Antigravity community**


## voice-engine / SKILL.md

---
name: voice-engine
description: "Build real-time conversational AI voice engines using async worker pipelines, streaming transcription, LLM agents, and TTS synthesis with interrupt handling and multi-provider support"
---

# Voice AI Engine Development

## Overview

This skill guides you through building production-ready voice AI engines with real-time conversation capabilities. Voice AI engines enable natural, bidirectional conversations between users and AI agents through streaming audio processing, speech-to-text transcription, LLM-powered responses, and text-to-speech synthesis.

The core architecture uses an async queue-based worker pipeline where each component runs independently and communicates via `asyncio.Queue` objects, enabling concurrent processing, interrupt handling, and real-time streaming at every stage.

## When to Use This Skill

Use this skill when:
- Building real-time voice conversation systems
- Implementing voice assistants or chatbots
- Creating voice-enabled customer service agents
- Developing voice AI applications with interrupt capabilities
- Integrating multiple transcription, LLM, or TTS providers
- Working with streaming audio processing pipelines
- The user mentions Vocode, voice engines, or conversational AI

## Core Architecture Principles

### The Worker Pipeline Pattern

Every voice AI engine follows this pipeline:

```
Audio In → Transcriber → Agent → Synthesizer → Audio Out
           (Worker 1)   (Worker 2)  (Worker 3)
```

**Key Benefits:**
- **Decoupling**: Workers only know about their input/output queues
- **Concurrency**: All workers run simultaneously via asyncio
- **Backpressure**: Queues automatically handle rate differences
- **Interruptibility**: Everything can be stopped mid-stream

### Base Worker Pattern

Every worker follows this pattern:

```python
class BaseWorker:
    def __init__(self, input_queue, output_queue):
        self.input_queue = input_queue   # asyncio.Queue to consume from
        self.output_queue = output_queue # asyncio.Queue to produce to
        self.active = False
    
    def start(self):
        """Start the worker's processing loop"""
        self.active = True
        asyncio.create_task(self._run_loop())
    
    async def _run_loop(self):
        """Main processing loop - runs forever until terminated"""
        while self.active:
            item = await self.input_queue.get()  # Block until item arrives
            await self.process(item)              # Process the item
    
    async def process(self, item):
        """Override this - does the actual work"""
        raise NotImplementedError
    
    def terminate(self):
        """Stop the worker"""
        self.active = False
```

## Component Implementation Guide

### 1. Transcriber (Audio → Text)

**Purpose**: Converts incoming audio chunks to text transcriptions

**Interface Requirements**:
```python
class BaseTranscriber:
    def __init__(self, transcriber_config):
        self.input_queue = asyncio.Queue()   # Audio chunks (bytes)
        self.output_queue = asyncio.Queue()  # Transcriptions
        self.is_muted = False
    
    def send_audio(self, chunk: bytes):
        """Client calls this to send audio"""
        if not self.is_muted:
            self.input_queue.put_nowait(chunk)
        else:
            # Send silence instead (prevents echo during bot speech)
            self.input_queue.put_nowait(self.create_silent_chunk(len(chunk)))
    
    def mute(self):
        """Called when bot starts speaking (prevents echo)"""
        self.is_muted = True
    
    def unmute(self):
        """Called when bot stops speaking"""
        self.is_muted = False
```

**Output Format**:
```python
class Transcription:
    message: str          # "Hello, how are you?"
    confidence: float     # 0.95
    is_final: bool        # True = complete sentence, False = partial
    is_interrupt: bool    # Set by TranscriptionsWorker
```

**Supported Providers**:
- **Deepgram** - Fast, accurate, streaming
- **AssemblyAI** - High accuracy, good for accents
- **Azure Speech** - Enterprise-grade
- **Google Cloud Speech** - Multi-language support

**Critical Implementation Details**:
- Use WebSocket for bidirectional streaming
- Run sender and receiver tasks concurrently with `asyncio.gather()`
- Mute transcriber when bot speaks to prevent echo/feedback loops
- Handle both final and partial transcriptions

### 2. Agent (Text → Response)

**Purpose**: Processes user input and generates conversational responses

**Interface Requirements**:
```python
class BaseAgent:
    def __init__(self, agent_config):
        self.input_queue = asyncio.Queue()   # TranscriptionAgentInput
        self.output_queue = asyncio.Queue()  # AgentResponse
        self.transcript = None               # Conversation history
    
    async def generate_response(self, human_input, is_interrupt, conversation_id):
        """Override this - returns AsyncGenerator of responses"""
        raise NotImplementedError
```

**Why Streaming Responses?**
- **Lower latency**: Start speaking as soon as first sentence is ready
- **Better interrupts**: Can stop mid-response
- **Sentence-by-sentence**: More natural conversation flow

**Supported Providers**:
- **OpenAI** (GPT-4, GPT-3.5) - High quality, fast
- **Google Gemini** - Multimodal, cost-effective
- **Anthropic Claude** - Long context, nuanced responses

**Critical Implementation Details**:
- Maintain conversation history in `Transcript` object
- Stream responses using `AsyncGenerator`
- **IMPORTANT**: Buffer entire LLM response before yielding to synthesizer (prevents audio jumping)
- Handle interrupts by canceling current generation task
- Update conversation history with partial messages on interrupt

### 3. Synthesizer (Text → Audio)

**Purpose**: Converts agent text responses to speech audio

**Interface Requirements**:
```python
class BaseSynthesizer:
    async def create_speech(self, message: BaseMessage, chunk_size: int) -> SynthesisResult:
        """
        Returns a SynthesisResult containing:
        - chunk_generator: AsyncGenerator that yields audio chunks
        - get_message_up_to: Function to get partial text (for interrupts)
        """
        raise NotImplementedError
```

**SynthesisResult Structure**:
```python
class SynthesisResult:
    chunk_generator: AsyncGenerator[ChunkResult, None]
    get_message_up_to: Callable[[float], str]  # seconds → partial text
    
    class ChunkResult:
        chunk: bytes          # Raw PCM audio
        is_last_chunk: bool
```

**Supported Providers**:
- **ElevenLabs** - Most natural voices, streaming
- **Azure TTS** - Enterprise-grade, many languages
- **Google Cloud TTS** - Cost-effective, good quality
- **Amazon Polly** - AWS integration
- **Play.ht** - Voice cloning

**Critical Implementation Details**:
- Stream audio chunks as they're generated
- Convert audio to LINEAR16 PCM format (16kHz sample rate)
- Implement `get_message_up_to()` for interrupt handling
- Handle audio format conversion (MP3 → PCM)

### 4. Output Device (Audio → Client)

**Purpose**: Sends synthesized audio back to the client

**CRITICAL: Rate Limiting for Interrupts**

```python
async def send_speech_to_output(self, message, synthesis_result,
                                stop_event, seconds_per_chunk):
    chunk_idx = 0
    async for chunk_result in synthesis_result.chunk_generator:
        # Check for interrupt
        if stop_event.is_set():
            logger.debug(f"Interrupted after {chunk_idx} chunks")
            message_sent = synthesis_result.get_message_up_to(
                chunk_idx * seconds_per_chunk
            )
            return message_sent, True  # cut_off = True
        
        start_time = time.time()
        
        # Send chunk to output device
        self.output_device.consume_nonblocking(chunk_result.chunk)
        
        # CRITICAL: Wait for chunk to play before sending next one
        # This is what makes interrupts work!
        speech_length = seconds_per_chunk
        processing_time = time.time() - start_time
        await asyncio.sleep(max(speech_length - processing_time, 0))
        
        chunk_idx += 1
    
    return message, False  # cut_off = False
```

**Why Rate Limiting?**
Without rate limiting, all audio chunks would be sent immediately, which would:
- Buffer entire message on client side
- Make interrupts impossible (all audio already sent)
- Cause timing issues

By sending one chunk every N seconds:
- Real-time playback is maintained
- Interrupts can stop mid-sentence
- Natural conversation flow is preserved

## The Interrupt System

The interrupt system is critical for natural conversations.

### How Interrupts Work

**Scenario**: Bot is saying "I think the weather will be nice today and tomorrow and—" when user interrupts with "Stop".

**Step 1: User starts speaking**
```python
# TranscriptionsWorker detects new transcription while bot speaking
async def process(self, transcription):
    if not self.conversation.is_human_speaking:  # Bot was speaking!
        # Broadcast interrupt to all in-flight events
        interrupted = self.conversation.broadcast_interrupt()
        transcription.is_interrupt = interrupted
```

**Step 2: broadcast_interrupt() stops everything**
```python
def broadcast_interrupt(self):
    num_interrupts = 0
    # Interrupt all queued events
    while True:
        try:
            interruptible_event = self.interruptible_events.get_nowait()
            if interruptible_event.interrupt():  # Sets interruption_event
                num_interrupts += 1
        except queue.Empty:
            break
    
    # Cancel current tasks
    self.agent.cancel_current_task()              # Stop generating text
    self.agent_responses_worker.cancel_current_task()  # Stop synthesizing
    return num_interrupts > 0
```

**Step 3: SynthesisResultsWorker detects interrupt**
```python
async def send_speech_to_output(self, synthesis_result, stop_event, ...):
    async for chunk_result in synthesis_result.chunk_generator:
        # Check stop_event (this is the interruption_event)
        if stop_event.is_set():
            logger.debug("Interrupted! Stopping speech.")
            # Calculate what was actually spoken
            seconds_spoken = chunk_idx * seconds_per_chunk
            partial_message = synthesis_result.get_message_up_to(seconds_spoken)
            # e.g., "I think the weather will be nice today"
            return partial_message, True  # cut_off = True
```

**Step 4: Agent updates history**
```python
if cut_off:
    # Update conversation history with partial message
    self.agent.update_last_bot_message_on_cut_off(message_sent)
    # History now shows:
    # Bot: "I think the weather will be nice today" (incomplete)
```

### InterruptibleEvent Pattern

Every event in the pipeline is wrapped in an `InterruptibleEvent`:

```python
class InterruptibleEvent:
    def __init__(self, payload, is_interruptible=True):
        self.payload = payload
        self.is_interruptible = is_interruptible
        self.interruption_event = threading.Event()  # Initially not set
        self.interrupted = False
    
    def interrupt(self) -> bool:
        """Interrupt this event"""
        if not self.is_interruptible:
            return False
        if not self.interrupted:
            self.interruption_event.set()  # Signal to stop!
            self.interrupted = True
            return True
        return False
    
    def is_interrupted(self) -> bool:
        return self.interruption_event.is_set()
```

## Multi-Provider Factory Pattern

Support multiple providers with a factory pattern:

```python
class VoiceHandler:
    """Multi-provider factory for voice components"""
    
    def create_transcriber(self, agent_config: Dict):
        """Create transcriber based on transcriberProvider"""
        provider = agent_config.get("transcriberProvider", "deepgram")
        
        if provider == "deepgram":
            return self._create_deepgram_transcriber(agent_config)
        elif provider == "assemblyai":
            return self._create_assemblyai_transcriber(agent_config)
        elif provider == "azure":
            return self._create_azure_transcriber(agent_config)
        elif provider == "google":
            return self._create_google_transcriber(agent_config)
        else:
            raise ValueError(f"Unknown transcriber provider: {provider}")
    
    def create_agent(self, agent_config: Dict):
        """Create LLM agent based on llmProvider"""
        provider = agent_config.get("llmProvider", "openai")
        
        if provider == "openai":
            return self._create_openai_agent(agent_config)
        elif provider == "gemini":
            return self._create_gemini_agent(agent_config)
        else:
            raise ValueError(f"Unknown LLM provider: {provider}")
    
    def create_synthesizer(self, agent_config: Dict):
        """Create voice synthesizer based on voiceProvider"""
        provider = agent_config.get("voiceProvider", "elevenlabs")
        
        if provider == "elevenlabs":
            return self._create_elevenlabs_synthesizer(agent_config)
        elif provider == "azure":
            return self._create_azure_synthesizer(agent_config)
        elif provider == "google":
            return self._create_google_synthesizer(agent_config)
        elif provider == "polly":
            return self._create_polly_synthesizer(agent_config)
        elif provider == "playht":
            return self._create_playht_synthesizer(agent_config)
        else:
            raise ValueError(f"Unknown voice provider: {provider}")
```

## WebSocket Integration

Voice AI engines typically use WebSocket for bidirectional audio streaming:

```python
@app.websocket("/conversation")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    # Create voice components
    voice_handler = VoiceHandler()
    transcriber = voice_handler.create_transcriber(agent_config)
    agent = voice_handler.create_agent(agent_config)
    synthesizer = voice_handler.create_synthesizer(agent_config)
    
    # Create output device
    output_device = WebsocketOutputDevice(
        ws=websocket,
        sampling_rate=16000,
        audio_encoding=AudioEncoding.LINEAR16
    )
    
    # Create conversation orchestrator
    conversation = StreamingConversation(
        output_device=output_device,
        transcriber=transcriber,
        agent=agent,
        synthesizer=synthesizer
    )
    
    # Start all workers
    await conversation.start()
    
    try:
        # Receive audio from client
        async for message in websocket.iter_bytes():
            conversation.receive_audio(message)
    except WebSocketDisconnect:
        logger.info("Client disconnected")
    finally:
        await conversation.terminate()
```

## Common Pitfalls and Solutions

### 1. Audio Jumping/Cutting Off

**Problem**: Bot's audio jumps or cuts off mid-response.

**Cause**: Sending text to synthesizer in small chunks causes multiple TTS calls.

**Solution**: Buffer the entire LLM response before sending to synthesizer:

```python
# ❌ Bad: Yields sentence-by-sentence
async for sentence in llm_stream:
    yield GeneratedResponse(message=BaseMessage(text=sentence))

# ✅ Good: Buffer entire response
full_response = ""
async for chunk in llm_stream:
    full_response += chunk
yield GeneratedResponse(message=BaseMessage(text=full_response))
```

### 2. Echo/Feedback Loop

**Problem**: Bot hears itself speaking and responds to its own audio.

**Cause**: Transcriber not muted during bot speech.

**Solution**: Mute transcriber when bot starts speaking:

```python
# Before sending audio to output
self.transcriber.mute()
# After audio playback complete
self.transcriber.unmute()
```

### 3. Interrupts Not Working

**Problem**: User can't interrupt bot mid-sentence.

**Cause**: All audio chunks sent at once instead of rate-limited.

**Solution**: Rate-limit audio chunks to match real-time playback:

```python
async for chunk in synthesis_result.chunk_generator:
    start_time = time.time()
    
    # Send chunk
    output_device.consume_nonblocking(chunk)
    
    # Wait for chunk duration before sending next
    processing_time = time.time() - start_time
    await asyncio.sleep(max(seconds_per_chunk - processing_time, 0))
```

### 4. Memory Leaks from Unclosed Streams

**Problem**: Memory usage grows over time.

**Cause**: WebSocket connections or API streams not properly closed.

**Solution**: Always use context managers and cleanup:

```python
try:
    async with websockets.connect(url) as ws:
        # Use websocket
        pass
finally:
    # Cleanup
    await conversation.terminate()
    await transcriber.terminate()
```

## Production Considerations

### 1. Error Handling

```python
async def _run_loop(self):
    while self.active:
        try:
            item = await self.input_queue.get()
            await self.process(item)
        except Exception as e:
            logger.error(f"Worker error: {e}", exc_info=True)
            # Don't crash the worker, continue processing
```

### 2. Graceful Shutdown

```python
async def terminate(self):
    """Gracefully shut down all workers"""
    self.active = False
    
    # Stop all workers
    self.transcriber.terminate()
    self.agent.terminate()
    self.synthesizer.terminate()
    
    # Wait for queues to drain
    await asyncio.sleep(0.5)
    
    # Close connections
    if self.websocket:
        await self.websocket.close()
```

### 3. Monitoring and Logging

```python
# Log key events
logger.info(f"🎤 [TRANSCRIBER] Received: '{transcription.message}'")
logger.info(f"🤖 [AGENT] Generating response...")
logger.info(f"🔊 [SYNTHESIZER] Synthesizing {len(text)} characters")
logger.info(f"⚠️ [INTERRUPT] User interrupted bot")

# Track metrics
metrics.increment("transcriptions.count")
metrics.timing("agent.response_time", duration)
metrics.gauge("active_conversations", count)
```

### 4. Rate Limiting and Quotas

```python
# Implement rate limiting for API calls
from aiolimiter import AsyncLimiter

rate_limiter = AsyncLimiter(max_rate=10, time_period=1)  # 10 calls/second

async def call_api(self, data):
    async with rate_limiter:
        return await self.client.post(data)
```

## Key Design Patterns

### 1. Producer-Consumer with Queues

```python
# Producer
async def producer(queue):
    while True:
        item = await generate_item()
        queue.put_nowait(item)

# Consumer
async def consumer(queue):
    while True:
        item = await queue.get()
        await process_item(item)
```

### 2. Streaming Generators

Instead of returning complete results:

```python
# ❌ Bad: Wait for entire response
async def generate_response(prompt):
    response = await openai.complete(prompt)  # 5 seconds
    return response

# ✅ Good: Stream chunks as they arrive
async def generate_response(prompt):
    async for chunk in openai.complete(prompt, stream=True):
        yield chunk  # Yield after 0.1s, 0.2s, etc.
```

### 3. Conversation State Management

Maintain conversation history for context:

```python
class Transcript:
    event_logs: List[Message] = []
    
    def add_human_message(self, text):
        self.event_logs.append(Message(sender=Sender.HUMAN, text=text))
    
    def add_bot_message(self, text):
        self.event_logs.append(Message(sender=Sender.BOT, text=text))
    
    def to_openai_messages(self):
        return [
            {"role": "user" if msg.sender == Sender.HUMAN else "assistant",
             "content": msg.text}
            for msg in self.event_logs
        ]
```

## Testing Strategies

### 1. Unit Test Workers in Isolation

```python
async def test_transcriber():
    transcriber = DeepgramTranscriber(config)
    
    # Mock audio input
    audio_chunk = b'\x00\x01\x02...'
    transcriber.send_audio(audio_chunk)
    
    # Check output
    transcription = await transcriber.output_queue.get()
    assert transcription.message == "expected text"
```

### 2. Integration Test Pipeline

```python
async def test_full_pipeline():
    # Create all components
    conversation = create_test_conversation()
    
    # Send test audio
    conversation.receive_audio(test_audio_chunk)
    
    # Wait for response
    response = await wait_for_audio_output(timeout=5)
    
    assert response is not None
```

### 3. Test Interrupts

```python
async def test_interrupt():
    conversation = create_test_conversation()
    
    # Start bot speaking
    await conversation.agent.generate_response("Tell me a long story")
    
    # Interrupt mid-response
    await asyncio.sleep(1)  # Let it speak for 1 second
    conversation.broadcast_interrupt()
    
    # Verify partial message in transcript
    last_message = conversation.transcript.event_logs[-1]
    assert last_message.text != full_expected_message
```

## Implementation Workflow

When implementing a voice AI engine:

1. **Start with Base Workers**: Implement the base worker pattern first
2. **Add Transcriber**: Choose a provider and implement streaming transcription
3. **Add Agent**: Implement LLM integration with streaming responses
4. **Add Synthesizer**: Implement TTS with audio streaming
5. **Connect Pipeline**: Wire all workers together with queues
6. **Add Interrupts**: Implement the interrupt system
7. **Add WebSocket**: Create WebSocket endpoint for client communication
8. **Test Components**: Unit test each worker in isolation
9. **Test Integration**: Test the full pipeline end-to-end
10. **Add Error Handling**: Implement robust error handling and logging
11. **Optimize**: Add rate limiting, monitoring, and performance optimizations

## Related Skills

- `@websocket-patterns` - For WebSocket implementation details
- `@async-python` - For asyncio and async patterns
- `@streaming-apis` - For streaming API integration
- `@audio-processing` - For audio format conversion and processing
- `@systematic-debugging` - For debugging complex async pipelines

## Resources

**Libraries**:
- `asyncio` - Async programming
- `websockets` - WebSocket client/server
- `FastAPI` - WebSocket server framework
- `pydub` - Audio manipulation
- `numpy` - Audio data processing

**API Providers**:
- Transcription: Deepgram, AssemblyAI, Azure Speech, Google Cloud Speech
- LLM: OpenAI, Google Gemini, Anthropic Claude
- TTS: ElevenLabs, Azure TTS, Google Cloud TTS, Amazon Polly, Play.ht

## Summary

Building a voice AI engine requires:
- ✅ Async worker pipeline for concurrent processing
- ✅ Queue-based communication between components
- ✅ Streaming at every stage (transcription, LLM, synthesis)
- ✅ Interrupt system for natural conversations
- ✅ Rate limiting for real-time audio playback
- ✅ Multi-provider support for flexibility
- ✅ Proper error handling and graceful shutdown

**The key insight**: Everything must stream and everything must be interruptible for natural, real-time conversations.


## voice-engine / common_pitfalls.md

# Common Pitfalls and Solutions

This document covers common issues encountered when building voice AI engines and their solutions.

## 1. Audio Jumping/Cutting Off

### Problem
The bot's audio jumps or cuts off mid-response, creating a jarring user experience.

### Symptoms
- Audio plays in fragments
- Sentences are incomplete
- Multiple audio streams overlap
- Unnatural pauses or gaps

### Root Cause
Sending text to the synthesizer in small chunks (sentence-by-sentence or word-by-word) causes multiple TTS API calls. Each call generates a separate audio stream, resulting in:
- Multiple audio files being played sequentially
- Timing issues between chunks
- Potential overlapping audio
- Inconsistent voice characteristics between chunks

### Solution
Buffer the entire LLM response before sending it to the synthesizer:

**❌ Bad: Yields sentence-by-sentence**
```python
async def generate_response(self, prompt):
    async for sentence in llm_stream:
        # This creates multiple TTS calls!
        yield GeneratedResponse(message=BaseMessage(text=sentence))
```

**✅ Good: Buffer entire response**
```python
async def generate_response(self, prompt):
    # Buffer the entire response
    full_response = ""
    async for chunk in llm_stream:
        full_response += chunk
    
    # Yield once with complete response
    yield GeneratedResponse(message=BaseMessage(text=full_response))
```

### Why This Works
- Single TTS call for the entire response
- Consistent voice characteristics
- Proper timing and pacing
- No gaps or overlaps

---

## 2. Echo/Feedback Loop

### Problem
The bot hears itself speaking and responds to its own audio, creating an infinite loop.

### Symptoms
- Bot responds to its own speech
- Conversation becomes nonsensical
- Transcriptions include bot's own words
- System becomes unresponsive

### Root Cause
The transcriber continues to process audio while the bot is speaking. If the bot's audio is being played through speakers and captured by the microphone, the transcriber will transcribe the bot's own speech.

### Solution
Mute the transcriber when the bot starts speaking:

```python
# Before sending audio to output
self.transcriber.mute()

# Send audio...
await self.send_speech_to_output(synthesis_result)

# After audio playback complete
self.transcriber.unmute()
```

### Implementation in Transcriber
```python
class BaseTranscriber:
    def __init__(self):
        self.is_muted = False
    
    def send_audio(self, chunk: bytes):
        """Client calls this to send audio"""
        if not self.is_muted:
            self.input_queue.put_nowait(chunk)
        else:
            # Send silence instead (prevents echo)
            self.input_queue.put_nowait(self.create_silent_chunk(len(chunk)))
    
    def mute(self):
        """Called when bot starts speaking"""
        self.is_muted = True
    
    def unmute(self):
        """Called when bot stops speaking"""
        self.is_muted = False
    
    def create_silent_chunk(self, size: int) -> bytes:
        """Create a silent audio chunk"""
        return b'\x00' * size
```

### Why This Works
- Transcriber receives silence while bot speaks
- No transcription of bot's own speech
- Prevents feedback loop
- Maintains audio stream continuity

---

## 3. Interrupts Not Working

### Problem
Users cannot interrupt the bot mid-sentence. The bot continues speaking even when the user starts talking.

### Symptoms
- Bot speaks over user
- User must wait for bot to finish
- Unnatural conversation flow
- Poor user experience

### Root Cause
All audio chunks are sent to the client immediately, buffering the entire message on the client side. By the time an interrupt is detected, all audio has already been sent and is queued for playback.

### Solution
Rate-limit audio chunks to match real-time playback:

**❌ Bad: Send all chunks immediately**
```python
async for chunk in synthesis_result.chunk_generator:
    # Sends all chunks as fast as possible
    output_device.consume_nonblocking(chunk)
```

**✅ Good: Rate-limit chunks**
```python
async for chunk in synthesis_result.chunk_generator:
    # Check for interrupt
    if stop_event.is_set():
        # Calculate partial message
        partial_message = synthesis_result.get_message_up_to(
            chunk_idx * seconds_per_chunk
        )
        return partial_message, True  # cut_off = True
    
    start_time = time.time()
    
    # Send chunk
    output_device.consume_nonblocking(chunk)
    
    # CRITICAL: Wait for chunk duration before sending next
    processing_time = time.time() - start_time
    await asyncio.sleep(max(seconds_per_chunk - processing_time, 0))
    
    chunk_idx += 1
```

### Why This Works
- Only one chunk is buffered on client at a time
- Interrupts can stop mid-sentence
- Natural conversation flow
- Real-time playback maintained

### Calculating `seconds_per_chunk`
```python
# For LINEAR16 PCM audio at 16kHz
sample_rate = 16000  # Hz
chunk_size = 1024    # bytes
bytes_per_sample = 2  # 16-bit = 2 bytes

samples_per_chunk = chunk_size / bytes_per_sample
seconds_per_chunk = samples_per_chunk / sample_rate
# = 1024 / 2 / 16000 = 0.032 seconds
```

---

## 4. Memory Leaks from Unclosed Streams

### Problem
Memory usage grows over time, eventually causing the application to crash.

### Symptoms
- Increasing memory usage
- Slow performance over time
- WebSocket connections not closing
- Resource exhaustion

### Root Cause
WebSocket connections, API streams, or async tasks are not properly closed when conversations end or errors occur.

### Solution
Always use context managers and cleanup:

**❌ Bad: No cleanup**
```python
async def handle_conversation(websocket):
    conversation = create_conversation()
    await conversation.start()
    
    async for message in websocket.iter_bytes():
        conversation.receive_audio(message)
    # No cleanup! Resources leak
```

**✅ Good: Proper cleanup**
```python
async def handle_conversation(websocket):
    conversation = None
    try:
        conversation = create_conversation()
        await conversation.start()
        
        async for message in websocket.iter_bytes():
            conversation.receive_audio(message)
            
    except WebSocketDisconnect:
        logger.info("Client disconnected")
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
    finally:
        # Always cleanup
        if conversation:
            await conversation.terminate()
```

### Proper Termination
```python
async def terminate(self):
    """Gracefully shut down all workers"""
    self.active = False
    
    # Stop all workers
    self.transcriber.terminate()
    self.agent.terminate()
    self.synthesizer.terminate()
    
    # Wait for queues to drain
    await asyncio.sleep(0.5)
    
    # Close connections
    if self.websocket:
        await self.websocket.close()
    
    # Cancel tasks
    for task in self.tasks:
        if not task.done():
            task.cancel()
```

---

## 5. Conversation History Not Updating

### Problem
The agent doesn't remember previous messages or context is lost.

### Symptoms
- Agent repeats itself
- No context from previous messages
- Each response is independent
- Poor conversation quality

### Root Cause
Conversation history is not being maintained or updated correctly.

### Solution
Maintain conversation history in the agent:

```python
class Agent:
    def __init__(self):
        self.conversation_history = []
    
    async def generate_response(self, user_input):
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Generate response with full history
        response = await self.llm.generate(self.conversation_history)
        
        # Add bot response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": response
        })
        
        return response
```

### Handling Interrupts
When the bot is interrupted, update history with partial message:

```python
def update_last_bot_message_on_cut_off(self, partial_message):
    """Update history when bot is interrupted"""
    if self.conversation_history and \
       self.conversation_history[-1]["role"] == "assistant":
        # Update with what was actually spoken
        self.conversation_history[-1]["content"] = partial_message
```

---

## 6. WebSocket Connection Drops

### Problem
WebSocket connections drop unexpectedly, interrupting conversations.

### Symptoms
- Frequent disconnections
- Connection timeouts
- "Connection closed" errors
- Unstable conversations

### Root Cause
- No heartbeat/ping mechanism
- Idle timeout
- Network issues
- Server overload

### Solution
Implement heartbeat and reconnection:

```python
@app.websocket("/conversation")
async def conversation_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    # Start heartbeat
    async def heartbeat():
        while True:
            try:
                await websocket.send_json({"type": "ping"})
                await asyncio.sleep(30)  # Ping every 30 seconds
            except:
                break
    
    heartbeat_task = asyncio.create_task(heartbeat())
    
    try:
        async for message in websocket.iter_bytes():
            # Process message
            pass
    finally:
        heartbeat_task.cancel()
```

---

## 7. High Latency / Slow Responses

### Problem
Long delays between user speech and bot response.

### Symptoms
- Noticeable lag
- Poor user experience
- Conversation feels unnatural
- Users repeat themselves

### Root Causes & Solutions

**1. Not using streaming**
```python
# ❌ Bad: Wait for entire response
response = await llm.complete(prompt)

# ✅ Good: Stream response
async for chunk in llm.complete(prompt, stream=True):
    yield chunk
```

**2. Sequential processing**
```python
# ❌ Bad: Sequential
transcription = await transcriber.transcribe(audio)
response = await agent.generate(transcription)
audio = await synthesizer.synthesize(response)

# ✅ Good: Concurrent with queues
# All workers run simultaneously
```

**3. Large chunk sizes**
```python
# ❌ Bad: Large chunks (high latency)
chunk_size = 8192  # 0.25 seconds

# ✅ Good: Small chunks (low latency)
chunk_size = 1024  # 0.032 seconds
```

---

## 8. Audio Quality Issues

### Problem
Poor audio quality, distortion, or artifacts.

### Symptoms
- Robotic voice
- Crackling or popping
- Distorted audio
- Inconsistent volume

### Root Causes & Solutions

**1. Wrong audio format**
```python
# ✅ Use LINEAR16 PCM at 16kHz
audio_encoding = AudioEncoding.LINEAR16
sample_rate = 16000
```

**2. Incorrect format conversion**
```python
# ✅ Proper MP3 to PCM conversion
from pydub import AudioSegment
import io

def mp3_to_pcm(mp3_bytes):
    audio = AudioSegment.from_mp3(io.BytesIO(mp3_bytes))
    audio = audio.set_frame_rate(16000)
    audio = audio.set_channels(1)
    audio = audio.set_sample_width(2)  # 16-bit
    return audio.raw_data
```

**3. Buffer underruns**
```python
# ✅ Ensure consistent chunk timing
await asyncio.sleep(max(seconds_per_chunk - processing_time, 0))
```

---

## Summary

| Problem | Root Cause | Solution |
|---------|-----------|----------|
| Audio jumping | Multiple TTS calls | Buffer entire response |
| Echo/feedback | Transcriber active during bot speech | Mute transcriber |
| Interrupts not working | All chunks sent immediately | Rate-limit chunks |
| Memory leaks | Unclosed streams | Proper cleanup |
| Lost context | History not maintained | Update conversation history |
| Connection drops | No heartbeat | Implement ping/pong |
| High latency | Sequential processing | Use streaming + queues |
| Poor audio quality | Wrong format/conversion | Use LINEAR16 PCM 16kHz |

---

## Best Practices

1. **Always buffer LLM responses** before sending to synthesizer
2. **Always mute transcriber** when bot is speaking
3. **Always rate-limit audio chunks** to enable interrupts
4. **Always cleanup resources** in finally blocks
5. **Always maintain conversation history** for context
6. **Always use streaming** for low latency
7. **Always use LINEAR16 PCM** at 16kHz for audio
8. **Always implement error handling** in worker loops


## voice-engine / provider_comparison.md

# Provider Comparison Guide

This guide compares different providers for transcription, LLM, and TTS services to help you choose the best option for your voice AI engine.

## Transcription Providers

### Deepgram

**Strengths:**
- ✅ Fastest transcription speed (< 300ms latency)
- ✅ Excellent streaming support
- ✅ High accuracy (95%+ on clear audio)
- ✅ Good pricing ($0.0043/minute)
- ✅ Nova-2 model optimized for real-time
- ✅ Excellent documentation

**Weaknesses:**
- ❌ Less accurate with heavy accents
- ❌ Smaller company (potential reliability concerns)

**Best For:**
- Real-time voice conversations
- Low-latency applications
- English-language applications
- Startups and small businesses

**Configuration:**
```python
{
    "transcriberProvider": "deepgram",
    "deepgramApiKey": "your-api-key",
    "deepgramModel": "nova-2",
    "language": "en-US"
}
```

---

### AssemblyAI

**Strengths:**
- ✅ Very high accuracy (96%+ on clear audio)
- ✅ Excellent with accents and dialects
- ✅ Good speaker diarization
- ✅ Competitive pricing ($0.00025/second)
- ✅ Strong customer support

**Weaknesses:**
- ❌ Slightly higher latency than Deepgram
- ❌ Streaming support is newer

**Best For:**
- Applications requiring highest accuracy
- Multi-speaker scenarios
- Diverse user base with accents
- Enterprise applications

**Configuration:**
```python
{
    "transcriberProvider": "assemblyai",
    "assemblyaiApiKey": "your-api-key",
    "language": "en"
}
```

---

### Azure Speech

**Strengths:**
- ✅ Enterprise-grade reliability
- ✅ Excellent multi-language support (100+ languages)
- ✅ Strong security and compliance
- ✅ Integration with Azure ecosystem
- ✅ Custom model training available

**Weaknesses:**
- ❌ Higher cost ($1/hour)
- ❌ More complex setup
- ❌ Slower than specialized providers

**Best For:**
- Enterprise applications
- Multi-language requirements
- Azure-based infrastructure
- Compliance-sensitive applications

**Configuration:**
```python
{
    "transcriberProvider": "azure",
    "azureSpeechKey": "your-key",
    "azureSpeechRegion": "eastus",
    "language": "en-US"
}
```

---

### Google Cloud Speech

**Strengths:**
- ✅ Excellent multi-language support (125+ languages)
- ✅ Good accuracy
- ✅ Integration with Google Cloud
- ✅ Automatic punctuation
- ✅ Speaker diarization

**Weaknesses:**
- ❌ Higher latency for streaming
- ❌ Complex pricing model
- ❌ Requires Google Cloud account

**Best For:**
- Multi-language applications
- Google Cloud infrastructure
- Applications needing speaker diarization

**Configuration:**
```python
{
    "transcriberProvider": "google",
    "googleCredentials": "path/to/credentials.json",
    "language": "en-US"
}
```

---

## LLM Providers

### OpenAI (GPT-4, GPT-3.5)

**Strengths:**
- ✅ Highest quality responses
- ✅ Excellent instruction following
- ✅ Fast streaming
- ✅ Large context window (128k for GPT-4)
- ✅ Best-in-class reasoning

**Weaknesses:**
- ❌ Higher cost ($0.01-0.03/1k tokens)
- ❌ Rate limits can be restrictive
- ❌ No free tier

**Best For:**
- High-quality conversational AI
- Complex reasoning tasks
- Production applications
- Enterprise use cases

**Configuration:**
```python
{
    "llmProvider": "openai",
    "openaiApiKey": "your-api-key",
    "openaiModel": "gpt-4-turbo",
    "prompt": "You are a helpful AI assistant."
}
```

**Pricing:**
- GPT-4 Turbo: $0.01/1k input tokens, $0.03/1k output tokens
- GPT-3.5 Turbo: $0.0005/1k input tokens, $0.0015/1k output tokens

---

### Google Gemini

**Strengths:**
- ✅ Excellent cost-effectiveness (free tier available)
- ✅ Multimodal capabilities
- ✅ Good streaming support
- ✅ Large context window (1M tokens for Pro)
- ✅ Fast response times

**Weaknesses:**
- ❌ Slightly lower quality than GPT-4
- ❌ Less predictable behavior
- ❌ Newer, less battle-tested

**Best For:**
- Cost-sensitive applications
- Multimodal applications
- Startups and prototypes
- High-volume applications

**Configuration:**
```python
{
    "llmProvider": "gemini",
    "geminiApiKey": "your-api-key",
    "geminiModel": "gemini-pro",
    "prompt": "You are a helpful AI assistant."
}
```

**Pricing:**
- Gemini Pro: Free up to 60 requests/minute
- Gemini Pro (paid): $0.00025/1k input tokens, $0.0005/1k output tokens

---

### Anthropic Claude

**Strengths:**
- ✅ Excellent safety and alignment
- ✅ Very long context window (200k tokens)
- ✅ High-quality responses
- ✅ Good at following complex instructions
- ✅ Strong reasoning capabilities

**Weaknesses:**
- ❌ Higher cost than Gemini
- ❌ Slower streaming than OpenAI
- ❌ More conservative responses

**Best For:**
- Safety-critical applications
- Long-context applications
- Nuanced conversations
- Enterprise applications

**Configuration:**
```python
{
    "llmProvider": "claude",
    "claudeApiKey": "your-api-key",
    "claudeModel": "claude-3-opus",
    "prompt": "You are a helpful AI assistant."
}
```

**Pricing:**
- Claude 3 Opus: $0.015/1k input tokens, $0.075/1k output tokens
- Claude 3 Sonnet: $0.003/1k input tokens, $0.015/1k output tokens

---

## TTS Providers

### ElevenLabs

**Strengths:**
- ✅ Most natural-sounding voices
- ✅ Excellent emotional range
- ✅ Voice cloning capabilities
- ✅ Good streaming support
- ✅ Multiple languages

**Weaknesses:**
- ❌ Higher cost ($0.30/1k characters)
- ❌ Rate limits on lower tiers
- ❌ Occasional pronunciation errors

**Best For:**
- Premium voice experiences
- Customer-facing applications
- Voice cloning needs
- High-quality audio requirements

**Configuration:**
```python
{
    "voiceProvider": "elevenlabs",
    "elevenlabsApiKey": "your-api-key",
    "elevenlabsVoiceId": "voice-id",
    "elevenlabsModel": "eleven_monolingual_v1"
}
```

**Pricing:**
- Free: 10k characters/month
- Starter: $5/month, 30k characters
- Creator: $22/month, 100k characters

---

### Azure TTS

**Strengths:**
- ✅ Enterprise-grade reliability
- ✅ Many languages (100+)
- ✅ Neural voices available
- ✅ SSML support for fine control
- ✅ Good pricing ($4/1M characters)

**Weaknesses:**
- ❌ Less natural than ElevenLabs
- ❌ More complex setup
- ❌ Requires Azure account

**Best For:**
- Enterprise applications
- Multi-language requirements
- Azure-based infrastructure
- Cost-sensitive high-volume applications

**Configuration:**
```python
{
    "voiceProvider": "azure",
    "azureSpeechKey": "your-key",
    "azureSpeechRegion": "eastus",
    "azureVoiceName": "en-US-JennyNeural"
}
```

**Pricing:**
- Neural voices: $16/1M characters
- Standard voices: $4/1M characters

---

### Google Cloud TTS

**Strengths:**
- ✅ Good quality neural voices
- ✅ Many languages (40+)
- ✅ WaveNet voices available
- ✅ Competitive pricing ($4/1M characters)
- ✅ SSML support

**Weaknesses:**
- ❌ Less natural than ElevenLabs
- ❌ Requires Google Cloud account
- ❌ Complex setup

**Best For:**
- Multi-language applications
- Google Cloud infrastructure
- Cost-effective neural voices

**Configuration:**
```python
{
    "voiceProvider": "google",
    "googleCredentials": "path/to/credentials.json",
    "googleVoiceName": "en-US-Neural2-F"
}
```

**Pricing:**
- WaveNet voices: $16/1M characters
- Neural2 voices: $16/1M characters
- Standard voices: $4/1M characters

---

### Amazon Polly

**Strengths:**
- ✅ AWS integration
- ✅ Good pricing ($4/1M characters)
- ✅ Neural voices available
- ✅ SSML support
- ✅ Reliable service

**Weaknesses:**
- ❌ Less natural than ElevenLabs
- ❌ Fewer voice options
- ❌ Requires AWS account

**Best For:**
- AWS-based infrastructure
- Cost-effective neural voices
- Enterprise applications

**Configuration:**
```python
{
    "voiceProvider": "polly",
    "awsAccessKey": "your-access-key",
    "awsSecretKey": "your-secret-key",
    "awsRegion": "us-east-1",
    "pollyVoiceId": "Joanna"
}
```

**Pricing:**
- Neural voices: $16/1M characters
- Standard voices: $4/1M characters

---

### Play.ht

**Strengths:**
- ✅ Voice cloning capabilities
- ✅ Natural-sounding voices
- ✅ Good streaming support
- ✅ Easy to use API
- ✅ Multiple languages

**Weaknesses:**
- ❌ Higher cost than cloud providers
- ❌ Smaller company
- ❌ Less documentation

**Best For:**
- Voice cloning applications
- Premium voice experiences
- Startups and small businesses

**Configuration:**
```python
{
    "voiceProvider": "playht",
    "playhtApiKey": "your-api-key",
    "playhtUserId": "your-user-id",
    "playhtVoiceId": "voice-id"
}
```

**Pricing:**
- Free: 2.5k characters
- Creator: $31/month, 50k characters
- Pro: $79/month, 150k characters

---

## Recommended Combinations

### Budget-Conscious Startup
```python
{
    "transcriberProvider": "deepgram",  # Fast and affordable
    "llmProvider": "gemini",            # Free tier available
    "voiceProvider": "google"           # Cost-effective neural voices
}
```
**Estimated cost:** ~$0.01 per minute of conversation

---

### Premium Experience
```python
{
    "transcriberProvider": "assemblyai",  # Highest accuracy
    "llmProvider": "openai",              # Best quality responses
    "voiceProvider": "elevenlabs"         # Most natural voices
}
```
**Estimated cost:** ~$0.05 per minute of conversation

---

### Enterprise Application
```python
{
    "transcriberProvider": "azure",  # Enterprise reliability
    "llmProvider": "openai",         # Best quality
    "voiceProvider": "azure"         # Enterprise reliability
}
```
**Estimated cost:** ~$0.03 per minute of conversation

---

### Multi-Language Application
```python
{
    "transcriberProvider": "google",  # 125+ languages
    "llmProvider": "gemini",          # Good multi-language support
    "voiceProvider": "google"         # 40+ languages
}
```
**Estimated cost:** ~$0.02 per minute of conversation

---

## Decision Matrix

| Priority | Transcriber | LLM | TTS |
|----------|-------------|-----|-----|
| **Lowest Cost** | Deepgram | Gemini | Google |
| **Highest Quality** | AssemblyAI | OpenAI | ElevenLabs |
| **Fastest Speed** | Deepgram | OpenAI | ElevenLabs |
| **Enterprise** | Azure | OpenAI | Azure |
| **Multi-Language** | Google | Gemini | Google |
| **Voice Cloning** | N/A | N/A | ElevenLabs/Play.ht |

---

## Testing Recommendations

Before committing to providers, test with your specific use case:

1. **Create test conversations** with representative audio
2. **Measure latency** end-to-end
3. **Evaluate quality** with real users
4. **Calculate costs** based on expected volume
5. **Test edge cases** (accents, background noise, interrupts)

---

## Switching Providers

The multi-provider factory pattern makes switching easy:

```python
# Just change the configuration
config = {
    "transcriberProvider": "deepgram",  # Change to "assemblyai"
    "llmProvider": "gemini",            # Change to "openai"
    "voiceProvider": "google"           # Change to "elevenlabs"
}

# No code changes needed!
factory = VoiceComponentFactory()
transcriber = factory.create_transcriber(config)
agent = factory.create_agent(config)
synthesizer = factory.create_synthesizer(config)
```
