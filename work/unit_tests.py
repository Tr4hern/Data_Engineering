import warnings
warnings.filterwarnings('ignore')
import toxicity

def test_toxicity_json():
    assert len(toxicity.detoxify_analyse("test")) == 7


def test_json_to_text():
    assert isinstance(toxicity.detoxify_json_to_string(toxicity.detoxify_analyse("test")), str)