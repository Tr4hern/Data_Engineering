import warnings
warnings.filterwarnings('ignore')
import toxicity

def check_threshold():
    result = toxicity.detoxify_analyse("bitch")
    for i in result.keys():
        if result[i] < 0.5:
            return False
    return True

def english():
    result = toxicity.detoxify_analyse("connard")
    return result['Toxicity Detector']

def not_toxic():
    result = toxicity.detoxify_analyse("it's a beautiful day")
    return result['Toxicity Detector']


def test_toxicity_json():
    assert len(toxicity.detoxify_analyse("test")) <= 7
    assert check_threshold() == True
    assert isinstance(english(), str)
    assert isinstance(not_toxic(), str)


def test_json_to_text():
    assert isinstance(toxicity.detoxify_json_to_string(toxicity.detoxify_analyse("test")), str)