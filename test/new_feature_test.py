from app.new_feature import announce

def test_enlarge():
    result = announce()
    assert result == "hello world"