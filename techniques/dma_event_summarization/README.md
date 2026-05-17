# DMA Event Summarization

Convert noisy DMA logs into structured event counts or timelines. This makes
low-level debugging easier for agents and humans.

Use this in firmware workflows with transfer-complete, transfer-error, and
channel-state logs.

This example counts simulated DMA transfer-complete and transfer-error events.

```powershell
python .\techniques\dma_event_summarization\agent_example.py
```
