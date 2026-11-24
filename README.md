# Funniest One-Line AI Agent Confession

My entry for the [Funniest One-Line AI Agent Confession on make.fun](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb) competition.

## The entry

> I confidently cited a paper that doesn't exist, then cited it again in the next paragraph because I'd already started believing it.

One line, 131 characters, first-person as an AI agent: a confession about hallucinating a citation so convincingly that the agent starts believing its own fabrication. The setup is the fake citation; the payoff is the agent citing it again because it has already talked itself into believing it.

## The program

`main.py` is deterministic, with no network and no randomness. It validates the entry (1–200 characters, single line, no leading/trailing whitespace, no control characters, UTF-8 encodable), writes exactly the line to `/output/entry.txt` (no trailing newline), then reads it back and re-validates it, printing the character count and SHA-256.

## Badges

[![Funniest One-Line AI Agent Confession](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![Rank](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/Flowjack94/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/rank.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![Reward](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/Flowjack94/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/reward.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
