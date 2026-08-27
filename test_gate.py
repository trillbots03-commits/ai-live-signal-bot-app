from app.signals.gate import a_plus_gate


def test_91_never_qualifies():
    result = a_plus_gate(91, {}, True, True)
    assert not result.eligible


def test_92_requires_all_gates():
    result = a_plus_gate(92, {"risk": False}, True, True)
    assert not result.eligible


def test_92_qualifies_when_all_pass():
    result = a_plus_gate(92, {"risk": True, "data": True}, True, True)
    assert result.eligible
