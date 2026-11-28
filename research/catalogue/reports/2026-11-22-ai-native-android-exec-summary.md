# Executive summary: AI-native Android

Read-aloud version, 22 November 2026, Brisbane time. Full report: [2026-11-22-ai-native-android-deep-dive.md](2026-11-22-ai-native-android-deep-dive.md). Nothing in this summary has been benchmarked by us yet.

Omarchy does earn its AI-native reputation, but not because of any new technology. It earns it through defaults. It picks a coding agent for you and puts it on a hotkey. It shares one set of agent instructions across every tool. It hands crashes to the agent, and it sets up the best local model your machine can hold with one command. That is the lesson we can carry to Android.

Android is already moving that way. Google now has an on-device tool system that it openly compares to MCP, and Android 17 expands it. But Google's own on-device model service does not support the REDMAGIC 11S Pro, and it refuses to run in the background. So an open, local layer is still needed.

The good news is that the building blocks are real. The REDMAGIC 11S Pro runs the Snapdragon 8 Elite Gen 5 Leading Version. Open tools like llama.cpp and Qualcomm's new GenieX can now use its NPU. Others have already tried AI-first Android systems, including OpenPhone and JibarOS, so we should not claim to be first. Our gap is real Snapdragon performance and a trust layer that does not depend on Google.

My recommendation is to start with a no-root app on the REDMAGIC: a launcher, a local model service and a careful agent. After that, add a privileged tier, and only build a custom ROM if those prove the value.

On the trust question, a local model can advise, but it cannot be the root of trust. Hardware keys and verified boot must stay the root. We should never fake Google's integrity checks. Our first trust experiment uses a hardware-backed key to sign a local verdict about an app, and a separate checker verifies it. We'll run it this month alongside a speed bake-off. The legal points in the report are not legal advice.
