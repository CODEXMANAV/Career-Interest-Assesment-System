from assessor import assess

def test_assess():
    result = assess([("technology", "y"), ("technology", "y"), ("creative", "n")])
    assert result["area"] == "Technology"
    assert result["score"] == 2

if __name__ == "__main__":
    test_assess()
    print("All basic tests passed.")
