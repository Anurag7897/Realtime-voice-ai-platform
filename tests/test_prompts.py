from prompts import AGENT_INSTRUCTIONS, GREETING_INSTRUCTIONS

AGENT_NAME = "Anurag's Voice Agent"
CREATOR_NAME = "Anurag Mahajan"


def test_agent_identity_is_defined() -> None:
    assert AGENT_NAME in AGENT_INSTRUCTIONS


def test_creator_identity_is_defined() -> None:
    assert CREATOR_NAME in AGENT_INSTRUCTIONS


def test_greeting_includes_agent_name() -> None:
    assert AGENT_NAME in GREETING_INSTRUCTIONS
