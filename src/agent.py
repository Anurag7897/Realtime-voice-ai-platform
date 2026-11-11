from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentServer,
    AgentSession,
    JobContext,
    STTContextOptions,
    TurnHandlingOptions,
    cli,
    inference,
    room_io,
)
from livekit.plugins import ai_coustics

from prompts import AGENT_INSTRUCTIONS, GREETING_INSTRUCTIONS

load_dotenv(".env.local")


class AnuragVoiceAgent(Agent):
    """Real-time conversational voice agent."""

    def __init__(self) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTIONS,
        )

    async def on_enter(self) -> None:
        """Greet the user when the agent becomes active."""
        await self.session.generate_reply(
            instructions=GREETING_INSTRUCTIONS,
        )


server = AgentServer()


@server.rtc_session(agent_name="realtime-voice-ai-platform")
async def my_agent(ctx: JobContext) -> None:
    """Create and start a real-time voice agent session."""

    ctx.log_context_fields = {
        "room": ctx.room.name,
    }

    session = AgentSession(
        stt=inference.STT(
            model="assemblyai/universal-3-6-pro",
            language="en",
        ),
        llm=inference.LLM(
            model="google/gemma-4-31b-it",
        ),
        stt_context_options=STTContextOptions(
            keyterms=[
                "LiveKit",
                "Anurag",
                "Anurag Mahajan",
                "Anurag's Voice Agent",
            ],
            keyterm_detection={
                "enabled": True,
            },
        ),
        tts=inference.TTS(
            model="fishaudio/s2.1-pro",
            voice="fa4c9eb3dccc4806b382b40d61c6b10a",
        ),
        turn_handling=TurnHandlingOptions(
            turn_detection=inference.TurnDetector(),
            preemptive_generation={
                "enabled": True,
            },
        ),
        expressive=True,
    )

    await session.start(
        agent=AnuragVoiceAgent(),
        room=ctx.room,
        room_options=room_io.RoomOptions(
            audio_input=room_io.AudioInputOptions(
                noise_cancellation=ai_coustics.audio_enhancement(
                    model=ai_coustics.EnhancerModel.QUAIL_VF_S,
                ),
            ),
        ),
    )

    await ctx.connect()


if __name__ == "__main__":
    cli.run_app(server)
